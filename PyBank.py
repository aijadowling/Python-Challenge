import csv


#Creating Varibles
Nmonths=0
TotalProfits=0
Date=[]
ProfitLoss=[]
Change=[]

#Importing
with open("budget_data.csv", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header=next(csvfile)

    for i in csvreader:
        Date.append(i[0])
        ProfitLoss.append(int(i[1]))

#Calculations 
Nmonths=len(Date)
TotalProfits=sum(ProfitLoss)

#Creating List of Change
for i in range(0,len(ProfitLoss)):
    if i >0:
        Change.append(ProfitLoss[i]-ProfitLoss[i-1])


#Finding Max Min values and respective dates
maxchange=0  
minchange=0
datemin=[]
datemax=[]

for i in range(0,len(Change)):
    if Change[i]>maxchange:
        maxchange=Change[i]
        datemax=Date[i+1]
    elif Change[i]<minchange:
        minchange=Change[i]
        datemin=Date[i+1]

#Printing our results
print("Financial Analysis")
print("--------------------------")
print("Total Months: ", Nmonths)
print("Total: ", TotalProfits)
print("Average Change In Profits: ", sum(Change)/len(Change))
print("Greatest Increase in profits: ", datemax, maxchange)
print("Greatest Decrease in losses: ", datemin, minchange)


#Creating Text Document With Output
with open('Financial Analysis.txt', 'w') as f:
    f.write("Financial Analysis")
    f.write('\n')
    f.write("--------------------------")
    f.write('\n')
    f.write("Total Months: " + str(Nmonths))
    f.write('\n')
    f.write("Total: " + str(TotalProfits))
    f.write('\n')
    f.write("Average Change In Profits: " + str(sum(Change)/len(Change)))
    f.write('\n')
    f.write("Greatest Increase in profits: " + str(datemax) + " " + str(maxchange))
    f.write('\n')
    f.write("Greatest Decrease in losses: " + str(datemin) + " " + str(minchange))