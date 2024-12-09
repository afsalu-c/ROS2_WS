#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):
    def __init__(self):
        super().__init__("py_test")
        self.counter = 0
        self.get_logger().info("HELLO ROS2")
        self.create_timer(.5,self.timer_callback)

    def timer_callback(self):
        self.counter += 1
        self.get_logger().info("hello" + str(self.counter))
        
def main(args=None):
    rclpy.init(args=args) #initialize/start ros2 communicaion
    node = MyNode()
    rclpy.spin(node) #kept alive
    rclpy.shutdown()#last line of the program to stop the node

if __name__ == "__main__":
    main()