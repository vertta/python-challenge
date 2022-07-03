## create a Python script that analyzes the records to calculate each of the following values:
  # The total number of months included in the dataset
  # The net total amount of "Profit/Losses" over the entire period
  # The changes in "Profit/Losses" over the entire period, and then the average of those changes
  # The greatest increase in profits (date and amount) over the entire period
  # The greatest decrease in profits (date and amount) over the entire period

import os
import csv
# Path to file in to read 
budgetdata_csv = os.path.join('Resources', 'budget_data.csv')
profitLossAnalysis = os.path.join('Resources', 'profit_loss_results.txt')
# open file for reading 
with open (budgetdata_csv,'r') as file:

# use csv.reader() function to open the file
  csvReader = csv.reader(file, delimiter=",") # create variable to read file and separate data by delimiter
  totalProfitLoss =0  #initialize variable total months
  totalMonths = 0  # initialize variable total months
  header =next(csvReader) # move to the next row in the file, ignore the header
  firstRow = next(csvReader) # get the first row of data after the header
  previousProfitLoss = int(firstRow[1]) # access the first profit/lost row of data
  totalProfitLoss += int(firstRow[1])
  totalMonths += 1          # add one to count 
  monthlyProfitLoss = [] # initialize an empty list to hold monthly change
  months = [] 
  greatestMonthlyIncrease = ["",0] # holds the greatest Monthly Increase 
  greatestMonthlyDecrease = ["",0] # holds the greatest Monthly Decrease

  for row in csvReader:   # look through file

      totalMonths += 1          # add one to count for total months
      # get previous profit/loss for previous month 
      netChange = int(row[1]) - previousProfitLoss

      totalProfitLoss += int(row[1])
      # add to the nextChange
      monthlyProfitLoss.append(netChange)
    # add first month that a change ocurred, month is in index 0
      months.append(row[0])
      # update the previous monthly profit/loss
      previousProfitLoss  =  int(row[1])
    # calculate the average change, once calculate monthly profit/loss 
    # take the length of monthly profitloss /length of  the monthly profit loss 
      averageProfitLoss = sum(monthlyProfitLoss)/len(monthlyProfitLoss)

# use loop to calucate the index of the greatest increase and decrease 
  for i in range(len(monthlyProfitLoss)):
    #calculate greatest increase and decrease 
     # if  montlyProfitLoss is greater than greatestIncrease assign that vakue to greateastIncrease
     if ( monthlyProfitLoss[i] > greatestMonthlyIncrease [1]): 
           greatestMonthlyIncrease[1] = monthlyProfitLoss[i]  # assign value of greatest increase 
           greatestMonthlyIncrease[0] = months[i]   # assign the month of the greatest increase to the month variable 

    # if  montlyProfitLoss is greater than greatestDecrease assign that vakue to greateastdecrease
     if ( monthlyProfitLoss[i] < greatestMonthlyDecrease [1]): 
           greatestMonthlyDecrease[1] = monthlyProfitLoss[i]  # assign value of greatest decrease 
           greatestMonthlyDecrease[0] = months[i]   # assign the month of the greatest decrease to the month variable 
# print results of greatest increase and decrease

# Write result to a file 
results = (
  f"Finanical Analysis\n"
  f"----------------------------------\n"
  f"Total Months: {totalMonths}\n"
  f"Total: ${totalProfitLoss}\n"
  f"Average Change: ${averageProfitLoss:.2f}\n"
  f"Greatest Increase in Profits: {greatestMonthlyIncrease[0]} (${greatestMonthlyIncrease[1]})\n"
  f"Greatest Decrease in Profits: {greatestMonthlyDecrease[0]} (${greatestMonthlyDecrease[1]})\n"
  )
# print the value in results to console
print (results)

# write results to a text file 
with open (profitLossAnalysis,"w") as textfile:
    textfile.write(results)
