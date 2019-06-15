import math

nImg = 1
con=0
l9 = []
l10 = []
l11 = []
l12 = []
l14 = []
l15 = []
l16 = []
l17 = []
l19 = []
l20 = []
l21 = []
l22 = []
l24 = []
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
		l10.append(float(linhas[36][3]))	
		l11.append(float(linhas[37][3]))
		l12.append(float(linhas[38][3]))
		l14.append(float(linhas[40][3]))
		l15.append(float(linhas[41][3]))
		l16.append(float(linhas[42][3]))
		l17.append(float(linhas[43][3]))		
		l19.append(float(linhas[45][3]))
		l20.append(float(linhas[46][3]))
		l21.append(float(linhas[47][3]))
		l22.append(float(linhas[48][3]))
		l24.append(float(linhas[50][3]))
		
		teste+=1
	nImg+=1	

mediaTime = sum(timeTotal)/float(len(timeTotal))
mediaL9 = sum(l9)/float(len(l9))
mediaL10 = sum(l10)/float(len(l10))
mediaL11 = sum(l11)/float(len(l11))
mediaL12 = sum(l12)/float(len(l12))
mediaL14 = sum(l14)/float(len(l14))
mediaL15 = sum(l15)/float(len(l15))
mediaL16 = sum(l16)/float(len(l16))
mediaL17 = sum(l17)/float(len(l17))
mediaL19 = sum(l19)/float(len(l19))
mediaL20 = sum(l20)/float(len(l20))
mediaL21 = sum(l21)/float(len(l21))
mediaL22 = sum(l22)/float(len(l22))
mediaL24 = sum(l24)/float(len(l24))

arquivo = open('SHITOMASI_orb_Time.txt','w')
arquivo.write("SHITOMASI_orb \n")
arquivo.write("Tempo_Total:     "+str(mediaTime)+" s \n")
arquivo.write("Linha    Resultado (Micro-Segundos) \n")
arquivo.write("9       "+str(mediaL9)+"\n")
arquivo.write("10      "+str(mediaL10)+"\n")
arquivo.write("11      "+str(mediaL11)+"\n")
arquivo.write("12      "+str(mediaL12)+"\n")
arquivo.write("14      "+str(mediaL14)+"\n")
arquivo.write("15      "+str(mediaL15)+"\n")
arquivo.write("16      "+str(mediaL16)+"\n")
arquivo.write("17      "+str(mediaL17)+"\n")
arquivo.write("19      "+str(mediaL19)+"\n")
arquivo.write("20      "+str(mediaL20)+"\n")
arquivo.write("21      "+str(mediaL21)+"\n")
arquivo.write("22      "+str(mediaL22)+"\n")
arquivo.write("24      "+str(mediaL24)+"\n")


