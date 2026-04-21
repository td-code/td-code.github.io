#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import numpy as np

from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
from visualization_msgs.msg import Marker
from geometry_msgs.msg import TwistStamped

class HitMe(Node):
    """
    A class to subscribe to a lidar scan, find and publish the closest point to an obstacle and drive our Turtlebot towards the closest point.
    """

    def __init__(self):
        super().__init__('hit_me')
        self.subscription = self.create_subscription(
            LaserScan,
            'scan',
            self.lidar_callback,
            1)
        self.subscription  # prevent unused variable warning

        self.closestPtMarkerPublisher = self.create_publisher(Marker, 'closest_pt_marker', 1)
        self.cmdVelPublisher = self.create_publisher(TwistStamped, 'cmd_vel', 1)

        self.get_logger().info(self.get_name() + " initialized. Starting main loop.")

    def lidar_callback(self, scanData):
        """
        The lidar callback function.
        scanData is the lidar scan data, cf. https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html
        """

        # TODO 1: Add code here for finding the closest point and setting the output message


        # TODO 2: Add code below to output the closest point as a marker in rviz
        m = Marker()
        m.header = scanData.header
        m.type = m.CUBE
        # set positions here
        m.pose.position.x = 0
        m.pose.position.y = 0
        m.pose.position.z = 0.
        m.pose.orientation.x = 0.
        m.pose.orientation.x = 0.
        m.pose.orientation.z = 0.
        m.pose.orientation.w = 1.
        m.color.r = 1.
        m.color.g = 0.
        m.color.b = 0.
        m.color.a = 1.
        m.scale.x = 0.1
        m.scale.y = 0.1
        m.scale.z = 0.1

        self.closestPtMarkerPublisher.publish(m)

        # TODO 3: Send steering command
        ts = TwistStamped()


def main(args=None):
    rclpy.init(args=args)

    hit_me = HitMe()
    

    rclpy.spin(hit_me)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    hit_me.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

