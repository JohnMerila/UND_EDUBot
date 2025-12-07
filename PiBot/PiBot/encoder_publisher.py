import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
import math

import smbus2
import time


# Define I2C address and bus
AS5600_ADDR = 0x36
ANGLE_REG = 0x0E




def read_angle_L():
    bus = smbus2.SMBus(1)
    # Read two bytes from the angle register
    raw_data = bus.read_i2c_block_data(AS5600_ADDR, ANGLE_REG, 2)
    angle = (raw_data[0] << 8) | raw_data[1]  # Combine MSB and LSB
    angle = angle & 0x0FFF  # Mask to 12 bits
    return (angle / 4096.0) * 360.0  # Convert to degrees

def read_angle_R():
    bus = smbus2.SMBus(4)
    # Read two bytes from the angle register
    raw_data = bus.read_i2c_block_data(AS5600_ADDR, ANGLE_REG, 2)
    angle = (raw_data[0] << 8) | raw_data[1]  # Combine MSB and LSB
    angle = angle & 0x0FFF  # Mask to 12 bits
    return (angle / 4096.0) * 360.0  # Convert to degrees


class JointStatePublisher(Node):
    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(JointState, 'joint_states', 10)
        timer_period = 0.05  # seconds
        self.timer = self.create_timer(timer_period, self.encoder_callback)
        self.joint_names = ['left', 'right']
        self.ang_L_prev = read_angle_L()
        self.time_L_prev = time.time()
        self.ang_R_prev = read_angle_R()
        self.time_R_prev = time.time()
        
        
        
        self.get_logger().info('Joint State Publisher Node has been started.')

    def encoder_callback(self):
        try:
            msg = JointState()

            # Fill joint names
            msg.name = self.joint_names
            ang_L = read_angle_L()
            
            vel_L = (ang_L - self.ang_L_prev) / (time.time() - self.time_L_prev)
            self.time_L_prev = time.time()
            self.ang_L_prev = ang_L
            ang_R = read_angle_R()
            
            vel_R = (ang_R - self.ang_R_prev) / (time.time() - self.time_R_prev)
            
            self.time_R_prev = time.time()
            self.ang_R_prev = ang_R
            msg.position = [ang_L,ang_R]
            msg.velocity = [vel_L,vel_R]
            
            self.publisher_.publish(msg)
            # msg = String()
            # msg.data = 'Hello World: %d' % self.i
            # self.publisher_.publish(msg)
            # self.get_logger().info('Publishing: "%s"' % msg.data)
            # self.i += 1
        except OSError as e:
            self.get_logger().warn(f"I2C read failed: {e}")
        except Exception as e:
            self.get_logger().error(f"Unexpected error in encoder_callback: {e}")


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = JointStatePublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()



# try:
#     while True:
#         angleL = read_angle_L()
#         angleR = read_angle_R()
#         print(f"Angle: {angleL:.2f} degrees")
#         print(f"Angle: {angleR:.2f} degrees")
#         time.sleep(0.05)
# except KeyboardInterrupt:
#     print("Exiting...")