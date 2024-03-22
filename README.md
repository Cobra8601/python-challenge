# python-challenge

## Prepare the data
* Import modules:  os and csv
* Establish the file pathway
* Create indexes of the columns in the dataset
* Read in the file, while skipping the header
* Create a code list (# variables) for analysis

## Analysis - PyBank
* Use a for loop to iterate through rows of the month index; (n = 86)
* Use a for loop to iterate through rows of the profit index and give a total of profits and losses; ($22,564,198)
* Change in profit/loss over the entire period and the average of those changes; for each row, calculated upcoming month - previous month to get profit change by month over the entire period. Created a list of changes to calculate the average by assigning the length of the list to 'Y', and the sum of the list to 'Z', then calculated the average.
Average change = $-8311.11
* Used an if loop inside a for loop to get the greatest increase or decrease in profits by date and amount. (Had some issues here, getting 2 extra dates???)
Greatest Increase in profit = $1862002, August 16th
Greatest Decrease in profit = -$1825558, February 14th
* Put the results into a table
* Export as a text file

## Analysis - PyPoll
* Use a for loop to iterate through rows of the ballot index; (n = 369,711)
* Put the candidate names in a list
* Put the list in a set
* Count the the votes per candidate, set it to 'Y'
* Calculate the % of votes, set it to 'Z'
* Print the total votes, candidate names, vote count per candidate and %
* Determine the winner
* Put the results into a table
* Export as a text file.
  
