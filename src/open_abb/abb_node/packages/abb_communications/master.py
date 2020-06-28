# coding=UTF-8
import cv2
import time
import camera as ca
import robot as rb

Motion = False

if __name__ == '__main__':
	cap = cv2.VideoCapture(0)
	while (cap.isOpened()):
		if not(Motion):
			cla,xc,yc=ca.Detect(cap)
			if(cla>0) & (xc>180):
				Motion = True
				# ret, frame = cap.read()
				print(cla,xc,yc)
		else:
			rb.grip(yc)
			ret, frame = cap.read()
			print("grip")
			rb.place(cla)
			Motion = False

		k = cv2.waitKey(5) & 0xFF
		if k == 27:
			break
	cap.release()
	cv2.destroyAllWindows()
	rb.R.close()



	#
	#     cla,xc,yc=ca.Detect(cap)
	#     if (cla>0) & (xc>180):
	#         move.get(yc)
	#         ret, frame = cap.read()
	#         print("grip")
	        
	# 		# move.put(cla)
	#     	print(cla,xc,yc)
