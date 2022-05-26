import csv

Candidate=[]
with open("election_data.csv", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header=next(csvfile)

    for i in csvreader:
        Candidate.append(i[2])


TotalVotes=len(Candidate)


# Creating a List of candidates 
CandidateList=[]                                        
for candidate in Candidate:                     
    if candidate not in CandidateList:                  
        CandidateList.append(candidate)                


#Calculating Total votes 
Votes={i:0 for i in CandidateList}                    
                                                       
for i in range(0,len(Candidate)):                            
    if Candidate[i]=="Khan":                    
        Votes["Khan"]=Votes["Khan"]+1                   

    elif Candidate[i]=="Correy":
        Votes["Correy"]=Votes["Correy"]+1

    elif Candidate[i]=="Li":
        Votes["Li"]=Votes["Li"]+1

    else:                                               
       Votes["O'Tooley"]=Votes["O'Tooley"]+1    



print("Election Results")                              
print("------------------------")                      
print("Total Votes: ", TotalVotes)
print("------------------------")
print("Khan: ", round(Votes["Khan"]/TotalVotes,2)*100,"%    ", "("+str(Votes["Khan"])+")")               
print("Correy: ", round(Votes["Correy"]/TotalVotes,2)*100, "%   ", "("+str(Votes["Correy"])+")")
print("Li: ", round(Votes["Li"]/TotalVotes,2)*100, "%   ", "("+str(Votes["Li"])+")")
print("O'Tooley: ", round(Votes["O'Tooley"]/TotalVotes,2)*100, "%   ", "("+str(Votes["O'Tooley"])+")")
print("------------------------")
print("Winner: ", max(Votes, key=Votes.get))           
print("------------------------")


#Creating Text Document With Output
with open('Election Results.txt', 'w') as f:
    f.write("Election Results")
    f.write('\n')
    f.write("--------------------------")
    f.write('\n')
    f.write("Total Votes: " + str(TotalVotes))
    f.write('\n')
    f.write("--------------------------")
    f.write('\n')
    f.write("Khan: " + " " +str(round(Votes["Khan"]/TotalVotes,2)*100) + "%, (" + str(Votes["Khan"]) + ") ")
    f.write('\n')
    f.write("Correy: " +" "+ str(round(Votes["Correy"]/TotalVotes,2)*100) +  "%, (" + str(Votes["Khan"]) + ") ")
    f.write('\n')
    f.write("Li: " +" "+ str(round(Votes["Li"]/TotalVotes,2)*100) + "%, (" + str(Votes["Li"]) + ") ")
    f.write('\n')
    f.write("O'Tooley: " +" "+ str(round(Votes["O'Tooley"]/TotalVotes,2)*100) + "% " + ", (" + str(Votes["O'Tooley"]) + ") ")
    f.write('\n')
    f.write("------------------------")
    f.write('\n')
    f.write("Winner: " + max(Votes, key=Votes.get))
    f.write('\n')
    f.write("------------------------") 
