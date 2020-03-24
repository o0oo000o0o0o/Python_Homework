import os
import csv

budget_data = "budget_data.csv"

# with open(budget_data) as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=",")

#     csv_header = next(csvfile)
#     print(f'Header: {csv_header}')

#  Finding Total number of months in the dataset

total = 0 

with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    print(f'Header: {csv_header}')

    for row in csvreader:
        for months in row:
            total = total + int(months[1])
            total_lines = sum(1 for line in csvfile)
            print(f'There are a total of {total_lines} line in this file')
            print(total)

# ------------------------------------------------------------------------------------

# def Total_Months(months):
#     with open(budget_data) as csvfile:
#         total_lines = sum(1 for line in csvfile)
#         print(f'There are a total of {total_lines} line in this file')


#  Net total amount of "Profit/Losses" over entire period

#  Average of changes in "Profit/Losses" over entire period

#  Greatest Increase in profits (date & amount) over entire period

#  Greatest decrease in losses (date & amount) over entire period

#  Exporting Textfile

# output_file = os.path.join("PyBank_Analysis_Report.csv")
# with open(output_file, "w") as datafile: 
#     writer = csv.writer(datafile)
#     writer.writerow
