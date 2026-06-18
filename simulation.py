import pybullet as p
import pybullet_data
import time
import os

# Start PyBullet
p.connect(p.GUI)

# No gravity
p.setGravity(0, 0, 0)

# Load ground
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.loadURDF("plane.urdf")

# Drone starts on ground
drone = p.loadURDF("cf2x.urdf", [0, 0, 0.1])

# Smooth speed
speed = 0.02

while True:

    pos, orn = p.getBasePositionAndOrientation(drone)

    x = pos[0]
    y = pos[1]
    z = pos[2]

    if os.path.exists("cmd.txt"):

        with open("cmd.txt", "r") as f:
            cmd = f.read().strip().lower()

        if cmd == "w":
            x += speed

        elif cmd == "s":
            x -= speed

        elif cmd == "a":
            y += speed

        elif cmd == "d":
            y -= speed

        elif cmd == "q":
            z += speed

        elif cmd == "e":
            z = max(0.1, z - speed)

        # clear command
        with open("cmd.txt", "w") as f:
            f.write("")

    p.resetBasePositionAndOrientation(
        drone,
        [x, y, z],
        orn
    )

    p.stepSimulation()
    time.sleep(1/240)
