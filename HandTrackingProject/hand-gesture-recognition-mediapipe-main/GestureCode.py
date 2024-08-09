import rclpy
from rclpy.node import Node
import cv2 as cv

import StopTest
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
import RobotControls as RC
#import importlib.util
from cv_bridge import CvBridge, CvBridgeError

class GestureNode(Node):
    def __init__(self):
        super().__init__('gesture_node')
        self.subscriber = self.create_subscription(Image, '/image_raw', self.image_callback)
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(0.5, self.timer_callback)
        self.cmd = Twist()
        self.step = 0
        self.cv_bridge = CvBridge()
        self.img = 0
    def image_callback(self, data):
        self.img = self.cv_bridge.imgmsg_to_cv2(data, desired_encoding='bgr8')
        # Example: Display the received image
        cv.imshow('Received Image', self.img)
        cv.waitKey(1)  # You can adjust the wait key time as needed
    def timer_callback(self):
        self.cmd = StopTest.ros_stop_test(self.img)
        self.publisher.publish(self.cmd)

def main(args=None):
    rclpy.init(args=args)
    node = GestureNode()

    try:
        rclpy.spin(node)
    except Exception as e:
        node.get_logger().error(f"Error calling StopTest.main(): {str(e)}")

    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()