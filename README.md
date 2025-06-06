# TurtleBot3 GUI Controller – ROS 2 + Gazebo Project

This project consists of controlling a TurtleBot3 robot in a Gazebo simulation environment using a custom Python-based GUI. 
Two different interfaces are provided: one using `tkinter` (button-based control) and another using pygame (click-based directional control). 
The system is built using ROS 2 Humble inside a Docker Dev Container with Gazebo simulation support.

---

## Requirements

- Docker Desktop
- VS Code with Dev Containers extension
- XLaunch (X11 server)
- ROS 2 Humble + Gazebo 11
- Internet connection for first-time setup

---

## Steps to Launch the Project

### 1. Environment Setup

1. **Run** XLaunch Server with default settings.
2. **Start** Docker Desktop (in the background).
3. **Open** VS Code and load the folder 'ros2_ws_template'.
4. Press 'F1' → choose:'`Dev Containers: Rebuild and Reopen in Container'.
5. Wait until the container is fully initialized (may take a few minutes the first time).

---

### 2. Build and install dependencies

Open a terminal inside the container and run:

'''
colcon build
source /opt/ros/humble/setup.bash
source install/setup.bash
sudo apt update
sudo apt install ros-humble-turtlebot3* ros-humble-gazebo-ros-pkgs
export TURTLEBOT3_MODEL=burger
ros2 launch turtlebot3_gazebo turtlebot3_house.launch.py
'''

This launches the TurtleBot3 inside a simulated house in Gazebo.

---

### 3. Run the GUI node

Open **another terminal** and execute:

'''
cd ~/ros2_ws
colcon build
source /opt/ros/humble/setup.bash
source install/setup.bash
ros2 run robot_interface robot_control
'''

This will start the GUI to control the robot.

---

## GUI Options

### Option A – `tkinter` button GUI

This interface shows a dark window with five buttons:

-  move_forward
-  turn_left
-  turn_right
-  move_backward
-  stop

Each button sends a 'Twist' message to the '/cmd_vel' topic.


---

## Files Overview

- 'robot_control.py' – GUI using 'tkinter' for directional control.
- 'gui_control.py' – GUI using `pygame` and mouse clicks.
- 'CMakeLists.txt', 'package.xml' – Standard ROS 2 Python package files.

---

## Authors
- Gloria Leon Lago
- Maria Leal Suarez
