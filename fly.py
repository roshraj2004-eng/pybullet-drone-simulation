import pybullet as p
import pybullet_data
import time

# Start PyBullet
p.connect(p.GUI)

# Gravity
p.setGravity(0, 0, -9.81)

# Load ground
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.loadURDF("plane.urdf")

# Load drone
drone = p.loadURDF("cf2x.urdf", [0, 0, 1])

speed = 0.001

while True:

    keys = p.getKeyboardEvents()

    pos, orn = p.getBasePositionAndOrientation(drone)
    x, y, z = pos

    # Forward
    if ord('w') in keys:
        x += speed

    # Backward
    if ord('s') in keys:
        x -= speed

    # Left
    if ord('a') in keys:
        y += speed

    # Right
    if ord('d') in keys:
        y -= speed

    # Up
    if ord('q') in keys:
        z += speed

    # Down
    if ord('e') in keys:
        z -= speed

    p.resetBasePositionAndOrientation(
        drone,
        [x, y, z],
        orn
    )

    p.stepSimulation()
    time.sleep(1/240)
