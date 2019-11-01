import os
import csv 
#creating a variable to contain the data to be executed
bank_data_csv = os.path.join('..','Bank_Analysis','PyBank_Resources_budget_data.csv')
# using open to read the csv file and execute the analysis
with open(bank_data_csv, 'r') as csvfile:
    #split the data with commas
    csvreader = csv.reader(csvfile, delimiter = ',')
    #defining the variable for counting months, the net total
    counter = 0
    net_total = 0
    #creating arrays to save the data and the amount of the max and min changes 
    greater_change=["date",0.00]
    lowest_change=["date",0.00]
    #skip the top row with the headers
    next(csvreader)
    print ("\n \n Finantial Analysis \n-----------------------------")
    #creating a 2d array to save the information for better iteration 
    array=[]
    array.append([])
    array.append([])
    for row in csvreader:
        #saving the information from the csv in the array we created earlier
        array[0].append(row[0])
        array[1].append(int(row[1]))
        #this condition let us identify the mas and min change and saved in corresponding arrays
        if array[1][counter]>greater_change[1]:
            greater_change[1] = array[1][counter]
            greater_change[0] = array[0][counter]
        if array[1][counter]<lowest_change[1]:
            lowest_change[1] = array[1][counter]
            lowest_change[0] = array[0][counter]
        #sum of net total and adding a counter for the array iteration
        net_total +=array[1][counter]
        counter += 1
    #creating a variables for the total average change iteration and sum 
    change=0
    i=1
    #while loop to get the sum and then create the average
    while i is not counter :
        change = change + (array[1][i]-array[1][i-1])
        i+=1
        #this condition makes sure the get out of the loop as soon as we are out of range of the array
        if i is (counter):
            break
    #printing the results and doing some basic formating
    print(f'Months: {counter} \nNet total: {net_total} \nAverage: {change/counter}')
    print (f'Greatest Change:{greater_change[0]} {greater_change[1]} \nLowest Change: {lowest_change[0]} {lowest_change[1]}')