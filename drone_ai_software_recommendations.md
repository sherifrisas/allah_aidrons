# Drone AI Software Stack: Best Recommended Versions

## 1. Operating System
- **Ubuntu 20.04 LTS (Focal Fossa)**
  - Most compatible with ROS Noetic, Jetson, and RPi.
  - Long-term support and widely used in robotics.

## 2. ROS (Robot Operating System)
- **ROS Noetic Ninjemys**
  - Latest LTS version for Ubuntu 20.04.
  - Most supported for robotics, drones, and AI integration.
  - [ROS Noetic Installation Guide](http://wiki.ros.org/noetic/Installation/Ubuntu)

## 3. AI Frameworks
- **TensorFlow:**  
  - **Version:** 2.9.x (for Jetson, use NVIDIA’s prebuilt wheels for best GPU support)
  - [TensorFlow for Jetson](https://docs.nvidia.com/deeplearning/frameworks/install-tf-jetson-platform/index.html)
- **PyTorch:**  
  - **Version:** 1.10.x or 1.11.x (for Jetson, use NVIDIA’s prebuilt wheels)
  - [PyTorch for Jetson](https://forums.developer.nvidia.com/t/pytorch-for-jetson-version-1-10-now-available/72048)
- **OpenCV:**  
  - **Version:** 4.5.x or higher (install via apt or build from source for CUDA support on Jetson)

## 4. Drone SDK
- **MAVSDK:**  
  - **Version:** Latest stable (Python: `pip install mavsdk`)
- **DroneKit:**  
  - **Version:** 2.9.2 (Python: `pip install dronekit`)
- **MAVROS (for PX4/ArduPilot):**  
  - **Version:** ros-noetic-mavros (install via apt for Noetic)

## 5. Other Key Packages
- **RTAB-Map (for SLAM):**  
  - **Version:** ros-noetic-rtabmap-ros
- **move_base (for navigation):**  
  - **Version:** ros-noetic-move-base
- **cv_bridge (for ROS-OpenCV):**  
  - **Version:** ros-noetic-cv-bridge

## 6. Simulation (Optional but Recommended)
- **Gazebo:**  
  - **Version:** 11.x (comes with ROS Noetic)
- **AirSim:**  
  - **Version:** Latest stable (from Microsoft GitHub)

## 7. General Recommendations
- Always use LTS (Long Term Support) versions for OS and ROS.
- For Jetson, always use NVIDIA’s optimized wheels for TensorFlow and PyTorch.
- For Raspberry Pi, use lightweight models and consider OpenCV’s optimizations for ARM.

---

### Summary Table

| Component      | Recommended Version / Distro         |
|----------------|-------------------------------------|
| OS             | Ubuntu 20.04 LTS                    |
| ROS            | Noetic Ninjemys                     |
| TensorFlow     | 2.9.x (NVIDIA Jetson wheel)         |
| PyTorch        | 1.10.x (NVIDIA Jetson wheel)        |
| OpenCV         | 4.5.x+                              |
| MAVSDK         | Latest stable (pip)                 |
| DroneKit       | 2.9.2 (pip)                         |
| MAVROS         | ros-noetic-mavros                   |
| RTAB-Map       | ros-noetic-rtabmap-ros              |
| move_base      | ros-noetic-move-base                |
| Gazebo         | 11.x                                |
| AirSim         | Latest stable                       |

---

**If you want a ready-to-use installation script for these versions, or a sample requirements file, just let me know!** 