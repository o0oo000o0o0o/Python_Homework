import os
import csv
import statistics

poll_df  = "election_data.csv"
candidate_list = []



with open(poll_df) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    for row in csvreader:
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
    print(f'Here is the list of candidates: {candidate_list}')

with open(poll_df) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    khan_votes = 0
    Correy_votes = 0
    Li_votes = 0
    OTooley_votes = 0   
    for row in csvreader:
        if row[2] == candidate_list[0]:
            khan_votes += 1
        elif row[2] == candidate_list[1]:
            Correy_votes += 1
        elif row[2] == candidate_list[2]:
            Li_votes += 1
        elif row[2] == candidate_list[3]:
            OTooley_votes += 1
total_votes = khan_votes + Correy_votes + Li_votes + OTooley_votes

print("Election Results")
print("-----------------------------------------------------------------------")
print(f'Total Votes: {total_votes}')
print("-----------------------------------------------------------------------")
print(f'Khan: {round((khan_votes/total_votes)*100,3)}% ({khan_votes})')
print(f'Correy: {round((Correy_votes/total_votes)*100,3)}% ({Correy_votes})')
print(f'Li: {round((Li_votes/total_votes)*100,3)}% ({Li_votes})')
print(f"O'Tooley: {round((OTooley_votes/total_votes)*100,3)}% ({OTooley_votes})")
print("-----------------------------------------------------------------------")

if khan_votes > Correy_votes and khan_votes > Li_votes and khan_votes > OTooley_votes:
    winner = "Khan"
    # print("Winner: Khan")
elif Correy_votes > khan_votes and Correy_votes > Li_votes and Correy_votes > OTooley_votes:
    winner = "Correy"
    # print("Winner: Correy")
elif Li_votes > khan_votes and Li_votes > Correy_votes and Li_votes > OTooley_votes:
    winner = "Li"
    # print("Winner: Li")
elif OTooley_votes >= khan_votes and OTooley_votes >= Li_votes and OTooley_votes >= Correy_votes:
    winner = "O'Tooley"
    # print("Winner: O'Tooley")
print(f'Winner: {winner}')
print("-----------------------------------------------------------------------")

output_path = 'Election Results.txt'

with open(output_path, 'w', newline ='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["-----------------------------------------------------------------------"])
    csvwriter.writerow([f'Total Votes: {total_votes}'])
    csvwriter.writerow(["-----------------------------------------------------------------------"])
    csvwriter.writerow([f'Khan: {round((khan_votes/total_votes)*100,3)}% ({khan_votes})'])
    csvwriter.writerow([f'Correy: {round((Correy_votes/total_votes)*100,3)}% ({Correy_votes})'])
    csvwriter.writerow([f'Li: {round((Li_votes/total_votes)*100,3)}% ({Li_votes})'])
    csvwriter.writerow([f"O'Tooley: {round((OTooley_votes/total_votes)*100,3)}% ({OTooley_votes})"])
    csvwriter.writerow(["-----------------------------------------------------------------------"])
    csvwriter.writerow([f'Winner: {winner}'])
    csvwriter.writerow(["-----------------------------------------------------------------------"])