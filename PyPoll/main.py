# The total number of votes cast
import os
import csv

filename_ = ('/Users/carlysethomas/Downloads/python-challenge/Resources/election_data.csv')

with open (filename_, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvfile) 

    total_votes = len(list(csvreader))
   

# A complete list of candidates who received votes 
list_of_candidates = []

with open (filename_, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvfile) 

    for candidates in csvreader:
        if candidates[2] not in list_of_candidates:
            list_of_candidates.append(candidates[2])


# The percentage of votes each candidate won
votes_Khan = 0
votes_Correy = 0
votes_Li = 0
votes_Tooley = 0

with open (filename_, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvfile) 

    def votes(voter_data):
        totals_votes = int(voter_data[3])
    
    for name in csvreader:
        if name[2] == "Khan":
            votes_Khan = (votes_Khan + 1)
        elif name[2] == "Correy":
            votes_Correy = (votes_Correy + 1)
        elif name[2] == "Li":
            votes_Li = (votes_Li + 1)
        elif name[2] == "O'Tooley":
            votes_Tooley = (votes_Tooley + 1)

total_votes_Khan = votes_Khan
total_votes_Correy = votes_Correy
total_votes_Li = votes_Li
total_votes_Tooley = votes_Tooley

percent_Khan = round((votes_Khan / total_votes)*100)
percent_Correy = round((votes_Correy / total_votes)*100)
percent_Li = round((votes_Li / total_votes)*100)
percent_Tooley = round((votes_Tooley / total_votes)*100)


# The total number of votes each candidate won
votes_Khan = 0
votes_Correy = 0
votes_Li = 0
votes_Tooley = 0

with open (filename_, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvfile) 

    for name in csvreader:
        if name[2] == "Khan":
            votes_Khan = (votes_Khan + 1)
        elif name[2] == "Correy":
            votes_Correy = (votes_Correy + 1)
        elif name[2] == "Li":
            votes_Li = (votes_Li + 1)
        elif name[2] == "O'Tooley":
            votes_Tooley = (votes_Tooley + 1)

total_votes_Khan = votes_Khan
total_votes_Correy = votes_Correy
total_votes_Li = votes_Li
total_votes_Tooley = votes_Tooley


# The winner of the election based on popular vote 
print("Election Results")
print("--------------------------------------")
print(f'Total Number Of Votes = {total_votes}')
print("--------------------------------------")
print(f'{list_of_candidates[0]}:  Percentage of Total Votes = {percent_Khan}%  Total Votes for Khan = {total_votes_Khan}')
print(f'{list_of_candidates[1]}:  Percentage of Total Votes = {percent_Correy}% Total Votes for Correy = {total_votes_Correy}')
print(f'{list_of_candidates[2]}:  Percentage of Total Votes = {percent_Li}% Total Votes for Li = {total_votes_Li}')
print(f'{list_of_candidates[3]}:  Percentage of Total Votes = {percent_Tooley}% print Total Votes for O\'Tooley = {total_votes_Tooley}')
print("--------------------------------------")
percents = []
percents.append(percent_Khan)
percents.append(percent_Correy)
percents.append(percent_Li)
percents.append(percent_Tooley)

grouped_list = list(zip(list_of_candidates,percents))

for winner in grouped_list:
    if winner[1] == max(percents):
        print(f'The Winner Of The Election Was {winner[0]}')
print("--------------------------------------")

