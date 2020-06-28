#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 发布速度和位置

import rospy
from std_msgs.msg import Float32MultiArray
# from std_msgs.msg import Bool
import cv2
import numpy as np
import camera_track as cat
import abb
import math

# doGripperOpen = 1
# doGripperClose = 2
# R = abb.Robot('192.168.125.1') # connecting to robot
# R.set_cartesian([[346, 0, 300], [0.707, 0.0, 0.707, 0.0]])
# R.set_dio(doGripperClose, 0)
# R.set_dio(doGripperOpen, 1)
# R.set_speed([100,100,100,100])

Motion = False
Count = 0

speed = [0,0,0,0,0,0]
color = 0
xc = 0
yc = 0

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


def camera_track_publisher():
    # ROS节点初始化
    rospy.init_node('camera_track_publisher', anonymous=True)
    cap = cv2.VideoCapture(1)
	# 创建一个Publisher，发布名为/camera_track_info的topic，消息类型为std_msgs::Float32MultiArray，队列长度1
    camera_track_info_pub = rospy.Publisher('/camera_track_info', Float32MultiArray, queue_size=1)
    # camera_rqt_info_pub = rospy.Publisher('/camera_rqt_info', Float32MultiArray, queue_size=1)
    # rospy.Subscriber("/robot_motion_info", Bool, robotCallback)
	#设置循环的频率
    rate = rospy.Rate(100) 

    xc = 0
    yc = 0

    # kp=0.005
    # kd=0.00

    # xy position 
    kp=2
    kd=0

    error_last_x = 0
    error_now_x = 0
    error_last_y = 0
    error_now_y = 0

    while not rospy.is_shutdown() & cap.isOpened():

        xc,yc = cat.track(cap)
        if(xc!=0)&(yc!=0):
            error_now_x = xc-320
            error_now_y = yc-240

            v1 = kp*error_now_x + kd*(error_now_x - error_last_x)
            v2 = kp*error_now_y + kd*(error_now_y - error_last_y)

            array = [v1, v2]
            camera_track_info = Float32MultiArray(data=array)
            rospy.loginfo(camera_track_info.data)
            # 发布消息
            camera_track_info_pub.publish(camera_track_info)   

            # # position
            # POSITION,POSE = R.get_cartesian()
            # POSITION[1] -= kp*error_now_x + kd*(error_now_x - error_last_x)
            # POSITION[0] -= kp*error_now_y + kd*(error_now_y - error_last_y)

            # R.set_cartesian_t([POSITION,POSE],0.01)

            # POSITION,POSE = R.get_cartesian()
            # j1,j2,j3,j4,j5,j6 = R.get_joints()
            # j1 -= kp*error_now_x + kd*(error_now_x - error_last_x)
            # j2 -= kp*error_now_y + kd*(error_now_y - error_last_y)

            # j3,j5 = get_angle(j2,POSITION[2])

            # R.set_joints_t([j1,j2,j3,j4,j5,j6],0.1)


            error_last_x = error_now_x
            error_last_y = error_now_y

            # # position
            # POSITION,POSE = R.get_cartesian()
            # POSITION[1] -= speed[0] * 0.01
            # POSITION[0] -= speed[1] * 0.01

            # R.set_cartesian_t([POSITION,POSE],0.01)


            # POSITION,POSE = R.get_cartesian()
            # j1,j2,j3,j4,j5,j6 = R.get_joints()
            # j1 -= speed[0] * 0.1
            # j2 -= speed[1] * 0.1

            # j3,j5 = get_angle(j2,POSITION[2])

            # R.set_joints_t([j1,j2,j3,j4,j5,j6],0.1)
        else:
            error_last_x = 0
            error_now_x = 0
            error_last_y = 0
            error_now_y = 0



		# 按照循环频率延时
        rate.sleep()
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    try:
        camera_track_publisher()
    except rospy.ROSInterruptException:
        pass

