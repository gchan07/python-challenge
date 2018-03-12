#Modules
import os
import csv

voterid = []
candidate = []
unique_candidate =[]
vote_unique_candidate = [] 

# Set path for files
filepath = os.path.join("raw_data", "election_data_2.csv")

# Open the CSV
with open(filepath, newline="") as csvfile:
	poll = csv.reader(csvfile, delimiter=",")
	for row in poll: 
		voterid.append(row[0])
		candidate.append(row[2])

votes =(len(voterid))-1

print("Election Results")
print("----------------")
print("Total Votes: " + str(votes))
print("----------------")

#sort list of candidates
candidate.sort()
#print(candidate)

#find unique list of candidates

for i in range(1,(len(candidate)-1)):
	if (candidate[i] != candidate[i+1]) or (i ==(len(candidate)-2)):
		unique_candidate.append(candidate[i])		
	
#print(unique_candidate)

for name in range(0,len(unique_candidate)):
	temp_count = candidate.count(unique_candidate[name])
	vote_unique_candidate.append(temp_count)
	print(unique_candidate[name]+": "+ str((vote_unique_candidate[name]/votes)*100) +"%" + " (" + str(vote_unique_candidate[name]) + ")")

winner_max = max(vote_unique_candidate)
winner_index = vote_unique_candidate.index(winner_max)
winner_name = unique_candidate[winner_index]

print("----------------")
print("Winner: " + winner_name)


	

