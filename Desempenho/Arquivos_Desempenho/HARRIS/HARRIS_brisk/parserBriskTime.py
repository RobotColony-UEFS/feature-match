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
timeTotal = []

while(nImg <= 13):
	teste = 1
	while(teste <= 10):
		linhas = []

		f = open("img"+str(nImg)+"/teste"+str(teste)+".txt", 'r')
		dados = f.readlines()

		for inf in dados:
			linhas.append(inf.split())	
		timeTotal.append(float(linhas[48][2]))		
		l8.append(float(linhas[56][2]))
		l9.append(float(linhas[57][2]))
		l11.append(float(linhas[59][2]))
		l12.append(float(linhas[60][2]))
		l13.append(float(linhas[61][2]))
		l14.append(float(linhas[62][2]))			
		l15.append(float(linhas[63][2]))
		l16.append(float(linhas[64][2]))
		l17.append(float(linhas[65][2]))		
		l18.append(float(linhas[66][2]))
		l19.append(float(linhas[67][2]))		
		l20.append(float(linhas[68][2]))
		l21.append(float(linhas[69][2]))
		l22.append(float(linhas[70][2]))
		l23.append(float(linhas[71][2]))
		l24.append(float(linhas[72][2]))
		l26.append(float(linhas[74][2]))	
		l28.append(float(linhas[76][2]))
		l29.append(float(linhas[77][2]))
		l30.append(float(linhas[78][2]))			
		l31.append(float(linhas[79][2]))
		l32.append(float(linhas[80][2]))
		l33.append(float(linhas[81][2]))		
		l34.append(float(linhas[82][2]))
		l35.append(float(linhas[83][2]))		
		l36.append(float(linhas[84][2]))
		l37.append(float(linhas[85][2]))
		l38.append(float(linhas[86][2]))
		l39.append(float(linhas[87][2]))
		l40.append(float(linhas[88][2]))
		l41.append(float(linhas[89][2]))	
		l42.append(float(linhas[90][2]))	
		l44.append(float(linhas[92][2]))	
						

	
		teste+=1
	nImg+=1	
mediaTime = sum(timeTotal)/float(len(timeTotal))
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





arquivo = open('HARRIS_brisk_time.txt','w')
arquivo.write("HARRIS_brisk \n")
arquivo.write("Tempo_Total:     "+str(mediaTime)+" s \n")
arquivo.write("Linha    Resultado (Micro-Segundos) \n")
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


