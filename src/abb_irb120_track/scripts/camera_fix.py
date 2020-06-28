#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 发布速度和位置

import rospy
from std_msgs.msg import Float32MultiArray
from pos_speed.srv import pos_speed, pos_speedResponse
import cv2
import numpy as np
import camera as ca
import time

speed = 0
color = 0
dx = 0.406  # image space to robot space   60.5/149
xc = 0
yc = 0

def camera_fixCallback(req):
	# 显示请求数据
	# 反馈数据
    return pos_speedResponse(xc,yc,color,speed)


def camera_fix_publisher():
    # ROS节点初始化
    rospy.init_node('camera_fix_publisher', anonymous=True)
    cap = cv2.VideoCapture(0)
	# 创建一个Publisher，发布名为/camera_fix_info的topic，消息类型为std_msgs::Float32MultiArray，队列长度1
    camera_fix_info_pub = rospy.Publisher('/camera_fix_info', Float32MultiArray, queue_size=1)
    camera_fix_server = rospy.Service('/camera_fix_service', Float32MultiArray, camera_fixCallback)

	#设置循环的频率
    rate = rospy.Rate(10) 

    while not rospy.is_shutdown() & cap.isOpened():

        color,last_xc,yc = ca.Detect(cap)

        if (color > 0) & (last_xc > 160):
            time.sleep(0.2)
            color, xc, yc = ca.Detect(cap)
            speed = ((xc - last_xc) * dx / 0.2)
            last_xc = xc
            print(xc, yc, speed)
            for i in range(3):
                time.sleep(0.2)
                color, xc, yc = ca.Detect(cap)
                speed = (speed + ((xc - last_xc) * dx / 0.2)) / 2
                last_xc = xc
                print(xc, yc, speed)
                if (speed<0) | (xc==0):
                    break
            array = [xc, yc, speed, color]
            camera_fix_info = Float32MultiArray(data=array)
            rospy.loginfo(camera_fix_info)
            # 发布消息
            camera_fix_info_pub.publish(camera_fix_info)
        else:
            speed = 0
            color = 0
            xc = 0
            yc = 0
        
		# 按照循环频率延时
        rate.sleep()
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    try:
        camera_fix_publisher()
    except rospy.ROSInterruptException:
        pass



