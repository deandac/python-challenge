import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
#we are skipping the first row because it doesn't have data we need so we used next(csvreader)
    header = next(csvreader)
    firstrow = next(csvreader)
    total_votes = 1

    

