#--PyBank
#--Andrew Scott Mar. 2019
#-------------------------

#--Values to write to textfile - monthcount,

#--import helpers
import os
import csv

#--Set path to PyBank CSV -Note that 'Resources' lies in the same directory, not one up as usual to keep my file structure clean
pybankcsv = os.path.join('Resources', 'budget_data.csv')

#--Opening CSV for Read
with open(pybankcsv, 'r') as csvfile:

    #-- Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #--Skipping my header row
    row = next(csvreader)

