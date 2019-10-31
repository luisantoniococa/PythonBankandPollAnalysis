import os 
import csv

#creating a variable to contain the data to be executed
poll_data = os.path.join('..','Poll_Analysis','PyPoll_election_data.csv')
# define the functions for different part of the Analysis
def dictionary(data):
    candidate = str(data[2])
    table = {}
with open (poll_data, 'r') as csvfile:
    poll = csv.reader(csvfile, delimiter = ',')
    next (poll)
    candidates = {}
    count = 0
    for row in poll:
        count += 1
        if row[2] not in candidates.keys():
            candidates[row[2]] = 0    
        if row[2] in candidates.keys():
            candidates[row[2]] += 1
    winner = [0, 'person']
    for person in candidates:
        if candidates[person] > winner[0]:
             
            print (f' {person} : {candidates[person]} {(candidates[person]/count)*100} %' )

    #votetotal =[]    
    # for person in candidates:
    #     print(person)
    #     votetotal.append(int(0))
        
    # print (f'Total votes {count}')
    # print (votetotal)
    # print (candidates)
    # for row in poll:
    #     for i in range(len(candidates)):
    #         if str(candidates[i-1]) == str(row[2]):
    #             votetotal[i-1] = votetotal[i-1] + 1
    #             print (row[2])
    # print (votetotal)
    # votecounter = {
    #     person : counter

    # }       
        