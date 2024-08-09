import rclpy
from rclpy.node import Node
import cv2 as cv
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image

import StopTest
import RobotControls as RC

def main ():

    vel = Twist()

    ST = StopTest(vel)

    rclpy.init_node("Gesture_Control")
    rclpy.Subscriber("/img", Image, ST.main())
    pub = rclpy.Publisher("/cmd_vel", Twist, queue_size=10)
    rate = rclpy.Rate(10)

if __name__ == '__main__':
    main()

