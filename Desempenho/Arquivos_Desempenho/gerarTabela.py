# coding: utf-8
import csv
with open('Tempo_Memoria_Utilizado.csv', 'w') as csvfile:
    fieldnames = ['Nome', 'Tempo(s)',  'Memoria(Mb)']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    f1 = open("totalMemoria.txt", 'r')
    dadosM = f1.readlines()
    linhasM = []
    for infM in dadosM:
    	linhasM.append(infM.split()) 
    f2 = open("totalTempo.txt", 'r')
    dadosT = f2.readlines()
    linhasT = []
    for infT in dadosT:
    	linhasT.append(infT.split())
    i=1
    while(i<len(linhasM)):
		writer.writerow({'Nome': linhasT[i][0] ,'Tempo(s)': linhasT[i][1] ,'Memoria(Mb)': linhasM[i][1]})
		i+=1