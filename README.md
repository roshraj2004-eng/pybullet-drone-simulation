# PyBullet Drone Simulation

A drone simulation project developed using Python and PyBullet.

## Features

* Drone simulation using a URDF model
* Keyboard-based teleoperation
* Real-time position tracking
* IMU data monitoring
* Circular trajectory generation
* Feedback loop for trajectory tracking

## Controls

| Key | Action          |
| --- | --------------- |
| W   | Move Forward    |
| S   | Move Backward   |
| A   | Move Left       |
| D   | Move Right      |
| Q   | Move Up         |
| E   | Move Down       |
| O   | Circular Motion |
| X   | Stop            |

## Project Structure

* simulation.py – Drone simulation and feedback system
* teleop.py – Keyboard teleoperation
* cf2x.urdf – Drone model

## Technologies Used

* Python
* PyBullet
* URDF

## Future Improvements

* ROS2 Publisher/Subscriber Communication
* PID Control
* Waypoint Navigation
