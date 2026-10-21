# Autonomous Drone – DJI Tello

## Overview
This project implements an autonomous person-following system for the DJI Tello Drone using Python, OpenCV, and the `djitellopy` library.

The drone detects and tracks a person in real time and uses PID (Proportional-Integral-Derivative) controllers to dynamically adjust its movements.

## Features
- Real-time person detection and tracking
- Autonomous flight control using PID controllers
- Movement adjustments across three axes:
  - X-axis: Left/Right rotation (Yaw)
  - Y-axis: Up/Down movement
  - Z-axis: Forward/Backward movement
- Automatic adjustments based on the tracked person's position

## Important Notes
**PID calibration is essential for stable flight performance.**

Before running the project, make sure to review and adjust the PID parameters in `main.py`.

The optimal PID values may vary significantly depending on your environment, lighting conditions, tracking performance, and other factors.

Always perform initial tests in a safe environment.

Use Python version 3.11 and mediapipe 0.10.21

## Technologies Used
- Python
- OpenCV
- djitellopy
- PID Control

## Disclaimer
This project is intended for educational and experimental purposes. Always supervise the drone during operation and follow local drone regulations.


## Installation
pip install -r requirements.txt

## start
1. Connect to the Tello Drone with Wifi
2. python main.py
3. If you want to land the Drone, press the "q" key in the Video-Window
---

Thanks for checking out this project! Contributions, suggestions, and improvements are always welcome.
