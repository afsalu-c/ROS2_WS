#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

def main(args=None):
    rclpy.init(args=args)#start ros2 communications
    node = Node()
    node.get_logger().info("HELLO ROS2")
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()
