# coding=UTF-8
import abb
# import cv2
import time

R = abb.Robot('192.168.125.1')

doGripperClose = 2
doGripperOpen = 1

dx = 0.406  # 60.5/149


def grip(pos_x):
    x = 344 - (pos_x - 211) * dx
    # Ready position
    R.set_cartesian([[x, 0, 212], [0.708, 0.0345, 0.704, -0.0168]])
    R.set_dio(doGripperClose, 0)
    R.set_dio(doGripperOpen, 1)
    time.sleep(1.7)  # 延时等待信号
    R.set_cartesian([[x, 0, 194], [0.708, 0.0345, 0.704, -0.0168]])
    time.sleep(0.2)
    R.set_dio(doGripperOpen, 0)
    R.set_dio(doGripperClose, 1)
    R.set_cartesian([[346, 0, 212], [0.708, 0.0345, 0.704, -0.0168]])


def place(TYPE):
    R.set_speed([200, 200, 100, 100])
    # Ready position
    R.set_cartesian([[352, 0, 212], [0.708, 0.0345, 0.704, -0.0168]])
    R.set_cartesian([[352, 0, 398], [0.708, 0.0345, 0.704, -0.0168]])

    R.set_joints([12.8, -15, 60.3, 16.3, -31.5, -17.45])
    # R.set_joints([126.47,-0.16,50.21,37.15,-55.58,-23.76])

    # Select placement which floor
    if TYPE == 1:  # 左边

        # case 1
        R.set_joints([126.47, -0.16, 50.21, 37.15, -55.58, -23.76])
        R.set_joints([144.83, 7.45, 2.70, 81.89, -48.89, -78])
        R.set_cartesian([[-290, 417, 572.63], [0.472, -0.5347, 0.46856, 0.521]])
        time.sleep(1)
        R.set_dio(doGripperClose, 0)
        R.set_dio(doGripperOpen, 1)
        R.set_joints([144.83, 7.45, 2.70, 81.89, -48.89, -78])
        R.set_joints([126.47, -0.16, 50.21, 37.15, -55.58, -23.76])

    elif TYPE == 2:  # 中间
        # case 2
        R.set_joints([126.47, -0.16, 50.21, 37.15, -55.58, -23.76])
        R.set_joints([126.47, -13.44, 23.57, 74.15, -31.18, -72.22])
        R.set_cartesian([[-155, 417, 572.63], [0.472, -0.5347, 0.46856, 0.521]])
        time.sleep(1)
        R.set_dio(doGripperClose, 0)
        R.set_dio(doGripperOpen, 1)
        R.set_joints([126.47, -13.44, 23.57, 74.15, -31.18, -72.22])
        R.set_joints([126.47, -0.16, 50.21, 37.15, -55.58, -23.76])

    elif TYPE == 3:  # 右边
        # case 3
        R.set_joints([100.48, -23.15, 29.69, 33.49, -7.06, -34.19])
        R.set_cartesian([[-45, 417, 572.63], [0.472, -0.5347, 0.46856, 0.521]])
        time.sleep(1)
        R.set_dio(doGripperClose, 0)
        R.set_dio(doGripperOpen, 1)
        R.set_joints([100.48, -23.15, 29.69, 33.49, -7.06, -34.19])
    # R.set_joints([98.98,-39.17,50.48,0,-10.18,2.1])

    # R.set_joints([126.47,-0.16,50.21,37.15,-55.58,-23.76])
    # go back initial position
    R.set_joints([12.8, -15, 60.3, 16.3, -31.5, -17.45])

    R.set_cartesian([[352, 0, 212], [0.708, 0.0345, 0.704, -0.0168]])
    R.set_speed([50, 50, 50, 50])

