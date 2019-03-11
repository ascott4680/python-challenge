#--PyBank
#--Andrew Scott Mar. 2019
#-------------------------

#--import helpers
import os
import csv

#--Set variable values
#monthcount = 0
#total = 0
#prevtotal = 0
change = 0

#--Third times a charm, going to cram it all into lists and see what happens (apparently this works, plus I can Min/Max/LEN this)
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


#--second loop through the entire list of revenue to calculate change
for i in range(1,len(revenue)):
    revenuechange.append(revenue[i] - revenue[i-1])
    change = sum(revenuechange)/len(revenuechange)

    #--Getting Max/Min revenue change dates via index of my lists
    datechangemax = revenuechange.index(max(revenuechange))
    datechangemin = revenuechange.index(min(revenuechange))

    #adding one to compensate for starting at zero (helper to match dates)
    datechangemax = datechangemax + 1
    datechangemin = datechangemin + 1

#--format change as decimal with two places (I don't recall this from class, thanks Google)
#avgchange = int(change)
from decimal import Decimal, ROUND_DOWN
avgchange = Decimal(str(change)).quantize(Decimal('.01'), rounding=ROUND_DOWN)


print("Average Change: $",(avgchange))
print("Greatest Increase in Profits: ", dates[datechangemax] ,"($", max(revenuechange),")")
print("Greatest Decrease in Profits: ", dates[datechangemin] ,"($", min(revenuechange),")")


#--------------------------------------------------------------------
#--Let's write this to an output file
#--------------------------------------------------------------------

text_file = open("Financial Analysis.txt", "w")
text_file.write("Financial Analysis") 
text_file.write("\n")
text_file.write("-------------------------")
text_file.write("\n")
text_file.write("Total Months: ")
text_file.write(str(len(dates)))
text_file.write("\n")
text_file.write("Total: $")
text_file.write(str(sum(revenue)))
text_file.write("\n")
text_file.write("Average Change: $")
text_file.write(str(avgchange))
text_file.write("\n")
text_file.write("Greatest Increase in Profits: ")
text_file.write(str(dates[datechangemax]))
text_file.write(" ")
text_file.write("($")
text_file.write(str(max(revenuechange)))
text_file.write(")")
text_file.write("\n")
text_file.write("Greatest Decrease in Profits: ")
text_file.write(str(dates[datechangemin]))
text_file.write(" ")
text_file.write("($")
text_file.write(str(min(revenuechange)))
text_file.write(")")
text_file.write("\n")
text_file.close()
#--End