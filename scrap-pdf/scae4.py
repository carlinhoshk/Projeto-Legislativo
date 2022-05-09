import csv

with open('nomes.csv') as csvfile:
    MonthlyRevenue = csv.DictReader(csvfile, delimiter=",", quotechar = '"')
    
for row in MonthlyRevenue:
    print (f"For the month {row['MONTH(purchases.date)']} the total revenue was {row['total_revenue_per_month']}."