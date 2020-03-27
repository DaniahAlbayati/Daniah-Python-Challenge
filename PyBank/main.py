import os
import csv

# Creating a path to collect the data from the Resource Folder
Pybank_csv= os.path.join("..","Resources","budget_data.csv")

# Read the budget_data file as CVS file
with open (Pybank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
# loop through the date data
       
    for row in csvreader:
     # add total months
     Total_Months.append(row[1])
        
 
# Get the Financial Analysis and the line underneath it as per the text example
print ("Financial Analysis")
print ("....................")
print ( "Total Months : {row_count}")


        




 