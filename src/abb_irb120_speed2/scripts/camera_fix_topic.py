#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 发布速度和位置

import rospy
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import Bool
import cv2
import numpy as np
import camera as ca
# import time

Motion = False

def robotCallback(msg):
	# 接收消息  
    # rospy.loginfo(msg.data)
    global Motion
    Motion = msg.data



def camera_fix_publisher():
    # ROS节点初始化
    rospy.init_node('camera_fix_publisher', anonymous=True)
    cap = cv2.VideoCapture(0)
	# 创建一个Publisher，发布名为/camera_fix_info的topic，消息类型为std_msgs::Float32MultiArray，队列长度1
    camera_fix_info_pub = rospy.Publisher('/camera_fix_info', Float32MultiArray, queue_size=1)
    # camera_rqt_info_pub = rospy.Publisher('/camera_rqt_info', Float32MultiArray, queue_size=1)
    rospy.Subscriber("/robot_motion_info", Bool, robotCallback)
	#设置循环的频率
    rate = rospy.Rate(5) 

    speed = 0
    color = 0
    dx = 0.406  # image space to robot space   60.5/149
    xc = 0
    last_xc = 0
    yc = 0
    num = 0
    temp_speed=[0,0,0,0]

    while not rospy.is_shutdown() & cap.isOpened():

        color,xc,yc = ca.Detect(cap)
        # print(xc, yc, speed)
        if (color > 0) & (xc > 180) & (num < 5):
            if last_xc>180  & num <= 3:
                if num==0:
                    temp_speed[num] = ((xc - last_xc) * dx / 0.2)
                else:
                    temp_speed[num] = (temp_speed[num-1] + ((xc - last_xc) * dx / 0.2)) / 2
                print(num, last_xc, xc, yc, temp_speed[num])
                num = num + 1
            if last_xc > xc : # 如果物体已经检测过，就清零
                speed = 0
                color = 0
                xc = 0
                last_xc = 0
                yc = 0
                num = 0

            last_xc = xc
            if num==4:
                num += 1
                speed = (temp_speed[1]+temp_speed[2]+temp_speed[3])/3
                # for v in temp_speed:
                #     speed = (speed + v)/2
                global Motion
                if (speed>0.01) & (xc>0) & (not Motion):
                    array = [xc, yc, speed, color]
                    camera_fix_info = Float32MultiArray(data=array)
                    rospy.loginfo(camera_fix_info.data)
                    # 发布消息
                    camera_fix_info_pub.publish(camera_fix_info)   
        # array = [xc, yc, speed, color]
        # camera_rqt_info = Float32MultiArray(data=array)
        # # 发布消息
        # camera_rqt_info_pub.publish(camera_rqt_info)  

        if (num==5) & (xc==0):
            speed = 0
            color = 0
            xc = 0
            last_xc = 0
            yc = 0
            num = 0
        
		# 按照循环频率延时
        rate.sleep()
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    try:
        camera_fix_publisher()
    except rospy.ROSInterruptException:
        pass



