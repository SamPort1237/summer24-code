import rclpy as rp
from rclpy.node import Node
from geometry_msgs.msg import Twist
import sys

msg = Twist()

def moveforward():
    print("Moving forward")
    msg.linear.x = 0.05   #range +0.22 , -0.22
    msg.linear.y = 0
    msg.linear.z = 0

    msg.angular.x = 0
    msg.angular.y = 0
    msg.angular.z = 0
    return msg

def stopmoving():
    print("Stop moving")
    msg.linear.x = 0
    msg.linear.y = 0
    msg.linear.z = 0

    msg.angular.x = 0
    msg.angular.y = 0
    msg.angular.z = 0
    return msg

def turnleft():
    print("Turn left")
    msg.linear.x = 0
    msg.linear.y = 0
    msg.linear.z = 0

    msg.angular.x = 0
    msg.angular.y = 0
    msg.angular.z = -0.05  #range +0.22 r, -0.22 l
    return msg

def turnright():
    print("Turn right")
    msg.linear.x = 0
    msg.linear.y = 0
    msg.linear.z = 0

    msg.angular.x = 0
    msg.angular.y = 0
    msg.angular.z = 0.05  # range +0.22 r, -0.22 l
    return msg

def reverse():
    print("Reverse")
    msg.linear.x = -0.05  # range +0.22 , -0.22
    msg.linear.y = 0
    msg.linear.z = 0

    msg.angular.x = 0
    msg.angular.y = 0
    msg.angular.z = 0
    return msg

def spin():
    print("Spin")
    msg.linear.x = 0
    msg.linear.y = 0
    msg.linear.z = 0

    msg.angular.x = 0
    msg.angular.y = 0
    msg.angular.z = 0.05
    return msg

def fullstop():
    print("Full Stop")
    #rock and roll symbol, stops code with exit()
    rp.shutdown()
    return msg








