#Your task is to create a Python script that analyzes the votes and calculates each of the following:
    #The total number of votes cast
    #A complete list of candidates who received votes
    #The percentage of votes each candidate won
    #The total number of votes each candidate won
    #The winner of the election based on popular vote.

# open the files for processing

import os 
import csv
# Path to file in to read
election_data = os.path.join('Resources', 'election_data.csv')
electionResults = os.path.join('Resources', 'election_data_analysis.txt')
# open file for reading
with open (election_data,'r') as file:
  csvReader = csv.reader(file, delimiter=",") # create variable to read file and separate data by delimiter
  header =next(csvReader) #move to the next row to get the header
  candidates = []
  totalVoteCount =0  #initialize variable total number of votes cast
  candidateVoteCount={}  # initialize variable total number of votes per candidate
  winnerCount= 0 # variable that holds the winner count
  winner = 0
  for row in csvReader :
      totalVoteCount +=1
      # check if candidate is in the list of candidates
      if row[2] not in candidates: # if the flavor is not in the list add to the list
        candidates.append(row[2])  # if candidate not in list, add their name to the list
        candidateVoteCount[row[2]] = 1  # add a vote to the candidate vote counter for candidate that was added
      else:
        candidateVoteCount[row[2]] += 1  #candidate was already on the list, add a vote to their counter
voteResults ="" 
for candidate in candidates:  # iterate through the candiates in list candidates
    votes = candidateVoteCount.get(candidate) # get the vote counte per candidate
    votePercentage =(float (votes) /float (totalVoteCount)) * 100  # calculate percentage of vote 
    voteResults += f"{candidate}: {votePercentage: .3f}%  ({votes})\n"
    if votes > winnerCount:
        winnerCount = votes
        winner = candidate
candidateOutput = f"Winner: {winner} \n"
output = (
        f"\nElection Results\n"
        f"----------------------------------\n"
        f"Total Votes: {totalVoteCount} \n"
        f"----------------------------------\n"
        f"{voteResults}"
        f"----------------------------------\n"
        f"{candidateOutput}"
        f"-----------------------------------\n"
        )
print (output)
