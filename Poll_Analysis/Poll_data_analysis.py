import os 
import csv

#creating a variable to contain the data to be executed
poll_data = os.path.join('..','Poll_Analysis','PyPoll_election_data.csv')
#opening the data as read for csv files
with open (poll_data, 'r') as csvfile:
    #setting the delimiter for a comma
    poll = csv.reader(csvfile, delimiter = ',')
    #using next to ignore the first row with headers
    next (poll)
    #creating an empty dictionary where the candidates and the votes are going to be stored
    candidates = {}
    #a variable to count all the votes
    vote_count = 0
    #the iteration for every row in the csv
    for row in poll:
        vote_count += 1
        #we are going to store in the dictionary any name that is not repetitive and when ever the name is founded for the first time it will create the first vote
        if row[2] not in candidates.keys():
            candidates[row[2]] = 1    
        if row[2] in candidates.keys():
            candidates[row[2]] += 1
    #creating an empty array with the winner name and the ammount of votes
    winner = ['person',0]
    #printing the results of the vote count
    print(f'Election Results \n---------------------- \nTotal Votes: {vote_count} \n-----------------------------')
    #using the for statement in orther to find the winner
    for person in candidates:
        if candidates[person] > winner[1]:
            winner[0]= person
            winner[1]= candidates[person]
        #printing all the results 
        print (f' {person} : {round((candidates[person]/vote_count)*100, 4)} % ({candidates[person]}) Votes ' )
    print(f'---------------------------\nWinner: {winner[0]} \n---------------------')
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
        