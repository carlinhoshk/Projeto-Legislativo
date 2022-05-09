# import os module
import os
import csv
import pandas as pd
 
# folder path and destination
path_name = r'banco-fotos'

nome = []
partido = []
uf = []

df = pd.read_excel('deputado.xls') 

# loop through the directory to rename all the files
#for count, filename in enumerate(os.listdir(path_name)):
        # COLOCAR leitura e condição para, ler nomes na coluna csv e retorna em cada repetição
        



with open(df) as f:
    for i, line in enumerate(reader):
        new = line + '.png'  # new file name
        src = os.path.join(path_name, filename)  # file source
        dst = os.path.join(path_name, new)  # file destination
        # rename all the file
        os.rename(src, dst)
