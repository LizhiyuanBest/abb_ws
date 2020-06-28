#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 接收camera_fix发布的速度和位置

import rospy
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import Bool
import robot as rb

Motion = False
Count = 0
Color = {0:"None",1:"Yellow",2:"Red",3:"Green"}

speed = 0
color = 0
xc = 0
yc = 0

def camera_fixCallback(msg):

	# 接收消息  
    rospy.loginfo(msg.data)
    global xc
    xc = msg.data[0]
    global yc
    yc = msg.data[1]
    global speed
    speed = msg.data[2]
    global color
    color = msg.data[3]

    if (speed<0.1) | (xc==0):
        return 
    global Motion
    if not Motion:
        Motion = True
        global Count
        Count = Count +1
        print(Count,Color[color])  



def robot_publisher():
    global Motion
    global Count
    global speed
    global color
    global xc
    global yc

    # ROS节点初始化
    rospy.init_node('robot_publisher', anonymous=True)
	# 创建一个Publisher，发布名为/camera_fix_info的topic，消息类型为std_msgs::Float32MultiArray，队列长度1
    robot_motion_info_pub = rospy.Publisher('/robot_motion_info', Bool, queue_size=1)
    rospy.Subscriber("/camera_fix_info", Float32MultiArray, camera_fixCallback)
	#设置循环的频率
    # rate = rospy.Rate(10) 
    # global Motion
    Motion = False
    robot_motion_info = Bool(data=Motion)
    rospy.loginfo(robot_motion_info)
    # 发布消息
    robot_motion_info_pub.publish(robot_motion_info)

    while not rospy.is_shutdown():
        # global Motion
        if Motion:
            robot_motion_info = Bool(data=Motion)
            # rospy.loginfo(robot_motion_info)
            # 发布消息
            robot_motion_info_pub.publish(robot_motion_info)
                  
            rb.grip(xc,yc,speed)
            rb.place(color)
            Motion = False
            robot_motion_info = Bool(data=Motion)
            # rospy.loginfo(robot_motion_info)
            # 发布消息
            robot_motion_info_pub.publish(robot_motion_info)
        # else:
        #     # 按照循环频率延时
        #     rospy.sleep(0.1)



if __name__ == '__main__':
    # camera_fix_subscriber()
    try:
        robot_publisher()
    except rospy.ROSInterruptException:
        pass
    
