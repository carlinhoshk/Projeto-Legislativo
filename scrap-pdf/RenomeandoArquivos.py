import os
import csv
 
# abra o arquivo csv
with open('nomes.csv', 'r') as csvfile:
    # crie um leitor csv
    reader = csv.reader(csvfile)
       # para cada linha do arquivo csv
    for row in reader:
        nome = row[0]    
       # pegue o partido do arquivo
        partido = row[1]
       # pegue o estado
        estado = row[2]

        print(nome.replace(" ", ""))

        # pegue nome de todos arquivos da pasta banco-fotos
        print("{}-{}-{}".format(nome.replace(" ", "_"), partido, estado))


       # renomeie o arquivo
       # os.rename('banco-fotos/' + nome, 'banco-fotos-renomeados/'nome.replace(" ", "")+"-"+partido + "-"+ estado'.jpg')
       # mostre o nome do arquivo
           


