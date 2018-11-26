#coding: utf-8

import numpy as np
import cv2

@profile
def FAST_sift():
	img1 = cv2.imread("../imgReferencia/img00.jpg", 0)

	fast = cv2.FastFeatureDetector_create(threshold=25)
	sift = cv2.xfeatures2d.SIFT_create()
	bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)

	kp1 = fast.detect(img1,None)
	kp1, des1 = sift.compute(img1, kp1)

	img2 = cv2.imread("../imgTeste/img1.jpg", 0)

	kp2 = fast.detect(img2,None)
	kp2, des2 = sift.compute(img2, kp2)

	matches = bf.match(des1,des2)

if __name__ == '__main__':
	FAST_sift()