#coding: utf-8

import cv2
import numpy as np

@profile
def SHITOMASI_brisk():
	img1 = cv2.imread("../imgReferencia/img00.jpg", 0)

	corners11 = cv2.goodFeaturesToTrack(img1, 100, 0.01, 10)
	corners1 = np.int0(corners11)
	kp1 = cv2.KeyPoint_convert(corners1)

	brisk = cv2.BRISK_create()
	bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
	kp1, des1 = brisk.compute(img1, kp1)

	img2 = cv2.imread("../imgTeste/img1.jpg", 0)
	
	corners22 = cv2.goodFeaturesToTrack(img2, 100, 0.01, 10)
	corners2 = np.int0(corners22)
	kp2 = cv2.KeyPoint_convert(corners2)
	kp2, des2 = brisk.compute(img2, kp2)

	matches = bf.match(des1,des2)
	
if __name__ == '__main__':
	SHITOMASI_brisk()