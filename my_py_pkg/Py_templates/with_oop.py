#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):#Inherit "Node" class 

    def __init__(self):
        super().__init__("py_test")
        self.get_logger().info("HELLO ROS2")

def main(args=None):
    rclpy.init(args=args)#start ros2 communications
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()
