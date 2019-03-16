#----------------------
#--Andrew Scott PyPoll
#-- March 2019
#---------------------

# Dependencies
import pandas as pd
import numpy as np
from collections import Counter


# Store filepath in a variable
election_import = "Resources/election_data.csv"

# Read our Data file with the pandas library
# Not every CSV requires an encoding, but be aware this can come up
election_df = pd.read_csv(election_import, encoding="UTF-8")

sumvotes = election_df["Voter ID"].count()

#--Find winner
winner = election_df.groupby('Candidate')['Voter ID'].count().idxmax()

avg = election_df.groupby(['Candidate']).count()
#avg.head(10)

#--Getting percentage of votes into dataframe
avg["Percent of Votes"] = avg["Voter ID"] / sumvotes * 100

#avg

#--Reorganizing my columns to fit output
output = avg[["Percent of Votes","Voter ID"]]

#output.head()
#renaming my columns
renamed_df = output.rename(columns={"Percent of Votes":"Percent of Votes", "Voter ID" : "Sum of Votes"})

#sorting by Sum of Votes
final_output = renamed_df.sort_values("Sum of Votes", ascending=False)

#final_output.head()


#--Output to Screen
print("")
print("Election Results")
print("---------------------------")
print(f"Total Votes: ", + sumvotes)
print("---------------------------")
print(final_output)
print("---------------------------")
print(f"Winner: " + str(winner))
print("---------------------------")

#--------------------------------------------------------------------
#--Let's write this to an output file
#--------------------------------------------------------------------

text_file = open("PyPoll Results.txt", "w")
text_file.write("") 
text_file.write("\n")
text_file.write("Election Results")
text_file.write("\n")
text_file.write("-------------------------")
text_file.write("\n")
text_file.write("Total Votes: ")
text_file.write(str(sumvotes))
text_file.write("\n")
text_file.write("-------------------------")
text_file.write("\n")
text_file.write(str(final_output))
text_file.write("\n")
text_file.write("-------------------------")
text_file.write("\n")
text_file.write("Winner: ")
text_file.write(str(winner))
text_file.write("\n")
text_file.write("-------------------------")
text_file.write("\n")
text_file.close()
#--End