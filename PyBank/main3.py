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

#--Third time around, going to cram it all into lists and see what happens
dates = []
revenue = []
revenuechange = []

#--Set path to PyBank CSV -Note that 'Resources' lies in the same directory, not one up as usual to keep my file structure clean
pybankcsv = os.path.join('Resources', 'budget_data.csv')

#--Opening CSV for Read
with open(pybankcsv, 'r') as csvfile:

    #-- Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #--Skipping my header row
    next(csvreader)


    #--Pushing data to lists
    for row in csvreader:
        revenue.append(int(row[1]))
        dates.append(row[0])
        
        





print("Financial Analysis")
print("-------------------------")
print("Total Months: ", len(dates))
print("Total: $", sum(revenue))
