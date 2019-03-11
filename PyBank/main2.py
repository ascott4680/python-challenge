#--PyBank
#--Andrew Scott Mar. 2019
#-------------------------

#--Values to write to textfile - monthcount,

#--import helpers
import os
import csv

#--Set variable values
monthcount = 0
total = 0
prevtotal = 0
change = 0

#--Set path to PyBank CSV -Note that 'Resources' lies in the same directory, not one up as usual to keep my file structure clean
pybankcsv = os.path.join('Resources', 'budget_data.csv')

#--Opening CSV for Read
with open(pybankcsv, 'r') as csvfile:

    #-- Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #--Skipping my header row
    next(csvreader)


    #--math
    for row in csvreader:
        
        #--count my months
        monthcount = monthcount +1

        #--Set previous sum so I can find the difference
        prevtotal = total - prevtotal

        #--Sum totals
        total += int(row[1])






        #--revenue change
        #change = total - prevtotal














print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {monthcount}")
print(f"Total: ${total}")
print(prevtotal)