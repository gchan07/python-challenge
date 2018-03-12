#Modules
import os
import csv

count = 0
total_revenue = 0
revenue =[]
date = []

# Set path for files
filepath = os.path.join("raw_data", "budget_data_2.csv")

# Open the CSV
with open(filepath, newline="") as csvfile:
	bank = csv.reader(csvfile, delimiter=",")
	for row in bank:
		count = count + 1
		if count != 1:
			revenue.append(int(row[1]))
			date.append(row[0])
			total_revenue = total_revenue + int(row[1])

#check list of dates
#print(date)	
		
#print total months -1 for header
print("Total Months: " + str(count-1))
#print total revenue
print("Total Revenue: $"+ str(total_revenue))


#Average Revenue Change = Change in Month/Total Months
avg_change =[]

#grab first month of revenue b/c change in revenue = first month revenue - 0 - add to list
avg_change.append(revenue[0])

for i in range(0, len(revenue)-1):
	
	#change in revenue - add to list
	avg_change.append((revenue[i+1])-(revenue[i]))

#print(avg_change)

sum_avg_change = sum(avg_change)
#print(sum_avg_change)

avg_rev_change = sum_avg_change/(count-1)
#print(avg_rev_change)

#print average revenue change
print("Average Revenue Change: $" + str(avg_rev_change))

#Greatest Increase in Revenue - find largest number in avg_change list, then find corresponding month

max_avg_change = max(avg_change)
#print(max_avg_change)

#find index of where max_avg_change is in the avg_change list

max_index = avg_change.index(max_avg_change)
#print(max_index)
#print(date[max_index])
print("Greatest Increase in Revenue: " + date[max_index] + " ($"+ str(max_avg_change)+")")

#Greatest Decrease in Revenue - find smallest number in avg_change list, then find corresponding month

min_avg_change = min(avg_change)
#print(min_avg_change)

#find index of where min_avg_change is in the avg)change list
min_index = avg_change.index(min_avg_change)
#print(min_index)
#print(date[min_index])
print("Greatest Decrease in Revenue: " + date[min_index] + " ($"+ str(min_avg_change)+")")

