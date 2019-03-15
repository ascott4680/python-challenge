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

#--Calculate other winners




#--Output to Screen
print("")
print("Election Results")
print("---------------------------")
print(f"Total Votes: ", + sumvotes)
print("---------------------------")



print("---------------------------")
print(f"Winner: " + str(winner))
print("---------------------------")