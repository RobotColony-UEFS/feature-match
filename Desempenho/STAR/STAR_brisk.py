#coding: utf-8

import numpy as np
import cv2
import sys

@profile
def STAR_brisk(img):
	img1 = cv2.imread("../imgReferencia/img00.jpg", 0)

	star = cv2.xfeatures2d.StarDetector_create()
	brisk = cv2.BRISK_create()
	bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

	kp1 = star.detect(img1,None)
	kp1, des1 = brisk.compute(img1, kp1)

	img2 = cv2.imread("../imgTeste/img"+str(img)+".jpg", 0)
	
	kp2 = star.detect(img2,None)
	kp2, des2 = brisk.compute(img2, kp2)
	matches = bf.match(des1,des2)
	
if __name__ == '__main__':
	imgNumero = sys.argv[1]
	STAR_brisk(imgNumero)