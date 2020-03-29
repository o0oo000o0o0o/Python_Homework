import os
import csv
import statistics

budget_df  = "budget_data.csv"
budget_df

def average (numbers):
    total = 0.0
    for number in numbers:
        total += number
    find_average = total/len(numbers)
    return find_average
        

months = [] #Total number of months
total = [] #total value of all the months added together 
monthly_changes =[] #list of all values for each month

with open(budget_df) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    for row in csvreader:
        months.append(row[0])
        total.append(row[1])
        monthly_changes.append(int(row[1]))
    amount_months = len(months)
    print(f'Total Months: {amount_months}')
    
    total_value = 0
    for values in total:
        total_value += int(values)
    print(f'Total: ${total_value}')

    net_change = [j-i for i,j in zip(monthly_changes[:-1], monthly_changes[1:])]
    print(f'Average Change: ${round(average(net_change),2)}')
    net_change.sort(reverse=True)
    
    print(f'The greatest increase in profits: ${net_change[0]}')
    print(f'The greatest decrease in profits: ${net_change[len(net_change)-1]}')

output_path = 'Financial Analysis.txt'

with open(output_path, 'w', newline ='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(["------------------------------------------------------"])
    csvwriter.writerow([f'Total Months: {amount_months}'])
    csvwriter.writerow([f'Total: ${total_value}'])
    csvwriter.writerow([f'Average Change: ${round(average(net_change),2)}'])
    csvwriter.writerow([f'The greatest increase in profits: ${net_change[0]}'])
    csvwriter.writerow([f'The greatest decrease in profits: ${net_change[len(net_change)-1]}'])
    