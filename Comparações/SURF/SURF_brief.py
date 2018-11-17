#coding: utf-8

import numpy as np
import cv2
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="descritores",
  passwd="12345678",
  database="referencias"
)

img11 = cv2.imread("/home/samuel/Algoritmos_tcc/Comparações/imgReferencia/img00.jpg", 0)
altura = img11.shape[0]
largura = img11.shape[1]
img1 = cv2.resize(img11, (int(largura*0.4), int(altura*0.4)))
img_dir = "/home/samuel/Algoritmos_tcc/Comparações/imgTeste/"
quantidadeImagens=1

surf = cv2.xfeatures2d.SURF_create()
brief = cv2.xfeatures2d.BriefDescriptorExtractor_create()
bf = cv2.BFMatcher_create(cv2.NORM_HAMMING, crossCheck=True)

kp1 = surf.detect(img1,None)
kp1, des1 = brief.compute(img1, kp1)

while(quantidadeImagens<=10):
	acertos = 0
	img22 = cv2.imread("../imgTeste/img"+str(quantidadeImagens)+".jpg", 0)
	altura2 = img22.shape[0]
	largura2 = img22.shape[1]
	img2 = cv2.resize(img22, (int(largura2*0.4), int(altura2*0.4)))


	kp2 = surf.detect(img2,None)
	kp2, des2 = brief.compute(img2, kp2)

	matches = bf.match(des1,des2)
	matches = sorted(matches, key = lambda x:x.distance)

	with open("../imgTeste/img"+str(quantidadeImagens)+".txt",'r') as f:
		texto=f.readlines()
	posicao_x= np.float_(texto[0:4])
	posicao_y = np.float_(texto[4:8])
	min_x = float(min(posicao_x))
	max_x = float(max(posicao_x))
	min_y = float(min(posicao_y))
	max_y = float(max(posicao_y))

	if len(matches)>10:
		    src_pts = np.float32([ kp1[m.queryIdx].pt for m in matches ]).reshape(-1,1,2)
		    dst_pts = np.float32([ kp2[m.trainIdx].pt for m in matches ]).reshape(-1,1,2)
		    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
		    h,w = img1.shape
		    pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
		    dst = cv2.perspectiveTransform(pts,M)
		    img2 = cv2.polylines(img2,[np.int32(dst)],True,255,3, cv2.LINE_AA)
		    for pos in dst_pts:
		    	if((pos[0][0]>(min_x) and pos[0][0]<(max_x)) and (pos[0][1]>(min_y) and pos[0][1]<(max_y))):
		    		acertos+=1	  

	img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:],None,flags=2)
	cv2.imwrite("../resultados/surf-brief/img"+str(quantidadeImagens)+".jpg", img3)
	mycursor = mydb.cursor()
	sql = "INSERT INTO surf_brief(Nome, Matches, Correto, ImgReferente) VALUES (%s, %s, %s, %s)"
	valor = ("Surf-Brief"+str(quantidadeImagens), len(matches), acertos, "img"+str(quantidadeImagens)+".jpg")
	mycursor.execute(sql, valor)
	mydb.commit()
	print(len(matches), acertos)
	quantidadeImagens+=1