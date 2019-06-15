#coding: utf-8
import cv2
import numpy as np
import sys

@profile
def HARRIS_brief(img):
	img1 = cv2.imread("../imgReferencia/img00.jpg", 0)
	brief = cv2.xfeatures2d.BriefDescriptorExtractor_create()

	imagem1 = np.float32(img1)
	dst1 = cv2.cornerHarris(imagem1,2,3,0.04)
	dst1 = cv2.dilate(dst1,None)
	ret1, dst1 = cv2.threshold(dst1,0.01*dst1.max(),255,0)
	dst1 = np.uint8(dst1)
	ret1, labels1, stats1, centroids1 = cv2.connectedComponentsWithStats(dst1)
	criteria1 = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
	corners1 = cv2.cornerSubPix(imagem1,np.float32(centroids1),(5,5),(-1,-1),criteria1)
	matriz1=[]
	for variavel in corners1:
		array=np.array([variavel])
		matriz1.append(array)
	kp1=cv2.KeyPoint_convert(matriz1)
	kp1, des1 = brief.compute(img1, kp1)

	bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

	img2 = cv2.imread("../imgTeste/img"+str(img)+".jpg", 0)
	imagem2 = np.float32(img2)
	dst2 = cv2.cornerHarris(imagem2,2,3,0.04)
	dst2 = cv2.dilate(dst2,None)
	ret2, dst2 = cv2.threshold(dst2,0.01*dst2.max(),255,0)
	dst2 = np.uint8(dst2)
	ret2, labels2, stats2, centroids2 = cv2.connectedComponentsWithStats(dst2)
	criteria2 = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
	corners2 = cv2.cornerSubPix(imagem2,np.float32(centroids2),(5,5),(-1,-1),criteria2)
	matriz2=[]
	for variavel in corners2:
		array=np.array([variavel])
		matriz2.append(array)
	kp2 = cv2.KeyPoint_convert(matriz2)
	kp2, des2 = brief.compute(img2, kp2)

	matches = bf.match(des1,des2)

if __name__ == '__main__':
	imgNumero = sys.argv[1]
	HARRIS_brief(imgNumero)
