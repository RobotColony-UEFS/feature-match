#coding: utf-8

import numpy as np
import cv2

@profile
def SURF_freak():
	img1 = cv2.imread("../imgReferencia/img00.jpg", 0)

	surf = cv2.xfeatures2d.SURF_create()
	freak = cv2.xfeatures2d.FREAK_create()
	bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
		
	kp1 = surf.detect(img1,None)
	kp1, des1 = freak.compute(img1, kp1)

	img2 = cv2.imread("../imgTeste/img1.jpg", 0)

	kp2 = surf.detect(img2,None)
	kp2, des2 = freak.compute(img2, kp2)

	matches = bf.match(des1,des2)
	
if __name__ == '__main__':
	SURF_freak()