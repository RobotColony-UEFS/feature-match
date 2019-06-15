#coding: utf-8
detectores = ["FAST", "HARRIS", "ORB", "SHITOMASI", "STAR", "SURF"]
timeTotal = []
arquivo = open('totalTempo.txt', 'a')
arquivo.write("Total de tempo gasto \n")

for detc in detectores:
	descritores = ["brief", "brisk", "freak", "orb", "sift"]
	for desc in descritores:
		f = open(detc+"/"+detc+"_"+desc+"/"+detc+"_"+desc+"_Time.txt", 'r')
		nome = detc+"_"+desc
		dados = f.readlines()
		linhas = []
		for inf in dados:
			linhas.append(inf.split())
		time = linhas[1][1]

		arquivo.write(nome+"   "+time+"\n")
		timeTotal.append(time)
		f.close()
print(timeTotal)