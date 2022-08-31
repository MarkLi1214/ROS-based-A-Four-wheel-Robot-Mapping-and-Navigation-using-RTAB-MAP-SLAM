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
## Mapping

Hold the camera steady with a clear view and run the following command to turn on the camrea and rtabmap:

```roslaunch realsense2_camera opensource_tracking_a.launch args:="--delete_db_on_start"```

Wait a little for the system to fix itself.

Then open and personalize Rviz ( A graphical tool that comes with ROS ) for mapping and monitoring robot status

From the Displays Panel:

TF -> Frames, and then leave out as marked only map and camera_link. 

PointCloud2: Create 3d map

Map: 2D grid map

You may want to watch the on-line video as well:
From the Displays panel:
Image->Image Topic: rewrite to /camera/color/image_raw
![](https://github.com/MarkLi1214/ROS-based-A-Four-wheel-Robot-Mapping-and-Navigation-using-RTAB-MAP-SLAM/blob/main/image/mapping.gif?raw=true)
![](https://github.com/MarkLi1214/ROS-based-A-Four-wheel-Robot-Mapping-and-Navigation-using-RTAB-MAP-SLAM/blob/main/image/resule.png)
![](https://github.com/MarkLi1214/ROS-based-A-Four-wheel-Robot-Mapping-and-Navigation-using-RTAB-MAP-SLAM/blob/main/image/os_tracking_display_panel.jpg)



you can create a 2D map using:

**Map server:** ```

```rosrun map_server map_saver map:=/rtabmap/proj_map –f mapname```

and a resulting map would look something like that:

![](https://github.com/MarkLi1214/ROS-based-A-Four-wheel-Robot-Mapping-and-Navigation-using-RTAB-MAP-SLAM/blob/main/image/map_demo_final.png)

You can save the point cloud using:

```rosrun pcl_ros pointcloud_to_pcd input:=/rtabmap/cloud_map```

You can install 'pcl-tools' to watch the saved point cloud later using:

```pcl_viewer 1543906154413083.pcd```

[Install using: ```sudo apt-get install pcl-tools```]

## Navigation

The main package for robot navigation is Move_base which is used to carry out the path planning to make the mobile robot reach the target point according
to the map and the target point information.The package maintains two cost maps for local and global planners: Local and Global costmaps, Local and Global planners.


![](https://github.com/MarkLi1214/ROS-based-A-Four-wheel-Robot-Mapping-and-Navigation-using-RTAB-MAP-SLAM/blob/main/image/move_base.png)

After configuring costamaps and planner files, we can see the information about the linear speed and angular of robot by using the command:


```rostopic echo \cmd_vel```

![](https://github.com/MarkLi1214/ROS-based-A-Four-wheel-Robot-Mapping-and-Navigation-using-RTAB-MAP-SLAM/blob/main/image/cmd_vel.png)

The values of linear and angular will change as the 2D Nav Goal changes and will change in real-time as the robot moves
 
Subscribe topic \cme_vel to get the information and calculate the speed of each montor by using the kinematic model.

The result of navigation in RVIZ would look something like that:

![](https://github.com/MarkLi1214/ROS-based-A-Four-wheel-Robot-Mapping-and-Navigation-using-RTAB-MAP-SLAM/blob/main/image/navigation.gif?raw=true)

![](https://github.com/MarkLi1214/ROS-based-A-Four-wheel-Robot-Mapping-and-Navigation-using-RTAB-MAP-SLAM/blob/main/image/navigation.png)

