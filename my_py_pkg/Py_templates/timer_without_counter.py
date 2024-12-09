#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):#Inherit "Node" class 

    def __init__(self):
        super().__init__("py_test")
        self.get_logger().info("HELLO ROS2")
        self.create_timer(0.5,self.timer_callback) #will print "HI ARE YOU FINE" in every 0.5 seconds
    
    def timer_callback(self):
        self.get_logger().info("HI ARE YOU FINE")

def main(args=None):
    rclpy.init(args=args)#start ros2 communications
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()
