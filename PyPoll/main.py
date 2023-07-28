import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
#we are skipping the first row because it doesn't have data we need so we used next(csvreader)
    header = next(csvreader)
    firstrow = next(csvreader)
    print(firstrow)
    total_votes = 1
    candidates = {}
    winner_votes = 0
    winner_candidate = ""

    # Loop through the data
    for row in csvreader:
        total_votes += 1

        candidate = row[2]
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1


# Print results

print("Election Results")        
print(f"Total Votes: {total_votes}")
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
    if votes > winner_votes:
        winner_votes = votes
        winner_candidate = candidate
print(f"Winner: {winner_candidate}")


# Export results to text file
output_directory = "output"
os.makedirs(output_directory, exist_ok=True)


output_file = os.path.join("output", "election_results.txt")
with open(output_file, "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        txtfile.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    txtfile.write(f"Winner: {winner_candidate}\n")

print("Analysis exported to 'election_results.txt'.")


