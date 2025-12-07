from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch.actions import IncludeLaunchDescription

def generate_launch_description():
    return LaunchDescription([
        # IncludeLaunchDescription(
        #     PathJoinSubstitution([
        #         FindPackageShare('sllidar_ros2'),
        #         'launch',
        #         'sllidar_a1_launch.py'
        #     ]),
        #     launch_arguments={}.items()),
        Node(
            package='PiBot',
            executable='encoder_data',
            name='encoder_data',
            #output='screen'
        ),
        Node(
            package='PiBot',
            executable='motor_control',
            name='motor_control',
            #output='screen'
        )
    ])
