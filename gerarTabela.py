#coding: utf-8
import mysql.connector
import math
import csv
from decimal import *

mydb = mysql.connector.connect(
	host = "localhost",
	user = "descritores",
	passwd = "12345678",
	database = "referencias"
)

detectores = ["fast", "harris", "orb", "shiTomasi", "star", "surf"]
descritores = ["brief" ,"brisk", "freak", "orb", "sift"]
					

with open('Comparacões2.csv', 'w') as csvfile:
    fieldnames = ['Nome', 'Media_Matches', 'Desvio_Padrao_Matches',  'Media_Corretos', 'Desvio_Padrao_Corretos', 'Porcentagem_Acertos']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for dect in detectores:
		detector = dect
		for desc in descritores:
			nomeAlg = str(dect+"_"+desc)
			mycursor = mydb.cursor()
			sql = "SELECT * FROM medias_desvios WHERE Nome = %s"
			valor = (nomeAlg, )
			mycursor.execute(sql, valor)
			result = mycursor.fetchall()
    			writer.writerow({'Nome': result[0][0] ,'Media_Matches': result[0][1] ,'Desvio_Padrao_Matches': result[0][2] ,'Media_Corretos': result[0][3] ,'Desvio_Padrao_Corretos': result[0][4] ,'Porcentagem_Acertos': result[0][5]})


