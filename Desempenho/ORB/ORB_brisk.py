#coding: utf-8

import cv2
import numpy as np
import sys 

@profile
def ORB_brisk(img):
	img1 = cv2.imread("../imgReferencia/img00.jpg", 0)

	orb = cv2.ORB_create()
	brisk = cv2.BRISK_create()
	bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

	kp1 = orb.detect(img1, None)
	kp1, des1 = brisk.compute(img1, kp1)

	img2 = cv2.imread("../imgTeste/img"+str(img)+".jpg", 0)
	
	kp2 = orb.detect(img2, None)
	kp2, des2 = brisk.compute(img2, kp2)
	matches = bf.match(des1, des2)
	
if __name__ == '__main__':
	imgNumero = sys.argv[1]
	ORB_brisk(imgNumero)