# coding=UTF-8
import cv2
import numpy as np
import lsqcurvefit as lsq


def Detect(cap):
    ret, frame = cap.read()

    # 背景去除
    # frame=frame[60:400, :]
    b, g, r = cv2.split(frame)
    mask = ((g > 160) | (r > 180)).astype(np.uint8) #红绿黄为1
    mask = mask * 255
    mask[:60, :] = 0
    mask[400:, :] = 0
    res = cv2.bitwise_and(frame, frame, mask=mask) #去除背景
    res = cv2.medianBlur(res, 5)  #中值滤波
    # 图像处理
    gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY) #转化为灰度图
    gray = cv2.GaussianBlur(gray, (5, 5), 0)  #高斯模糊
    edge = cv2.Canny(gray, 70, 200)  #边缘检测
    # 物体检测
    e = np.nonzero(edge)
    n = len(e[0]) #边缘像素总数
    if n > 430: #为有效物体
        xc, yc, rc = lsq.Circle_Fit(e[1], e[0]) #圆拟合
        cv2.circle(frame, (xc, yc), rc, (255, 0, 0), 3) #画圆
        cv2.circle(frame, (xc, yc), 5, (255, 0, 0), -1) #画圆心

        # 判断物体类型
        b, g, r = cv2.split(res)
        yellow = np.uint8(((g > 160) & (r > 180)))
        red = np.uint8((r > 180))
        if np.sum(yellow.flatten())>1000: #黄色
            cla=1
        elif np.sum(red.flatten())>1000: #红色
            cla=2
        else: #绿色
            cla=3
    else:
        cla=0
        xc=0
        yc=0
    cv2.imshow('frame', frame)
    # cv2.imshow('edge', edge)

    return cla,xc,yc

