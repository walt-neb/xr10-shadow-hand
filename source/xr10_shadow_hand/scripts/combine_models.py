import os
import carb
from pxr import Usd, UsdGeom, Gf, Sdf

def find_end_effector(stage, base_path):
    """Find the end-effector frame in the UR10 arm.
    
    Args:
        stage: The USD stage containing the UR10 arm
        base_path: The base path of the UR10 arm in the stage
        
    Returns:
        The prim path of the end-effector frame, or None if not found
    """
    # Common end-effector frame names
    eef_names = ["tool0", "wrist_3_link", "ee_link", "end_effector"]
    
    for name in eef_names:
        eef_path = f"{base_path}/{name}"
        prim = stage.GetPrimAtPath(eef_path)
        if prim and prim.IsValid():
            return eef_path
    
    # If no common names found, try to find the last link
    prim = stage.GetPrimAtPath(base_path)
    if not prim or not prim.IsValid():
        return None
        
    # Get all children and find links
    links = [child for child in prim.GetChildren() if "link" in child.GetName().lower()]
    if not links:
        return None
        
    # Return the last link's path
    return links[-1].GetPath().pathString

def combine_models(ur10_usd_path: str, shadow_hand_usd_path: str, output_usd_path: str):
    """Combine UR10 arm and Shadow hand USD files into a single USD file.
    
    Args:
        ur10_usd_path (str): Path to UR10 arm USD file
        shadow_hand_usd_path (str): Path to Shadow hand USD file
        output_usd_path (str): Path where to save the combined USD file
    """
    # Create a new stage
    stage = Usd.Stage.CreateNew(output_usd_path)
    
    # Load UR10 arm
    ur10_stage = Usd.Stage.Open(ur10_usd_path)
    if not ur10_stage:
        carb.log_error(f"Failed to open UR10 USD file: {ur10_usd_path}")
        return False
    
    # Load Shadow hand
    shadow_stage = Usd.Stage.Open(shadow_hand_usd_path)
    if not shadow_stage:
        carb.log_error(f"Failed to open Shadow Hand USD file: {shadow_hand_usd_path}")
        return False
    
    # Copy UR10 arm to new stage
    ur10_prim = stage.DefinePrim("/ur10", "Xform")
    ur10_prim.GetReferences().AddReference(ur10_usd_path)
    
    # Find the end-effector frame of the UR10 arm
    eef_path = find_end_effector(stage, "/ur10")
    if not eef_path:
        carb.log_error("Could not find UR10 end-effector frame")
        return False
        
    print(f"Found end-effector frame at: {eef_path}")
    
    # Create a new Xform for the Shadow hand at the end-effector location
    hand_xform = UsdGeom.Xform.Define(stage, f"{eef_path}/shadow_hand")
    
    # Add reference to the Shadow hand model
    hand_xform.GetPrim().GetReferences().AddReference(shadow_hand_usd_path)
    
    # Set up the transformation for the Shadow hand
    xformAPI = UsdGeom.XformCommonAPI(hand_xform)
    
    # Rotate the hand to align with the end effector
    # 90 degrees around X to point fingers forward
    # 180 degrees around Z to align palm orientation
    rotation = Gf.Vec3d(90.0, 0.0, 180.0)
    
    # Translate to align the hand's base with the end effector
    # Adjust these values based on your specific hand model
    translation = Gf.Vec3d(0.0, 0.0, 0.0)
    
    # Apply the transformation
    xformAPI.SetRotate(rotation)
    xformAPI.SetTranslate(translation)
    
    # Save the stage
    stage.Save()
    print(f"Saved combined USD file to: {output_usd_path}")
    
    return True

def test_movements(stage_path: str):
    """Test basic movements of the combined robot.
    
    Args:
        stage_path (str): Path to the combined USD file
    """
    stage = Usd.Stage.Open(stage_path)
    if not stage:
        carb.log_error(f"Failed to open combined USD file: {stage_path}")
        return
    
    # Test UR10 arm movements
    ur10_prim = stage.GetPrimAtPath("/ur10")
    if ur10_prim and ur10_prim.IsValid():
        print("UR10 arm found, testing joints...")
        # List all joints
        joints = [child for child in ur10_prim.GetChildren() 
                 if child.GetTypeName() == "RevoluteJoint"]
        print(f"Found {len(joints)} joints in UR10 arm")
        
        # Test each joint
        for joint in joints:
            print(f"Testing joint: {joint.GetName()}")
            # Here you would add code to test joint movement
            # This is typically done through Isaac Sim's Python API
    else:
        print("UR10 arm not found in combined USD file")
    
    # Test Shadow Hand movements
    hand_prim = stage.GetPrimAtPath("/ur10/shadow_hand")
    if hand_prim and hand_prim.IsValid():
        print("Shadow Hand found, testing fingers...")
        # List all finger joints
        finger_joints = [child for child in hand_prim.GetChildren() 
                        if "finger" in child.GetName().lower()]
        print(f"Found {len(finger_joints)} finger joints in Shadow Hand")
        
        # Test each finger
        for joint in finger_joints:
            print(f"Testing finger joint: {joint.GetName()}")
            # Here you would add code to test finger movement
            # This is typically done through Isaac Sim's Python API
    else:
        print("Shadow Hand not found in combined USD file")

if __name__ == "__main__":
    # Get the directory of this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    
    # Define paths
    ur10_usd_path = os.path.join(project_root, "assets", "UR10.usd")
    shadow_hand_usd_path = os.path.join(project_root, "assets", "shadow_hand.usd")
    output_usd_path = os.path.join(project_root, "assets", "ur10_shadow_hand.usd")
    
    # Check if input files exist
    if not os.path.exists(ur10_usd_path):
        print(f"Error: UR10 USD file not found at: {ur10_usd_path}")
        exit(1)
        
    if not os.path.exists(shadow_hand_usd_path):
        print(f"Error: Shadow Hand USD file not found at: {shadow_hand_usd_path}")
        exit(1)
    
    # Create assets directory if it doesn't exist
    os.makedirs(os.path.dirname(output_usd_path), exist_ok=True)
    
    # Combine models
    print("Combining UR10 and Shadow Hand models...")
    success = combine_models(ur10_usd_path, shadow_hand_usd_path, output_usd_path)
    
    if success:
        print(f"Successfully created combined USD file at: {output_usd_path}")
        print("\nTesting movements...")
        test_movements(output_usd_path)
    else:
        print("Failed to create combined USD file") 