import os
import carb
from omni.isaac.kit import SimulationApp

def main():
    # Launch Isaac Sim
    simulation_app = SimulationApp({"headless": False})
    
    # Import necessary modules
    from omni.isaac.core import World
    from omni.isaac.core.objects import DynamicCuboid
    from omni.isaac.core.utils.stage import add_reference_to_stage
    
    # Get the directory of this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    
    # Create a new world
    world = World(stage_units_in_meters=1.0)
    
    # Add the combined robot to the stage
    robot_usd_path = os.path.join(project_root, "assets", "ur10_shadow_hand.usd")
    add_reference_to_stage(robot_usd_path, "/ur10_shadow_hand")
    
    # Add a test cube for visual reference
    cube = DynamicCuboid(
        prim_path="/cube",
        position=[0.5, 0.0, 0.5],
        scale=[0.1, 0.1, 0.1],
        color=[0.0, 0.0, 1.0]
    )
    
    # Reset the world
    world.reset()
    
    # Test UR10 arm movements
    print("Testing UR10 arm movements...")
    ur10_prim = world.stage.GetPrimAtPath("/ur10_shadow_hand/ur10")
    if ur10_prim.IsValid():
        # Get all joints
        joints = [child for child in ur10_prim.GetChildren() 
                 if child.GetTypeName() == "RevoluteJoint"]
        
        # Test each joint
        for joint in joints:
            print(f"Testing joint: {joint.GetName()}")
            # Set joint position to 45 degrees
            joint.GetAttribute("xformOp:rotateZ").Set(45.0)
            world.step(render=True)
            
            # Set joint position back to 0 degrees
            joint.GetAttribute("xformOp:rotateZ").Set(0.0)
            world.step(render=True)
    
    # Test Shadow Hand movements
    print("\nTesting Shadow Hand movements...")
    hand_prim = world.stage.GetPrimAtPath("/ur10_shadow_hand/ur10/shadow_hand")
    if hand_prim.IsValid():
        # Get all finger joints
        finger_joints = [child for child in hand_prim.GetChildren() 
                        if "finger" in child.GetName().lower()]
        
        # Test each finger
        for joint in finger_joints:
            print(f"Testing finger joint: {joint.GetName()}")
            # Close finger
            joint.GetAttribute("xformOp:rotateZ").Set(45.0)
            world.step(render=True)
            
            # Open finger
            joint.GetAttribute("xformOp:rotateZ").Set(0.0)
            world.step(render=True)
    
    # Keep the simulation running for visual inspection
    while simulation_app.is_running():
        world.step(render=True)
    
    simulation_app.close()

if __name__ == "__main__":
    main() 