

# importing the module
import csv
 
# open the file in read mode
filename = open('nomes.csv', 'r')
 
# creating dictreader object
file = csv.DictReader(filename)
 
# creating empty lists
month = []
totalprofit = []
totalunit = []
 
# iterating over each row and append
# values to empty list
for col in file:
    month.append(col['Nome Parlamentar'])
    totalprofit.append(col['Partido'])
    totalunit.append(col['UF'])
 
# printing lists
print('Month:', month)
print('Moisturizer:', totalprofit)
print('Total Units:', totalunit)
