#!/usr/bin/env python
import rospy

# to get commandline arguments
import sys

# Because of transformations
import tf

import tf2_ros
import geometry_msgs.msg

if __name__ == '__main__':
    rospy.init_node('kinect_static_broadcaster')
    broadcaster = tf2_ros.StaticTransformBroadcaster()
    static_transformStamped = geometry_msgs.msg.TransformStamped()

    static_transformStamped.header.stamp = rospy.Time.now()
    static_transformStamped.header.frame_id = "base_link"
    static_transformStamped.child_frame_id = "kinect2_link"

    static_transformStamped.transform.translation.x = 0.35
    static_transformStamped.transform.translation.y = 0.0
    static_transformStamped.transform.translation.z = -0.15

    quat = tf.transformations.quaternion_from_euler(0.0, 0.0, 0.0, 'rzyx')
    static_transformStamped.transform.rotation.x = quat[0]
    static_transformStamped.transform.rotation.y = quat[1]
    static_transformStamped.transform.rotation.z = quat[2]
    static_transformStamped.transform.rotation.w = quat[3]

    broadcaster.sendTransform(static_transformStamped)
    rospy.spin()
