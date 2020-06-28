# coding=UTF-8
import abb
import time


doGripperOpen = 1
doGripperClose = 2
R = abb.Robot('192.168.125.1') # connecting to robot
R.set_cartesian([[346, 0, 212], [0.708, 0.0345, 0.704, -0.0168]])
R.set_dio(doGripperClose, 0)
R.set_dio(doGripperOpen, 1)
time.sleep(0.1)

grip_down_time = 0.35
dx = 0.406  # image space to robot space   60.5/149
dy = 0.406 # image space to robot space 60.5/149
s = 250 #等待的距离

def grip(pos_y,pos_x,speed):
    wait_time = (s-(pos_y-180)*dy)/speed
    x = 340 - (pos_x - 211) * dx
    R.set_speed([100, 100, 100, 100])
    # Ready position
    R.set_cartesian([[x, 0, 212], [0.708, 0.0345, 0.704, -0.0168]])
    R.set_dio(doGripperClose, 0)
    R.set_dio(doGripperOpen, 1)
    time.sleep(wait_time-grip_down_time)  # 延时等待信号 1.8
    # Grip position
    R.set_cartesian([[x, 0, 194], [0.708, 0.0345, 0.704, -0.0168]])
    time.sleep(0.1)
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
    if TYPE == 1:  # Left Yellow
        # case 1
        R.set_joints([126.47, -0.16, 50.21, 37.15, -55.58, -23.76])
        R.set_joints([144.83, 7.45, 2.70, 81.89, -48.89, -78])
        # R.set_cartesian([[-290, 417, 572.63], [0.472, -0.5347, 0.46856, 0.521]]) #[0.45883, -0.50158, 0.4721, 0.56117]
        R.set_cartesian([[-290, 417, 563.3], [0.472, -0.5347, 0.46856, 0.521]])
        time.sleep(1)
        R.set_dio(doGripperClose, 0)
        R.set_dio(doGripperOpen, 1)
        R.set_joints([144.83, 7.45, 2.70, 81.89, -48.89, -78])
        R.set_joints([126.47, -0.16, 50.21, 37.15, -55.58, -23.76])

    elif TYPE == 2:  # Middle Red
        # case 2
        R.set_joints([126.47, -0.16, 50.21, 37.15, -55.58, -23.76])
        R.set_joints([126.47, -13.44, 23.57, 74.15, -31.18, -72.22])
        R.set_cartesian([[-154, 417, 561.3], [0.472, -0.5347, 0.46856, 0.521]])
        time.sleep(1)
        R.set_dio(doGripperClose, 0)
        R.set_dio(doGripperOpen, 1)
        R.set_joints([126.47, -13.44, 23.57, 74.15, -31.18, -72.22])
        R.set_joints([126.47, -0.16, 50.21, 37.15, -55.58, -23.76])

    elif TYPE == 3:  # Right Green
        # case 3
        R.set_joints([100.48, -23.15, 29.69, 33.49, -7.06, -34.19])
        R.set_cartesian([[-43, 417, 558.3], [0.472, -0.5347, 0.46856, 0.521]])
        time.sleep(1)
        R.set_dio(doGripperClose, 0)
        R.set_dio(doGripperOpen, 1)
        R.set_joints([100.48, -23.15, 29.69, 33.49, -7.06, -34.19])

    # go back initial position
    R.set_joints([12.8, -15, 60.3, 16.3, -31.5, -17.45])

    R.set_cartesian([[352, 0, 212], [0.708, 0.0345, 0.704, -0.0168]])
    R.set_speed([50, 50, 50, 50])

