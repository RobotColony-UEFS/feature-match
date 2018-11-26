#coding: utf-8

import numpy as np
import cv2

@profile
def STAR_orb():
	img1 = cv2.imread("../imgReferencia/img00.jpg", 0)

	star = cv2.xfeatures2d.StarDetector_create()
	orb = cv2.ORB_create()

	bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
		
	kp1 = star.detect(img1,None)
	kp1, des1 = orb.compute(img1, kp1)

	img2 = cv2.imread("../imgTeste/img1.jpg", 0)

	kp2 = star.detect(img2,None)
	kp2, des2 = orb.compute(img2, kp2)

	matches = bf.match(des1,des2)
	
if __name__ == '__main__':
	STAR_orb()