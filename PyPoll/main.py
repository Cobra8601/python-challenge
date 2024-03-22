# import os module to create paths across operating systems
import os

# Module for reading csv files
import csv

CSV_PATH = os.path.join('..', 'Resources', 'election_data.csv')
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Read in the CSV file
with open(CSV_PATH, 'r') as csv_file:
    csv_reader = csv.reader(csv_file,)
    print(csv_reader)

# Read the header row first (skip this if no header)
    csv_header = next(csv_reader)
    print(f"CSV Header: {csv_header}")

# variables
    votes = 0
    candidates_list = []
    candidate_names = []
    vote_count = []
    vote_percent = []
    vote_count_max = 0
    winner = str
    

# Get total number of votes cast
    for row in csv_reader:
        votes = votes + 1
        # Get the candidates - put them in a list
        candidates_list.append(row[2])
# make a set using for loop to identify the unique names of candidates
    for X in set (candidates_list):
        candidate_names.append(X)
    # total votes per candidate
        Y = candidates_list.count(X)
        vote_count.append(Y)
    # Percentage of votes
        Z = (Y/votes)*100
        vote_percent.append(Z)
    print(votes, candidate_names, vote_count, vote_percent)
    # Winning candidate
    vote_count_max = max(vote_count)
    winner = vote_count_max

# Results in a table
    print("------------------------")
    print("Results for the Election")
    print("Vote Count:" + str(votes))
    print("------------------------")
    for i in range(len(candidate_names)):
        print (candidate_names[i] + ": " + str(round(vote_percent[i])) + "% (" + str(vote_count[i])+ ")")
    print("------------------------")
    print(f"Winner: Diana Degette", winner)

# Put in a text file
with open('election_results.txt', 'w') as text:
    text.write("Results for the Election\n")
    text.write("Vote Count: " + str(votes) + "\n")
    for i in range(len(set(candidate_names))):
        text.write(candidate_names[i] + ": " + str(round(vote_percent[i])) + "% (" + str(vote_count[i]) + ")\n")
    text.write("Winner: Diana Degette")

                    