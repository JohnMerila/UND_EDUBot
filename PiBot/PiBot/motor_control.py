import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
from gpiozero import Motor
from time import sleep

class MinimalSubscriber(Node):
	
	def __init__(self):
		super().__init__('node')
		self.subscription = self.create_subscription(
			Twist,
			'/cmd_vel',
			self.listener_callback,
			10)
		self.subscription  # prevent unused variable warning
		self.m1vel = None
		self.m2vel = None
	def listener_callback(self, msg):
		
		self.get_logger().info('I heard: "%s"' % msg.linear)
		linearvel = msg.linear.x
		angularvel = msg.angular.z
  
		if linearvel != 0 and angularvel != 0:
      
			m1vel_temp = linearvel*.8 + angularvel*.25
			m2vel_temp = linearvel*.8 - angularvel*.25
			if m1vel_temp > 1:
				m1vel_temp = 1
			elif m1vel_temp < -1:
				m1vel_temp = -1
			if m2vel_temp > 1:
				m2vel_temp = 1
			elif m2vel_temp < -1:
				m2vel_temp = -1
    
		else:
		
			m1vel_temp = linearvel*.8 + angularvel*.25
			m2vel_temp = linearvel*.8 - angularvel*.25
			if m1vel_temp > 1:
				m1vel_temp = 1
			elif m1vel_temp < -1:
				m1vel_temp = -1
			if m2vel_temp > 1:
				m2vel_temp = 1
			elif m2vel_temp < -1:
				m2vel_temp = -1
		self.get_logger().info('I heard: "%s"' % m1vel_temp)
		self.get_logger().info('I heard: "%s"' % m2vel_temp)
	
		self.m1vel = m1vel_temp*.8
		self.m2vel = m2vel_temp*.8
		
		


def main(args=None):
	rclpy.init(args=args)
	motor1 = Motor(25,18)
	motor2 = Motor(14,15)

	
	node = MinimalSubscriber()

	try:
		while rclpy.ok():
			rclpy.spin_once(node, timeout_sec=0.1)
			if node.m1vel and node.m2vel:
				# Use the stored value here

				print(node.m1vel)
				print(node.m2vel)
				if node.m1vel > 0:
					motor1.forward(node.m1vel)
				else:
					motor1.backward(abs(node.m1vel))
				if node.m2vel > 0:
					motor2.forward(node.m2vel)
				else:
					
					motor2.backward(abs(node.m2vel))
			else:
				motor1.forward(0)
				motor2.forward(0)
				#print(f"[Main loop] linear.x = {node.m1vel})
	except KeyboardInterrupt:
		motor1.forward(0)
		motor2.forward(0)
		pass
	node.destroy_node()
	rclpy.shutdown()


if __name__ == '__main__':
	main()