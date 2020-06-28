#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 发布速度和位置

import rospy
from std_msgs.msg import Float32MultiArray
# from std_msgs.msg import Bool
import cv2
import numpy as np
import camera_track as cat
# import time

# Motion = False

# def robotCallback(msg):
# 	# 接收消息  
#     # rospy.loginfo(msg.data)
#     global Motion
#     Motion = msg.data



def camera_track_publisher():
    # ROS节点初始化
    rospy.init_node('camera_track_publisher', anonymous=True)
    cap = cv2.VideoCapture(1)
	# 创建一个Publisher，发布名为/camera_track_info的topic，消息类型为std_msgs::Float32MultiArray，队列长度1
    camera_track_info_pub = rospy.Publisher('/camera_track_info', Float32MultiArray, queue_size=1)
    # camera_rqt_info_pub = rospy.Publisher('/camera_rqt_info', Float32MultiArray, queue_size=1)
    # rospy.Subscriber("/robot_motion_info", Bool, robotCallback)
	#设置循环的频率
    rate = rospy.Rate(10) 

    xc = 0
    yc = 0

    # kp=0.005
    # kd=0.00

    # xy position 
    kp=1
    kd=3

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
            error_last_x = error_now_x
            error_last_y = error_now_y

            array = [v1, v2]
            camera_track_info = Float32MultiArray(data=array)
            rospy.loginfo(camera_track_info.data)
            # 发布消息
            camera_track_info_pub.publish(camera_track_info)   

		# 按照循环频率延时
        rate.sleep()
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    try:
        camera_track_publisher()
    except rospy.ROSInterruptException:
        pass

