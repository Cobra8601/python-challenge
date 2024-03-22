# import os module to create paths across operating systems
import os

# Module for reading csv files
import csv

# This section was assisted by a tutor
CSV_PATH = os.path.join('Resources', 'budget_data.csv')
MONTH_IDX = 0
PROFIT_IDX = 1
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Read in the CSV file
with open(CSV_PATH, 'r') as csv_file:
    csv_reader = csv.reader(csv_file,)

#Read the header row first (skip this if no header)
    csv_header = next(csv_reader)
    print(f"CSV Header: {csv_header}")

# variables
    months = 0
    current_month = 0
    current_profit = 0
    profits_losses = 0
    revenue_change = 0
    previous_revenue = 0
    profit_delta_list = []
    month_delta = []
    avg_change = 0
    pd_list = []
    gr_increase = ["", 0]
    gr_decrease = ["", 9999999]   

# The total number of months included in the dataset
    for row in csv_reader:
        months += 1 
        current_month = row[MONTH_IDX]
        current_profit = row[PROFIT_IDX]
        print(months)
    
# The net total amount of "Profit/Losses" over the entire period
# Code: For each row find the profit or loss and give a running total
        profits_losses = int(profits_losses) + int(row[1])
        print(profits_losses)

# Code: For each row: upcoming month - previous month = profit change by month
#The changes in "Profit/Losses" over the entire period, and then the average of those changes
        revenue_change = float(row[1]) - (previous_revenue)
        previous_revenue = float(row[1])
        profit_delta_list = (profit_delta_list) + [revenue_change]
        month_delta = [month_delta] + [row[0]]
        pd_list = (-1443517.0, 631156.0, -1004755.0, 1581126.0, -289272.0, -1098929.0, 1167557.0, -806093.0, 1124485.0, -1736491.0, -408383.0, 604557.0, -294345.0, 1327485.0, 394323.0, 243585.0, -617439.0, -1530577.0, 1390390.0, -1130397.0, 1293604.0, 641758.0, -337413.0, -52031.0, -937192.0, 863841.0, -76245.0, -100481.0, -960729.0, 591856.0, 54930.0, 680102.0, -250254.0, -840415.0, 582358.0, -48628.0, -135256.0, 978586.0, -599210.0, -442789.0, 652924.0, -1005714.0, 1167373.0, -234900.0, -165147.0, -52275.0, -302320.0, 719028.0, -1825558.0, 1287083.0, -48303.0, 210234.0, -236414.0, 585165.0, -1400632.0, 839777.0, 465229.0, 317811.0, -760202.0, -71868.0, 795457.0, -182685.0, -1242836.0, 1371884.0, -445193.0, 10025.0, -1043998.0, 1350395.0, 80538.0, -1223250.0, 104148.0, 843924.0, -1808664.0, 1505005.0, 306402.0, -143603.0, -1266937.0, -162519.0, 1862002.0, -52986.0, -1627245.0, 616795.0, 628522.0, 90895.0, -224669.0)
        Y = len(pd_list)
        Z = sum(pd_list)
        avg_revenue = Z/Y
        #print(pd_list, Y, Z, avg_revenue)
       
#greatest increase/decrease in profits (date and amount)
#for some reason I am getting an output for Jan 10 and May 10 in addition to Aug 16, and I don't know why
        #if loop inside 'for' loop
        if revenue_change>gr_increase[1]:
            gr_increase[1]=revenue_change
            gr_increase[0]=row[0]  
            print(gr_increase)
#for some reason I am getting output for Feb 10 and Nov 10, and I don't know why
        if revenue_change<gr_decrease[1]:
            gr_decrease[1]=revenue_change
            gr_decrease[0]=row[0]
            print(gr_decrease)

# Results in a table
    print("Financial Analysis")
    print("------------------------")
    print("Total Months: " + str(months))
    print("Total: " + "$" + str(profits_losses))
    print("Average Change: " + str(round(avg_revenue)))
    print("Greatest Increase in Profits: " + str(gr_increase))
    print("Greatest Decrease in Profits: " + str(gr_decrease))
  

# Put in a text file
with open('Budget_analysis.txt', 'w') as text:
    text.write("Financial Analysis\n")
    text.write("------------------------")
    text.write("Total Months: " + str(months) + "\n")
    text.write("Total: " + "$" + str(profits_losses) + "\n")
    text.write("Average Change: " + "$" + (str(round(avg_revenue))) + "\n")
    text.write("Greatest Increase in Profits: " + str(gr_increase) + "\n")
    text.write("Greatest Decrease in Profits: " + str(gr_decrease) + "\n")
   