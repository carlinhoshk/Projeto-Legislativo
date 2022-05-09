import pandas as pd

df = pd.read_excel('deputado.xls') # can also index sheet by name or fetch all sheets

for names in name:
    mylist = df['Nome Parlamentar'].tolist()
    mylist2 = df['Partido'].tolist()
    print(mylist, mylist2)
