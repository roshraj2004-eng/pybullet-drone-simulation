import pybullet as p
import pybullet_data
import time
import os
import math

# Connect
p.connect(p.GUI)

p.setGravity(0, 0, 0)

p.resetDebugVisualizerCamera(
    cameraDistance=3,
    cameraYaw=45,
    cameraPitch=-30,
    cameraTargetPosition=[0, 0, 0]
)

p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.loadURDF("plane.urdf")

drone = p.loadURDF("cf2x.urdf", [0, 0, 0.1])

print("\nJOINTS FOUND:\n")

for i in range(p.getNumJoints(drone)):
    print(i, p.getJointInfo(drone, i)[12].decode())

print("\n---------------------\n")

# Command file
with open("cmd.txt", "w") as f:
    f.write("x")

current_cmd = "x"

speed = 0.002

counter = 0

# Circular motion parameters
radius = 1.0
theta = 0.0
angular_speed = 0.002

while True:

    # Read command
    if os.path.exists("cmd.txt"):
        with open("cmd.txt", "r") as f:
            cmd = f.read().strip().lower()

            if cmd:
                current_cmd = cmd

    pos, orn_old = p.getBasePositionAndOrientation(drone)

    x, y, z = pos

    roll = 0
    pitch = 0
    yaw = 0

    # --------------------
    # Manual Control
    # --------------------

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

    # --------------------
    # Circular Motion
    # --------------------

    elif current_cmd == "o":

        target_x = radius * math.cos(theta)
        target_y = radius * math.sin(theta)

        error_x = target_x - x
        error_y = target_y - y

        # Simple feedback controller
        Kp = 0.05

        x += Kp * error_x
        y += Kp * error_y

        yaw = theta

        theta += angular_speed

        if counter % 120 == 0:

            print("\n===== FEEDBACK LOOP =====")

            print(
                f"Target Position : "
                f"({target_x:.3f}, {target_y:.3f})"
            )

            print(
                f"Actual Position : "
                f"({x:.3f}, {y:.3f})"
            )

            print(
                f"Error : "
                f"({error_x:.3f}, {error_y:.3f})"
            )

    elif current_cmd == "x":
        pass

    quaternion = p.getQuaternionFromEuler(
        [roll, pitch, yaw]
    )

    p.resetBasePositionAndOrientation(
        drone,
        [x, y, z],
        quaternion
    )

    # IMU Data
    position, orientation = \
        p.getBasePositionAndOrientation(drone)

    linear_velocity, angular_velocity = \
        p.getBaseVelocity(drone)

    counter += 1

    if counter % 240 == 0:

        print("\n===== IMU DATA =====")

        print("Position:", position)

        print("Orientation:", orientation)

        print(
            "Linear Velocity:",
            linear_velocity
        )

        print(
            "Angular Velocity:",
            angular_velocity
        )

    with open("imu.txt", "w") as imu_file:

        imu_file.write(
            f"Position: {position}\n"
            f"Orientation: {orientation}\n"
            f"Linear Velocity: {linear_velocity}\n"
            f"Angular Velocity: {angular_velocity}\n"
        )

    p.stepSimulation()

    time.sleep(1 / 240)
