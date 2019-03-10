#--PyBank
#--Andrew Scott Mar. 2019
#-------------------------

#--Values to write to textfile - monthcount,

#--import helpers
import os
import csv

#--Set variable values
total = 0
previoustotal = 0
newtotal = 0


#--Set path to PyBank CSV -Note that 'Resources' lies in the same directory, not one up as usual to keep my file structure clean
pybankcsv = os.path.join('Resources', 'budget_data.csv')

#--Opening CSV for Read
with open(pybankcsv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #Skipping my header row
    row = next(csvreader)
    
    #Counting my totals
    for row in csvreader:
        total += int(row[1])


with open(pybankcsv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #Skipping my header row
    row = next(csvreader)
    
    #Counting my totals
    for row in csvreader:
        monthcount = sum(1 for row in csvreader) 
        monthcount = monthcount +1
 




print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {monthcount}")
print(f"Total: ${total}")