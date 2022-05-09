import os
import pandas as pd

path_name = r'banco-fotos'
df = pd.read_excel('deputado.xls')
linha_inteira  = df['Nome Parlamentar'].tolist()
print(linha_inteira)



for i, line in enumerate(linha_inteira):
    new = line + '.png'
    src = os.path.join(path_name)
    dst = os.path.join(path_name, new)
    os.rename(src, dst)


