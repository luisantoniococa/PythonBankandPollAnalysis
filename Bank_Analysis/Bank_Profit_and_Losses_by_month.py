import os
import csv 
#creating a variable to contain the data to be executed
bank_data_csv = os.path.join('..','Bank_Analysis','PyBank_Resources_budget_data.csv')
# define the functions for different part of the Analysis
def finantial_analysis(bank_dataset):
    month = str(bank_dataset[0])
    change = int(bank_dataset[1])
    # ask in class about using len to obtain the values of the column months
    #print (len(month))
    net_total = 0
    for row in bank_dataset:
        net_total += change
    #print(f'the net total is {net_total}')
    return net_total
#read the csvfile
with open(bank_data_csv, 'r') as csvfile:
    #split the data with commas
    csvreader = csv.reader(csvfile, delimiter = ',')
    #defining the variable for counting months
    counter = 0
    next(csvreader)
    print ("\n \n Finantial Analysis \n-----------------------------")
    #counting the amount of months
    for row in csvreader:
        counter += 1 
        #calling my funtion to work with the data
        net=finantial_analysis(row)    
    print(f'Months: {counter} \nNet total: {net}')
    