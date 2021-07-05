# import modules
import os
import csv

# Set path for file
csvpath = os.path.join('resources', 'pybank_data.csv')

# open the csv
with open(csvpath) as csvfile:
    next(csvfile)
    csvreader = csv.reader(csvfile, delimiter=",")

# store variables 
    months = 0
    profloss = 0

# set loop
    for row in csvreader:
        # add 1 for every loop, each loop represents a new month
        months = months + 1

        # adds p&l from previous loop with current p&l
        profloss += int(row[1])

        # average of the changes in "Profit/Losses" over the entire period


        # greatest increase in profits (date and amount) over the entire period


        # greatest decrease in losses (date and amount) over the entire period


    print('Financial Analysis')
    print('----------------------------')
    # print months       
    print(f'Total Months: {months}')
    #print(profloss)
    print(f'Total: ${profloss}')

#exfile = open('pybank_analysis.txt', 'w')
# collect the input that will be entered into the text file
inputs = ['Financial Analysis', '----------------------------',
f'Total Months: {months}',f'Total: ${profloss}']

#for loop to input the inputs with a new like for each new entry
with open('pybank_analysis.txt', 'w') as exfile:
    for line in inputs:
        exfile.write(line)
        exfile.write('\n')

