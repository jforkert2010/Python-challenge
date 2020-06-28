# Unlike lists, dictionaries store information in pairs
# ---------------------------------------------------------------
import os
import csv


election_data_csv = os.path.join("election_data.csv")

with open(election_data_csv) as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")
    # Read the header row first (skip this part if there is no header)
   csv_header = next(csvreader)
   print(f"Header: {csv_header}")
   
   candidates = {}
   candidates = dict()
   total_votes = 0
   winner_votes = 0
   for row in csvreader:
            if (row[2]) in candidates:
                candidates[row[2]]  = candidates[row[2]] + 1
            else: 
                candidates.update({row [2]:1})
            pass
            total_votes = total_votes + 1 
    
   print("Election Results")
   print("---------------------------")
   print("Total Votes:", total_votes)
output_path = os.path.join("new.csv")         
with open(output_path, 'w') as csvfile:
   csvwriter = csv.writer(csvfile, delimiter=',')
   

    # Write the second row
   csvwriter.writerow(['Name', 'Votes', 'Percentage'])  
   for key in candidates:
         percentage = candidates[key] /total_votes
         csvwriter.writerow([key,candidates[key],percentage])
         print(key,percentage,"(",candidates[key],")")
         if (int(candidates[key]) > winner_votes):
            winner_votes = candidates[key]
            winner = key
         else:
            pass
   csvwriter.writerow(['Winner:',winner,'Total Votes:', total_votes])
   
   print("-----------------------------")
   print("Winner:", winner)
   print("-----------------------------")


    # Initialize csv.writer
    
    
