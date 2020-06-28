# coding=UTF-8
import cv2
import time
import camera as ca
import robot as rb

Motion = False
Count = 0
Color = {1:"Yellow",2:"Red",3:"Green"}
speed = 0
dx = 0.406  # image space to robot space   60.5/149
xc = 0
yc = 0

if __name__ == '__main__':
	cap = cv2.VideoCapture(1)
	while (cap.isOpened()):
		if not(Motion):
			color,last_xc,yc=ca.Detect(cap)
			if (color > 0) & (last_xc > 160):
				time.sleep(0.2)
				color, xc, yc = ca.Detect(cap)
				speed = ((xc - last_xc) * dx / 0.2)
				last_xc = xc
				print(Count, xc, yc, speed)
				for i in range(3):
					time.sleep(0.2)
					color, xc, yc = ca.Detect(cap)
					speed = (speed + ((xc - last_xc) * dx / 0.2)) / 2
					last_xc = xc
					print(Count, xc, yc, speed)
					if (speed<0) | (xc==0):
						break
				Count = Count + 1
				Motion = True
		else:
			if (speed<0) | (xc==0):
				Motion = False
			rb.grip(xc,yc,speed)
			ret, frame = cap.read()
			print(Color[color])
			rb.place(color)
			Motion = False

		k = cv2.waitKey(5) & 0xFF
		if k == 27:
			break
	cap.release()
	cv2.destroyAllWindows()
	rb.R.close()
