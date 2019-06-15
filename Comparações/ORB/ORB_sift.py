#coding: utf-8

import cv2
import numpy as np
import mysql.connector
import math

mydb = mysql.connector.connect(
  host="localhost",
  user="descritores",
  passwd="12345678",
  database="referencias"
)


def desvio (vetResult):
	# Desvio padrão populacional
	soma = float(sum(vetResult))
	media = soma/len(vetResult)
	res = 0
	for valor in vetResult:
		res += ((valor - media)**2)

	desvio = (math.sqrt(res/len(vetResult)))
	return (media, desvio)


vet_matches = []
vet_corretos = []

img11 = cv2.imread("../../imgReferencia/img00.jpg", 0)
altura = img11.shape[0]
largura = img11.shape[1]
img1 = cv2.resize(img11, (int(largura*0.4), int(altura*0.4)))
orb = cv2.ORB_create()
sift = cv2.xfeatures2d.SIFT_create()
bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)

quantidadeImagens = 1

kp1 = orb.detect(img1, None)
kp1, des1 = sift.compute(img1, kp1)

while(quantidadeImagens<=13):
	acertos = 0
	img22 = cv2.imread("../../imgTeste/img"+str(quantidadeImagens)+".jpg", 0)
	altura2 = img22.shape[0]
	largura2 = img22.shape[1]
	img2 = cv2.resize(img22, (int(largura2*0.4), int(altura2*0.4)))
	
	kp2 = orb.detect(img2, None)	
	kp2, des2 = sift.compute(img2, kp2)
	
	mat = bf.match(des1, des2)
	mat = sorted(mat, key = lambda x:x.distance)
	matches = mat[0:150]
	with open("../../imgTeste/img"+str(quantidadeImagens)+".txt",'r') as f:
		texto=f.readlines()
	posicao_x= np.float_(texto[0:4])
	posicao_y = np.float_(texto[4:8])
	min_x = float(min(posicao_x))
	max_x = float(max(posicao_x))
	min_y = float(min(posicao_y))
	max_y = float(max(posicao_y))

	if len(matches)>15:
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
	cv2.imwrite("../resultados/orb-sift/img"+str(quantidadeImagens)+".jpg", img3)
	vet_matches.append(len(matches))
	vet_corretos.append(acertos)
	mycursor = mydb.cursor()
	sql = "INSERT INTO orb_sift(Nome, Matches, Correto, ImgReferente) VALUES (%s, %s, %s, %s)"
	valor = ("Orb-sift"+str(quantidadeImagens), len(matches), acertos, "img"+str(quantidadeImagens)+".jpg")
	mycursor.execute(sql, valor)
	mydb.commit()
	print(len(matches), acertos)
	quantidadeImagens+=1

media_matches, desvio_matches = desvio(vet_matches)
media_corretos, desvio_corretos = desvio(vet_corretos)
porcentagem  = (media_corretos/media_matches)*100
sql2 = "INSERT INTO medias_desvios(Nome, MediaMatches, DesvioMatches, MediaCorretos, DesvioCorretos, Porcentagem) VALUES (%s, %s, %s, %s, %s, %s)"
valor2 = ("orb_sift", media_matches, desvio_matches, media_corretos, desvio_corretos, porcentagem)
mycursor.execute(sql2, valor2)
mydb.commit()