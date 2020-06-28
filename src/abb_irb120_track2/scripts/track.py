#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 接收camera_fix发布的速度和位置

import rospy
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import Bool
import abb
import math


doGripperOpen = 1
doGripperClose = 2
R = abb.Robot('192.168.125.1') # connecting to robot
R.set_cartesian([[346, 0, 300], [0.707, 0.0, 0.707, 0.0]])
R.set_dio(doGripperClose, 0)
R.set_dio(doGripperOpen, 1)
R.set_speed([100,100,100,100])

Motion = False
Count = 0

speed = [0,0,0,0,0,0]
color = 0
xc = 0
yc = 0



def camera_trackCallback(msg):
    global speed

	# 接收消息  
    # rospy.loginfo(msg.data)
    speed[0] = msg.data[0]
    speed[1] = msg.data[1]

    
def get_angle(theta2,high):
    l1=270
    l2=310  # math.sqrt(70^2+302^2)
    high=high-290
    alpha2=90-theta2
    alpha5=180-math.asin((l1*math.sin(alpha2*math.pi/180)-high)/l2)*180/math.pi
    alpha3=alpha5-alpha2

    theta3=180-77-alpha3
    theta5=-(180+13-alpha5)
    return theta3,theta5


def robot_publisher():
    global xc
    global yc

    # ROS节点初始化
    rospy.init_node('robot_publisher', anonymous=True)
    # 创建一个Publisher，发布名为/camera_fix_info的topic，消息类型为std_msgs::Float32MultiArray，队列长度1
    # robot_motion_info_pub = rospy.Publisher('/robot_motion_info', Bool, queue_size=1)
    rospy.Subscriber("/camera_track_info", Float32MultiArray, camera_trackCallback)
    #设置循环的频率
    rate = rospy.Rate(10) 
    # 发布消息
    # robot_motion_info_pub.publish(robot_motion_info)

    while not rospy.is_shutdown():

        # POSITION,POSE = R.get_cartesian()
        # j1,j2,j3,j4,j5,j6 = R.get_joints()
        # j1 -= speed[0] * 0.1
        # j2 -= speed[1] * 0.1

        # j3,j5 = get_angle(j2,POSITION[2])

        # R.set_joints_t([j1,j2,j3,j4,j5,j6],0.1)


        # position
        POSITION,POSE = R.get_cartesian()
        POSITION[1] -= speed[0] * 0.01
        POSITION[0] -= speed[1] * 0.01

        R.set_cartesian_t([POSITION,POSE],0.01)

        # 按照循环频率延时
        rate.sleep()



if __name__ == '__main__':
    try:
        robot_publisher()
    except rospy.ROSInterruptException:
        pass
    


