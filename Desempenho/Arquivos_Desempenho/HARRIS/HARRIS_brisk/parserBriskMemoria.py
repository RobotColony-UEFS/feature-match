import math

nImg = 1
con=0
l8 = []
l9 = []
l11 = []
l12 = []
l13 = []
l14 = []
l15 = []
l16 = []
l17 = []
l18 = []
l19 = []
l20 = []
l21 = []
l22 = []
l23 = []
l24 = []
l26 = []
l28 = []
l29 = []
l30 = []
l31 = []
l32 = []
l33 = []
l34 = []
l35 = []
l36 = []
l37 = []
l38 = []
l39 = []
l40 = []
l41 = []
l42 = []
l44 = []

while(nImg <= 13):
	teste = 1
	while(teste <= 10):
		linhas = []

		f = open("img"+str(nImg)+"/teste"+str(teste)+".txt", 'r')
		dados = f.readlines()

		for inf in dados:
			linhas.append(inf.split())			
		l8.append(float(linhas[6][3]))
		l9.append(float(linhas[7][3]))
		l11.append(float(linhas[9][3]))
		l12.append(float(linhas[10][3]))
		l13.append(float(linhas[11][3]))
		l14.append(float(linhas[12][3]))			
		l15.append(float(linhas[13][3]))
		l16.append(float(linhas[14][3]))
		l17.append(float(linhas[15][3]))		
		l18.append(float(linhas[16][3]))
		l19.append(float(linhas[17][3]))		
		l20.append(float(linhas[18][3]))
		l21.append(float(linhas[19][3]))
		l22.append(float(linhas[20][3]))
		l23.append(float(linhas[21][3]))
		l24.append(float(linhas[22][3]))
		l26.append(float(linhas[24][3]))	
		l28.append(float(linhas[26][3]))
		l29.append(float(linhas[27][3]))
		l30.append(float(linhas[28][3]))			
		l31.append(float(linhas[29][3]))
		l32.append(float(linhas[30][3]))
		l33.append(float(linhas[31][3]))		
		l34.append(float(linhas[32][3]))
		l35.append(float(linhas[33][3]))		
		l36.append(float(linhas[34][3]))
		l37.append(float(linhas[35][3]))
		l38.append(float(linhas[36][3]))
		l39.append(float(linhas[37][3]))
		l40.append(float(linhas[38][3]))
		l41.append(float(linhas[39][3]))	
		l42.append(float(linhas[40][3]))	
		l44.append(float(linhas[42][3]))	
						

	
		teste+=1
	nImg+=1	

mediaL8 = sum(l8)/float(len(l8))
mediaL9 = sum(l9)/float(len(l9))
mediaL11 = sum(l11)/float(len(l11))
mediaL12 = sum(l12)/float(len(l12))
mediaL13 = sum(l13)/float(len(l13))
mediaL14 = sum(l14)/float(len(l14))
mediaL15 = sum(l15)/float(len(l15))
mediaL16 = sum(l16)/float(len(l16))
mediaL17 = sum(l17)/float(len(l17))
mediaL18 = sum(l18)/float(len(l18))
mediaL19 = sum(l19)/float(len(l19))
mediaL20 = sum(l20)/float(len(l20))
mediaL21 = sum(l21)/float(len(l21))
mediaL22 = sum(l22)/float(len(l22))
mediaL23 = sum(l23)/float(len(l23))
mediaL24 = sum(l24)/float(len(l24))
mediaL26 = sum(l26)/float(len(l26))
mediaL28 = sum(l28)/float(len(l28))
mediaL29 = sum(l29)/float(len(l29))
mediaL30 = sum(l30)/float(len(l30))
mediaL31 = sum(l31)/float(len(l31))
mediaL32 = sum(l32)/float(len(l32))
mediaL33 = sum(l33)/float(len(l33))
mediaL34 = sum(l34)/float(len(l34))
mediaL35 = sum(l35)/float(len(l35))
mediaL36 = sum(l36)/float(len(l36))
mediaL37 = sum(l37)/float(len(l37))
mediaL38 = sum(l38)/float(len(l38))
mediaL39 = sum(l39)/float(len(l39))
mediaL40 = sum(l40)/float(len(l40))
mediaL41 = sum(l41)/float(len(l41))
mediaL42 = sum(l42)/float(len(l42))
mediaL44 = sum(l44)/float(len(l44))





arquivo = open('HARRIS_brisk_memoria.txt','w')
arquivo.write("HARRIS_brisk \n")
arquivo.write("Linha     Resultado (Mb) \n")
arquivo.write("8        "+str(mediaL8)+"\n")
arquivo.write("9        "+str(mediaL9)+"\n")
arquivo.write("11       "+str(mediaL11)+"\n")
arquivo.write("12       "+str(mediaL12)+"\n")
arquivo.write("13       "+str(mediaL13)+"\n")
arquivo.write("14       "+str(mediaL14)+"\n")
arquivo.write("15       "+str(mediaL15)+"\n")
arquivo.write("16       "+str(mediaL16)+"\n")
arquivo.write("17       "+str(mediaL17)+"\n")
arquivo.write("18       "+str(mediaL18)+"\n")
arquivo.write("19       "+str(mediaL19)+"\n")
arquivo.write("20       "+str(mediaL20)+"\n")
arquivo.write("21       "+str(mediaL21)+"\n")
arquivo.write("22       "+str(mediaL22)+"\n")
arquivo.write("23       "+str(mediaL23)+"\n")
arquivo.write("24       "+str(mediaL24)+"\n")
arquivo.write("26       "+str(mediaL26)+"\n")
arquivo.write("28       "+str(mediaL28)+"\n")
arquivo.write("29       "+str(mediaL29)+"\n")
arquivo.write("30       "+str(mediaL30)+"\n")
arquivo.write("31       "+str(mediaL31)+"\n")
arquivo.write("32       "+str(mediaL32)+"\n")
arquivo.write("33       "+str(mediaL33)+"\n")
arquivo.write("34       "+str(mediaL34)+"\n")
arquivo.write("35       "+str(mediaL35)+"\n")
arquivo.write("36       "+str(mediaL36)+"\n")
arquivo.write("37       "+str(mediaL37)+"\n")
arquivo.write("38       "+str(mediaL38)+"\n")
arquivo.write("39       "+str(mediaL39)+"\n")
arquivo.write("40       "+str(mediaL40)+"\n")
arquivo.write("41       "+str(mediaL41)+"\n")
arquivo.write("42       "+str(mediaL42)+"\n")
arquivo.write("44       "+str(mediaL44)+"\n")


