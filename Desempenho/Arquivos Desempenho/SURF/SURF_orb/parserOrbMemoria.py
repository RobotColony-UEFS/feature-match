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
while(nImg <= 13):
	teste = 1
	while(teste <= 10):
		linhas = []

		f = open("img"+str(nImg)+"/teste"+str(teste)+".txt", 'r')
		dados = f.readlines()

		for inf in dados:
			linhas.append(inf.split())			

		l9.append(float(linhas[7][3]))
		l11.append(float(linhas[9][3]))
		l12.append(float(linhas[10][3]))
		l13.append(float(linhas[11][3]))
		l15.append(float(linhas[13][3]))
		l16.append(float(linhas[14][3]))
		l18.append(float(linhas[16][3]))
		l20.append(float(linhas[18][3]))
		l21.append(float(linhas[19][3]))
		l22.append(float(linhas[20][3]))
		
		teste+=1
	nImg+=1	


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

arquivo = open('SURF_orb_memoria.txt','w')
arquivo.write("SURF_orb \n")
arquivo.write("Linha     Resultado (Mb) \n")
arquivo.write("9       "+str(mediaL9)+"\n")
arquivo.write("11      "+str(mediaL11)+"\n")
arquivo.write("12      "+str(mediaL12)+"\n")
arquivo.write("13      "+str(mediaL13)+"\n")
arquivo.write("15      "+str(mediaL15)+"\n")
arquivo.write("16      "+str(mediaL16)+"\n")
arquivo.write("18      "+str(mediaL18)+"\n")
arquivo.write("20      "+str(mediaL20)+"\n")
arquivo.write("21      "+str(mediaL21)+"\n")
arquivo.write("22      "+str(mediaL22)+"\n")


