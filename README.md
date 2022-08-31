# ROS-based-A-Four-wheel-Robot-Mapping-and-Navigation-using-RTAB-MAP-SLAM
The presented work describes an implementation of A Four-wheels Robot Mapping and
Navigation in the laboratory using RTABMAP SLAM based on the ROS platform. It
explains in detail how to configure the packages required for the experiment and how to
configure the files required for mapping and navigation and a discussion is drawn relating
practical aspects of the algorithms with the inner workings and main parameters of the
respective ROS implementation

# Installation

**ROS Melodic:**  Follow the installation guide in: http://wiki.ros.org/melodic/Installation/Ubuntu

**realsense2_camera:** Follow the installation guide in: https://github.com/intel-ros/realsense

**imu_filter_madgwick:** ```sudo apt-get install ros-kinetic-imu-filter-madgwick```

**rtabmap_ros:** ```sudo apt-get install ros-kinetic-rtabmap-ros```

**robot_localization:** ```sudo apt-get install ros-kinetic-robot-localization```

**depthimage to laserscan** ```sudo apt-get install ros-melodic-depthimage-to-laserscan```

# Running
Hold the camera steady with a clear view and run the following command to turn on the camrea and rtabmap:

```roslaunch realsense2_camera opensource_tracking_a.launch args:="--delete_db_on_start"```

Wait a little for the system to fix itself.

Then open and personalize Rviz ( A graphical tool that comes with ROS ) to monitor robot status
