import os
import csv

# Path to collect data from the Resources folder
csvpath= os.path.join("Resources","election_data.csv")

# set my variables
total_votes = 0
candidate_list = []
candidate_votes_list = {}
candidate_percentages_list = {}

# check if we found the file
found=False

# Open the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header
    csv_header = next(csvfile)

    # get the total votes  
    for row in csvreader:
        total_votes = total_votes + 1

        # check if the candidate is in the candidate list and then create a list
        candidate= (row[2])
        if candidate not in candidate_list:
            candidate_list.append(row[2])
            candidate_votes_list[candidate] = 1

        else: # candidate is in list
            candidate_votes_list[candidate] = candidate_votes_list[candidate] + 1

    # Get the vote percentage
    for candidate in candidate_list:
        candidate_percentages_list[candidate] = (float(candidate_votes_list[candidate]) / float(total_votes) * 100)
        
winner = max(candidate_votes_list, key=candidate_votes_list.get)

print ("Election Results")
print (".......................")
print ("Total Votes :",(total_votes))
print("........................")

for candidate in candidate_list:
    print(candidate + ": " +str(candidate_percentages_list[candidate]) + "%   (" + str(candidate_votes_list[candidate])+")")

print("........................")
print("Winner: ", winner)
print("........................")




