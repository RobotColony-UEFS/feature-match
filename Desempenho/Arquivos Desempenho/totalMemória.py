#coding: utf-8
detectores = ["FAST", "HARRIS", "ORB", "SHITOMASI", "STAR", "SURF"]
memTotal = []
arquivo = open('totalMemoria.txt', 'a')
arquivo.write("Total de memória gasto \n")

for detc in detectores:
	descritores = ["brief", "brisk", "freak", "orb", "sift"]
	for desc in descritores:
		i = 2
		f = open(detc+"/"+detc+"_"+desc+"/"+detc+"_"+desc+"_memoria.txt", 'r')
		nome = detc+"_"+desc
		dados = f.readlines()
		linhas = []
		for inf in dados:
			linhas.append(inf.split())

		somaMem = 0
		while(i<len(linhas)):
			somaMem = somaMem + float(linhas[i][1])
			i+=1
		arquivo.write(nome+"   "+str(somaMem)+"\n")
		
		memTotal.append(somaMem)
		f.close()
print(memTotal)