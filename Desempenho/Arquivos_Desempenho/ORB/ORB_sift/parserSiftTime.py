import math

nImg = 1
con=0
l9 = []
l11 = []
l12 = []
l13 = []
l15 = []
l16 = []
l18 = []
l20 = []
l21 = []
l22 = []
timeTotal = []
while(nImg <= 13):
	teste = 1
	while(teste <= 10):
		linhas = []

		f = open("img"+str(nImg)+"/teste"+str(teste)+".txt", 'r')
		dados = f.readlines()

		for inf in dados:
			linhas.append(inf.split())			
		timeTotal.append(float(linhas[27][2]))
		l9.append(float(linhas[35][3]))
		l11.append(float(linhas[37][3]))
		l12.append(float(linhas[38][3]))
		l13.append(float(linhas[39][3]))
		l15.append(float(linhas[41][3]))
		l16.append(float(linhas[42][3]))
		l18.append(float(linhas[44][3]))
		l20.append(float(linhas[46][3]))
		l21.append(float(linhas[47][3]))
		l22.append(float(linhas[48][3]))
		
		teste+=1
	nImg+=1	

mediaTime = sum(timeTotal)/float(len(timeTotal))
mediaL9 = sum(l9)/float(len(l9))
mediaL11 = sum(l11)/float(len(l11))
mediaL12 = sum(l12)/float(len(l12))
mediaL13 = sum(l13)/float(len(l13))
mediaL15 = sum(l15)/float(len(l15))
mediaL16 = sum(l16)/float(len(l16))
mediaL18 = sum(l18)/float(len(l18))
mediaL20 = sum(l20)/float(len(l20))
mediaL21 = sum(l21)/float(len(l21))
mediaL22 = sum(l22)/float(len(l22))

arquivo = open('ORB_sift_Time.txt','w')
arquivo.write("ORB_sift \n")
arquivo.write("Tempo_Total:     "+str(mediaTime)+" s \n")
arquivo.write("Linha    Resultado (Micro-Segundos) \n")
arquivo.write("9      "+str(mediaL9)+"\n")
arquivo.write("11     "+str(mediaL11)+"\n")
arquivo.write("12     "+str(mediaL12)+"\n")
arquivo.write("13     "+str(mediaL13)+"\n")
arquivo.write("15     "+str(mediaL15)+"\n")
arquivo.write("16     "+str(mediaL16)+"\n")
arquivo.write("18     "+str(mediaL18)+"\n")
arquivo.write("20     "+str(mediaL20)+"\n")
arquivo.write("21     "+str(mediaL21)+"\n")
arquivo.write("22     "+str(mediaL22)+"\n")


