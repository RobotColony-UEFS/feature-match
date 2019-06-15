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
while(nImg <= 13):
	teste = 1
	while(teste <= 10):
		linhas = []

		f = open("img"+str(nImg)+"/teste"+str(teste)+".txt", 'r')
		dados = f.readlines()

		for inf in dados:
			linhas.append(inf.split())			

		l9.append(float(linhas[6][3]))
		l10.append(float(linhas[7][3]))	
		l11.append(float(linhas[8][3]))
		l12.append(float(linhas[9][3]))
		l14.append(float(linhas[11][3]))
		l15.append(float(linhas[12][3]))
		l16.append(float(linhas[13][3]))
		l17.append(float(linhas[14][3]))		
		l19.append(float(linhas[16][3]))
		l20.append(float(linhas[17][3]))
		l21.append(float(linhas[18][3]))
		l22.append(float(linhas[19][3]))
		l24.append(float(linhas[21][3]))
		
		teste+=1
	nImg+=1	


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

arquivo = open('SHITOMASI_sift_memoria.txt','w')
arquivo.write("SHITOMASI_sift \n")
arquivo.write("Linha     Resultado (Mb) \n")
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


