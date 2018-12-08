import os 
import csv 
 
date, revenue = ([] for i in range(2)) 

 
# input and output files 
input_file = "budget_data.csv" 
output_file = "budget_data_result.txt" 

 # file path
budget_data = os.path.join("budget_data.csv")
with open(budget_data , 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')


#results path
results= os.path.join("results.txt")
  
with open(budget_data, mode='r', newline='') as csvfile: 
    reader = csv.reader(csvfile, delimiter=',') 
 
 
    next(reader) 

   
    row_num = 0 
    for row in reader: 
        date.append(row[0]) 
        revenue.append(row[1]) 
        row_num += 1 


 # |  Summary Table  | 


# print summary header
print("\nFinancial Analysis", "\n" + "-" * 50) 
  
 
  # sum of months 
print("Total Months:", row_num) 

 
# sum of revenue 
revenue_sum = 0 
for i in revenue: 
    revenue_sum += int(i) 
 
 
print("Total Revenue: $" + str(revenue_sum)) 
  
 
 
 
# average revenue change 
total_revenue_change = 0 
for h in range(row_num): 
    total_revenue_change += int(revenue[h]) - int(revenue[h - 1]) 
 
 
  # the first_pass variable is created to remove the first iteration revenue change 
 # which, takes the first list element and subtracts it by the last list element. 
first_pass = (int(revenue[0]) - int(revenue[-1])) 
total_revenue_change_adj = total_revenue_change - first_pass 
 
 
avg_revenue_change = (total_revenue_change_adj + int(revenue[0])) / row_num 
print("Average Revenue Change: $" + str(round(avg_revenue_change))) 
 
 
  
 
 # greatest increase in revenue 
high_revenue = 0 
for j in range(len(revenue)): 
    if int(revenue[j]) - int(revenue[j - 1]) > high_revenue: 
       high_revenue = int(revenue[j]) - int(revenue[j - 1]) 
       high_month = date[j] 

 
print("Greatest Increase in Revenue:", high_month, "($" + str(high_revenue) + ")") 
 
 

 # greatest decrease in revenue 
low_revenue = 0 
for k in range(len(revenue)): 
    if int(revenue[k]) - int(revenue[k - 1]) < low_revenue: 
       low_revenue = int(revenue[k]) - int(revenue[k - 1]) 
       low_month = date[k] 
 
 
print("Greatest Decrease in Revenue:", low_month, "($" + str(low_revenue) + ")") 
  
 
 # white space after table 
print("\n\n") 
 
 

 
  # |  Output TXT File  | 
 
  
with open(results, mode='w', newline='') as summary_txt: 
     writer = csv.writer(summary_txt) 

     writer.writerows([ 
         ["Financial Analysis for: " + input_file], 
         ["-" * 50], 
         ["Total Months: " + str(row_num)], 
         ["Total Revenue: $" + str(revenue_sum)], 
         ["Average Revenue Change: $" + str(round(avg_revenue_change))], 
         ["Greatest Increase in Revenue: " + str(high_month) + " ($" + str(high_revenue) + ")"], 
         ["Greatest Decrease in Revenue: " + str(low_month) + " ($" + str(low_revenue) + ")"] 
 
   ])

