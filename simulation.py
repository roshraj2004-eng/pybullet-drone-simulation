import pybullet as p
import pybullet_data
import time
import os

# Connect to PyBullet
p.connect(p.GUI)

# No gravity (hover mode)
p.setGravity(0, 0, 0)

# Camera
p.resetDebugVisualizerCamera(
    cameraDistance=3,
    cameraYaw=45,
    cameraPitch=-30,
    cameraTargetPosition=[0, 0, 0]
)

# Ground
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.loadURDF("plane.urdf")

# Drone starts on ground
drone = p.loadURDF("cf2x.urdf", [0, 0, 0.1])

# Start in STOP mode
with open("cmd.txt", "w") as f:
    f.write("x")

current_cmd = "x"

# Smooth slow speed
speed = 0.002

while True:

    # Read latest command
    if os.path.exists("cmd.txt"):
        with open("cmd.txt", "r") as f:
            cmd = f.read().strip().lower()

            if cmd:
                current_cmd = cmd

    pos, _ = p.getBasePositionAndOrientation(drone)

    x, y, z = pos

    roll = 0
    pitch = 0
    yaw = 0

    if current_cmd == "w":
        x += speed
        pitch = -0.08

    elif current_cmd == "s":
        x -= speed
        pitch = 0.08

    elif current_cmd == "a":
        y += speed
        roll = 0.08

    elif current_cmd == "d":
        y -= speed
        roll = -0.08

    elif current_cmd == "q":
        z += speed

    elif current_cmd == "e":
        z = max(0.1, z - speed)

    elif current_cmd == "x":
        pass

    orn = p.getQuaternionFromEuler([roll, pitch, yaw])

    p.resetBasePositionAndOrientation(
        drone,
        [x, y, z],
        orn
    )

    p.stepSimulation()
    time.sleep(1/240)
