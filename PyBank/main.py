import os
import csv
total_months = 0
Net_Total = 0
Average = 0
sum = 0

# Creating a path for the file
csvpath= os.path.join("Resources","budget_data.csv")

# check if we found the file
found=False

# Open the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# Skip the header
    csv_header = next(csvfile)
   
# loop through the date column  
    for row in csvreader:
        total_months = total_months + 1
      
# Get the net total of profit/losses
        Net_Total = Net_Total+ int(row[1])

 # Get the average change

    
print ("Financial Analysis")
print ("..........................")
print ("Total Months :" ,(total_months))
print("Total : $",Net_Total)




  




        
