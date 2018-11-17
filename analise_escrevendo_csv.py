#coding: utf-8

import mysql.connector
import math
import csv
from decimal import *

# Análise com falha, pois o desvio padrão está obtendo as relação para matches e corretos, mas não necessariamente
# a relação este os matches e corretos, o desviopadrão não está levando em consideração esse problema

def desvio (vetResult):
	# Desvio padrão populacional
	soma = float(sum(vetResult))
	media = soma/len(vetResult)
	res = 0
	for valor in vetResult:
		res += ((valor - media)**2)

	desvio = (math.sqrt(res/len(vetResult)))
	return (media, desvio)




matches = []
corretos = []
Med_matches = []
Med_Corretos = []
Des_Matches = []
Des_Corretos = []
Nomes = []
Porcent_Acertos = []


mydb = mysql.connector.connect(
	host = "localhost",
	user = "descritores",
	passwd = "12345678",
	database = "referencias"
)
detectores = ["fast", "harris", "orb", "shiTomasi", "star", "surf"]
descritores = ["brief" ,"brisk", "freak", "orb", "sift"]
#mydb.cursor() instancia objetos que podem executar operações, como inserir, select .....

for dect in detectores:
	detector = dect
	for desc in descritores:
		nomeAlg = str(dect+"_"+desc)
		mycursor = mydb.cursor()
		sql = "SELECT * FROM "+nomeAlg
		mycursor.execute(sql)
		result = mycursor.fetchall()
		
		Nomes.append(nomeAlg)
		porcentSoma = 0
		arquivo = open("arquivosTxt/detector_"+detector+"/"+nomeAlg,'w')
		arquivo.write("                     "+nomeAlg)
		arquivo.write("\n\n")
		arquivo.write("  Nome----Matches---Corretos---Porcentagem---ImgAssociada\n")
		arquivo.write("\n")

		for dado in result:
			porcentagem = "%.2f"%((float(dado[2])/float(dado[1]))*100)
			
			arquivo.write(" "+dado[0]),
			arquivo.write("    "+str(dado[1])),
			arquivo.write("    "+str(dado[2])),
			arquivo.write("       "+str(porcentagem)+"%"),
			arquivo.write("        "+str(dado[3]))
			arquivo.write("\n")
			porcentSoma += float(porcentagem)

			matches.append(dado[1])
			corretos.append(dado[2])
			

		media_matches, desvio_matches = desvio(matches)
		media_corretos, desvio_corretos = desvio(corretos)
		

		porcentMedio = ((media_corretos/media_matches)*100)
		arquivo.write("\n\n")
		arquivo.write("Média dos matches:  "+str(media_matches)+"\n")
		arquivo.write("Desvio Padrão dos matches:  "+str(desvio_matches)+"\n")
		arquivo.write("Média dos corretos:  "+str(media_corretos)+"\n")
		arquivo.write("Desvio Padrão dos corretos:  "+str(desvio_corretos)+"\n")
		arquivo.write("Porcentagem em relação aos valores médios:  "+str(porcentMedio)+ " %")
		print("Arquivo de texto escrito")

		Porcent_Acertos.append(porcentMedio)
		Med_matches.append(media_matches)
		Med_Corretos.append(media_corretos)
		Des_Matches.append(desvio_matches)
		Des_Corretos.append(desvio_corretos)


QuantRelacoes = 30
j=0
with open('Comparacões.csv', 'w') as csvfile:
    fieldnames = ['Nome', 'Media_Matches', 'Desvio_Padrao_Matches',  'Media_Corretos', 'Desvio_Padrao_Corretos', 'Porcentagem_Acertos']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    while(j<QuantRelacoes):
    	writer.writerow({'Nome': Nomes[j] ,'Media_Matches': Med_matches[j] ,'Desvio_Padrao_Matches': Des_Corretos[j] ,'Media_Corretos': Med_Corretos[j] ,'Desvio_Padrao_Corretos': Des_Corretos[j] ,'Porcentagem_Acertos': Porcent_Acertos[j] })
    	j+=1


# Erro ao carregar algumas célular no libreoffice
