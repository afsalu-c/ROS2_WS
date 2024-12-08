#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):
    def __init__(self):
        super().__init__("py_test")
        self.get_logger().info("Hello ROS2")
        
def main(args=None):
    rclpy.init(args=args) #initialize/start ros2 communicaion
    node = MyNode()
    rclpy.spin(node) #kept alive
    rclpy.shutdown()#last line of the program  

if __name__ == "__main__":
    main()
