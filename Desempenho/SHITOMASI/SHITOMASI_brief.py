#coding: utf-8

import cv2
import numpy as np

# @profile
def SHITOMASI_brief():
	img1 = cv2.imread("../imgReferencia/img00.jpg")
	gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)


	corners11 = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
	corners1 = np.int0(corners11)
	kp1 = cv2.KeyPoint_convert(corners1)

	brief = cv2.xfeatures2d.BriefDescriptorExtractor_create()
	bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
	kp1, des1 = brief.compute(img1, kp1)
	img2 = cv2.imread("../imgTeste/img1.jpg", 0)
	
	corners22 = cv2.goodFeaturesToTrack(img2, 100, 0.01, 10)
	corners2 = np.int0(corners22)
	kp2 = cv2.KeyPoint_convert(corners2)
	kp2, des2 = brief.compute(img2, kp2)

	matches = bf.match(des1,des2)
	
if __name__ == '__main__':
	SHITOMASI_brief()