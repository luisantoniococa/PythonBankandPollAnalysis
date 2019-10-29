import os
import csv 
#creating a variable to contain the data to be executed
bank_data_csv = os.path.join('..','Bank_Analysis','PyBank_Resources_budget_data.csv')
# define the functions for different part of the Analysis
def finantial_analysis(bank_dataset):
    month = str(bank_dataset[0])
    change = int(bank_dataset[1])
    absolutechange = int(abs(change))
    # ask in class about using len to obtain the values of the column months
    #print (len(month))
    # net_total = 0
    # for row in bank_dataset:
    #     net_total += absolutechange
    #     print (absolutechange)
    #print(f'the net total is {net_total}')
    #return net_total
#read the csvfile
def average(numbers):
    length = len(numbers)
    total = 0.00
    for number in numbers:
        total += number
    return total / length

with open(bank_data_csv, 'r') as csvfile:
    #split the data with commas
    csvreader = csv.reader(csvfile, delimiter = ',')
    #defining the variable for counting months
    counter = 0
    net_total = 0
    greater_change=[0.00, "date"]
    lowest_change=[0.00, "date"]
    next(csvreader)
    print ("\n \n Finantial Analysis \n-----------------------------")
    #counting the amount of months
    for row in csvreader:
        counter += 1 
        net_total += int(row[1])
        if int(row[1])>greater_change[0]:
            greater_change[0] = int(row[1])
            greater_change[1] = str(row[0])
        if int(row[1]) < lowest_change[0]:
            lowest_change[0] = int(row[1])
            lowest_change[1] = str(row[0])

    print(f'Months: {counter} \nNet total: {net_total} \nAverage: {net_total/counter}')
    print (f'Greatest Change:{greater_change[1]} {greater_change[0]} \nLowest Change: {lowest_change[1]} {lowest_change[0]}')