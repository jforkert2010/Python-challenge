import os
import csv


budget_data_csv = os.path.join("budget_data.csv")

# def average ()
# Open and read csv
with open(budget_data_csv) as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
   csv_header = next(csvreader)
   print(f"Header: {csv_header}")
   
   total = 0
   number_of_months = 0
   greatest_increase = 0
   greatest_decrease = 0
   former_value = 0
   total_change = 0
   change = 0
   
    #Read through each row of data after the header
   for row in csvreader:
        #print("in the loop")
   
      if int(row[1]) > greatest_increase:
           greatest_increase = int(row[1])
           month_increase = row[0]
           print("greatest_increase")
      else: 
        #if int(row[1]) < greatest_decrease:
         greatest_decrease = int(row[1])
         month_decrease = row[0]
         print("greatest_decrease")
         pass  
      if int (number_of_months) > 1:
         change = former_value - int(row[1])
         print(change)
         pass   
      print("stiil in loop")  
      total = total + int(row[1])
      former_value = int(row[1])
      former_value = int (row[1])
      total_change = total_change+change 
      number_of_months = number_of_months + 1
   average_change = total_change / number_of_months
   print("Financial Analysis")
   print("-------------------------------")
   print("Total Months: ", number_of_months)
   print("Total:", total)
   print("Average Change :", average_change)
   print("Greatest Increase in Profits:", month_increase ," ", greatest_increase)
   print("Greatest Decrease in Profits:", month_decrease ," ", greatest_decrease)
   
         
      
        # Convert row to float and compare to grams of fiber
        #if float(row[7]) >= 5:
        
            
 
