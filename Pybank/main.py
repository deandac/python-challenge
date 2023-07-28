import os
import csv

#Part 2
net_change_list = []
net_total = 0
average_change = 0
csvpath = os.path.join("Resources", "budget_data.csv")

total_months = 0
greatest_increase_amount = 0
greatest_increase_month = ""
greatest_decrease_amount = 0
greatest_decrease_month = ""
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)
    firstrow = next(csvreader)
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
        if net_change > greatest_increase_amount:
            greatest_increase_amount = net_change
            greatest_increase_month = row[0]
        if net_change < greatest_decrease_amount:
            greatest_decrease_amount = net_change
            greatest_decrease_month = row[0]
# Part 4
# Initialize variables to track the greatest increase in profits

#Part 5
# Initialize variables to track the greatest decrease in profits

average_change = sum(net_change_list)/ len(net_change_list)
print("Financial Analysis")
print(total_months)
print(net_total)
print(average_change)

print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_amount})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_amount})")


# Export results to a text file
output_directory = "output"
os.makedirs(output_directory, exist_ok=True)

output_file = os.path.join("output", "financial_analysis.txt")
with open(output_file, "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_total}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_amount})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_amount})\n")

print("Analysis exported to 'financial_analysis.txt'.")