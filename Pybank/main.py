import os
import csv

#Part 2
net_change_list = []
net_total = 0
average_change = 0
csvpath = os.path.join("Resources", "budget_data.csv")

total_months = 0

with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)
    firstrow = next(csvreader)
    print(firstrow)
    total_months = 1
#Part 2
    net_total = int(firstrow[1])

#Part3
    previous_profit_loss = int(firstrow[1])
    for row in csvreader:
        total_months = total_months + 1
        net_total = net_total + int(row[1])
        net_change = int(row[1]) - previous_profit_loss
        net_change_list.append(net_change)
        previous_profit_loss = int(row[1])

average_change = sum(net_change_list)/ len(net_change_list)
print(total_months)
print(net_total)
print(average_change)