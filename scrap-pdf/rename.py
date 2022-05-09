import pandas as pd

read_file = pd.read_excel (r'deputado.xls')
read_file.to_csv (r'nomes.csv', index = None, header=True)
