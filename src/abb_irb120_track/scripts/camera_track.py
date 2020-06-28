#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import time


# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()
# Change thresholds
params.minThreshold = 0
params.maxThreshold = 256
params.thresholdStep = 10
# Filter by Color.
params.filterByColor = False
# Filter by Area.
params.filterByArea = True
params.minArea = 10000
params.maxArea = 200000
# Filter by Circularity
params.filterByCircularity = False
params.minCircularity = 0.5
# Filter by Convexity
params.filterByConvexity = False
params.minConvexity = 0.5
# Filter by Inertia
params.filterByInertia = False
params.minInertiaRatio = 0.5

count = 0 #计数用

def track(cap):
	xc = 0
	yc = 0

	ret, frame = cap.read()
	# # show orignal 
	# cv2.imshow('frame', frame)  
	# cv2.waitKey(10)
	# sp = frame.shape
	# print sp 

	# b, g, r = cv2.split(frame)  #color separation
	# cv2.imshow("image_r", r)
	# cv2.imshow("image_g", g)
	# cv2.imshow("image_b", b)
	# frame = cv2.medianBlur(frame, 5)  #中值滤波

	# img_yellow = cv2.inRange(frame,(0,200,200),(100,255,255))
	img_red = cv2.inRange(frame,(30,30,190),(160,140,255))

	# rgb to gray
	# gary = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	# cv2.imshow("gary",gary)
	# cv2.waitKey(10)

	# rgb to hsv
	img_hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	# cv2.imshow("hsv",img_hsv)
	# cv2.waitKey(10)

	img_yellow = cv2.inRange(img_hsv,(26,43,46),(34,255,255))
	# img_red1 = cv2.inRange(img_hsv,(0,43,46),(10,255,255))
	# img_red2 = cv2.inRange(img_hsv,(156,43,46),(180,255,255))
	# img_red = img_red1+img_red2
	# img_green = cv2.inRange(img_hsv,(43,43,46),(70,255,255))

	cv2.imshow("img_yellow",img_yellow)
	cv2.waitKey(1)
	cv2.imshow("img_red",img_red)
	cv2.waitKey(1)
	# cv2.imshow("img_green",img_green)
	# cv2.waitKey(10)

	detector = cv2.SimpleBlobDetector_create(params)
	# Detect blobs
	keypoints = detector.detect(img_red)
	# print(keypoints)

	for kp in keypoints :
		xc = kp.pt[0]
		yc = kp.pt[1]

	if (xc==0)&(yc==0):
		keypoints = detector.detect(img_yellow)
		# print(keypoints)

		for kp in keypoints :
			# point = kp.pt
			xc = kp.pt[0]
			yc = kp.pt[1]
			# print(point)

	im_with_keypoints = cv2.drawKeypoints(frame,keypoints,np.array([]),(255,0,0),cv2.DRAW_MATCHES_FLAGS_DEFAULT)
	im_with_keypoints = cv2.drawKeypoints(im_with_keypoints,keypoints,np.array([]),(255,0,0),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

	cv2.imshow("Keypoints",im_with_keypoints)
	cv2.waitKey(1)


	return xc,yc

