To get RVIZ working
locally: xhost +local:docker

build work space
colcon build --symlink-install
*when first building the workspace it will take some time to build the lidar package
*it will fail on the first build, re run command and it will work

To source the local ROS workspace 
source install/setup.bash

Start up motor control and wheel encoders
ros2 launch PiBot PiBot_launch.py 

Start up lidar with visualization
ros2 launch sllidar_ros2 view_sllidar_a1_launch.py

For teleop control
ros2 run teleop_twist_keyboard teleop_twist_keyboard 


Topics for robot:

/

Notes:

If you are adding additional packages via sudo apt install . . . 

Put at the end of Dockerfile with run preceding
* add -y if it requires yes when installing 

