#coding: utf-8

import mysql.connector
import math

# A partir deste script será possível realizar a criação de arquivos de textos relacionado aos dados de precisão dos algoritmos
def escrever(result, detector, nomeSalvar, dadosComputados):
	arquivo = open("arquivosTxt/detector_"+detector+"/"+nomeSalvar,'w')
	arquivo.write("                     "+nomeSalvar)
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
		
	arquivo.write("\n\n")
	arquivo.write("Média dos matches:  "+str(dadosComputados[0][1])+"\n")
	arquivo.write("Desvio Padrão dos matches:  "+str(dadosComputados[0][2])+"\n")
	arquivo.write("Média dos corretos:  "+str(dadosComputados[0][3])+"\n")
	arquivo.write("Desvio Padrão dos corretos:  "+str(dadosComputados[0][4])+"\n")
	arquivo.write("Porcentagem em relação aos valores médios:  "+str(dadosComputados[0][5])+ " %")
	print("Arquivo de texto escrito")


mydb = mysql.connector.connect(
	host = "localhost",
	user = "descritores",
	passwd = "12345678",
	database = "referencias"
)
detectores = ["fast", "harris", "orb", "shiTomasi", "star", "surf"]
descritores = ["brief" ,"brisk", "freak", "orb", "sift"]


for dect in detectores:
	nomeDetect = dect
	for desc in descritores:
		nomeAlg = str(dect+"_"+desc)
		mycursor = mydb.cursor()

		
		sql = "SELECT * FROM "+nomeAlg
		sql2 = "SELECT * FROM medias_desvios WHERE Nome = %s"
		valor2 = (nomeAlg, )
		mycursor.execute(sql)
		result1 = mycursor.fetchall()
		
		mycursor.execute(sql2, valor2)
		dadosComputados = mycursor.fetchall()
		escrever(result1, nomeDetect, nomeAlg, dadosComputados)
