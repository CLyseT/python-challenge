# Total number of months
import os      
import csv     

filename = ('/Users/carlysethomas/Downloads/python-challenge/Resources/budget_data.csv')

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvfile)

    lines = len(list(csvreader))
    

# Net total of "Profit/Losses" over the entire period
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvfile)    
    
    total = sum(int(r[1]) for r in csv.reader(csvfile))
    
            
# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
# Convert the csvfile to a list - defined as total_profits
with open(filename, 'r') as total_profits:
    csvreader_2 = csv.reader(total_profits)
    
    next(csvreader_2) 
    profits = []
    date = []
    difference = []
    
    for row in csvreader_2:
       profits.append(float(row[1]))
       date.append(row[0])
    
    for i in range(1, len(profits)):
        difference.append(profits[i] - profits[i-1])
        average_difference = round(sum(difference)/len(difference))

print("Financial Analysis")
print("------------------------------")
print(f'Total Months = {lines}')
print(f'Net Total = ${total}')
print(f'Average Revenue Change: ${round(average_difference)}')


# The greatest increase in profits (date and amount) over the entire period
max_difference = max(difference)
max_difference_date = str(date[difference.index(max(difference))])

# The greatest decrease in profits (date and amount) over the entire period
min_difference = min(difference)
min_difference_date = str(date[difference.index(min(difference))])

print(f'Greatest Increase in Revenue: ${max_difference} {max_difference_date}')
print(f'Greatest Decrease in Revenue: ${min_difference} {min_difference_date}')