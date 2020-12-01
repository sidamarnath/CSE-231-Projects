###########################################################
# Computer Project #5
# Algorithm
# prompt user for a year
# opens corresponding file
# finds the average salary of corresponding file
# calculates median salary
# calculates the range
# prompt user to see plot
# prompts user to enter percent or range
###########################################################

# imports pylab to access graph tools
import pylab

# do plot 
def do_plot(x_vals,y_vals,year):
    
    # displays all x and y labels for the plot
    pylab.xlabel('Income')
    pylab.ylabel('Cumulative Percent')
    pylab.title("Cumulative Percent for Income in "+str(year))
    pylab.plot(x_vals,y_vals)
    pylab.show()

# open file function    
def open_file():
    '''This function will open income data file for a specific year range \
    entered by user'''
    # prompts user for year until user enters a valid year
    while True:
        year_str = input("Enter a year where 1990 <= year <= 2015: \n")
        
        if year_str.isdigit():
            
        # if statement to check if year is valid
            if int(year_str) >= 1990 and int(year_str) <= 2015:
                filename = "year"+ year_str + ".txt"
                # opens file if year is valid
                try:
                    fp = open(filename)
                    break
                # prints error message if file is not valid
                except:
                    print("Error in file name:",filename," Please try again.")
            else:
                # prints error message if year is not in range
                print("Error in year. Please try again.")
        else:
            print("Error in year. Please try again.")
            
    return fp, int(year_str)

# read file function to read file and eliminate lines
def read_file(fp):
    '''This function reads the file entered by user and creates a list'''
    # data list set to an empty list
    data_list = []
    # reads lines in file
    reader = fp.readlines()
    
    # reads every line in file from line 2 onwards
    for line in reader[2:]:
        data = line.split()
        data.pop(1)
        # if statement to account for words "and over" and  is set to a number
        if data[1] == "over":
            data[1] = "100,000,000,000"
        # adds data to the data list
        data_list.append(data)
        
    return data_list  

# find avg function to find avg salary       
def find_average(data_lst):
    '''This function returns the average salary from data list '''
    # set variables to 0
    avg_salary = 0
    numerator = 0
    denominator = 0
    
    # reads each line in data list
    for line in data_lst:
        # replaces numerator and denominator to replace commas
        n = line[5].replace(",", "")
        d = line[2].replace(",", "")
        # calculates sum of numerator and denominator
        numerator = numerator + float(n)
        denominator = denominator + float(d)
        
    # calculates average salary and returns that value   
    avg_salary = (numerator / denominator)
    
    return avg_salary
  
# find median function to find median salary   
def find_median(data_lst):
    '''This function returns the median income from data list'''
    # set median salary = 0
    median_salary = 0
    
    # reads each line in data list
    for line in data_lst:
        # finds value closest to 50
        temp_val = line[4].replace(",","")
        if float(temp_val) >= 50.00:
            after_line = line
            break
        else:
            if float(temp_val) <= 50:
                before_line = line
    if abs(float(before_line[4]) - 50) < abs(float(after_line[4]) - 50):
       sal_range, percent, median_salary = get_range(data_lst, float(before_line[4]))
    else:
        # setting multiple variables equal to get range function
        sal_range, percent, median_salary = get_range(data_lst, float(after_line[4]))
            
    return median_salary

# get range function to get salary range as tuple      
def get_range(data_lst, percent):
    '''This function returns a salary range from the data list for a percent'''
    
    # reads each line in data list
    for line in data_lst:
        
        # setting variables to desired lines and replaces commas
        top_range = float(line[0].replace(",",""))
        bottom_range = float(line[1].replace(",",""))
        percentage = float(line[4].replace(",",""))
        avg = float(line[6].replace(",",""))
        
        # if statement to see if percent is greater than or equal to percent
        if percentage >= percent:
            break
       
    # returns range(as a tuple), percentage, and avg
    return (top_range,bottom_range), percentage, avg

# get percent function to get percent based on salary
def get_percent(data_lst,salary):
    '''This function returns percentage from data list and salary'''
    # reads each line in data list
    for line in data_lst:
        # setting variables based on line 
        bottom_range = float(line[0].replace(",",""))
        top_range = float(line[1].replace(",",""))
        
        # if statement to see if salary is within range
        if salary >= bottom_range and salary <= top_range:
            percentage = float(line[4].replace(",",""))
            break
        # if salary isn't in range, percentage = 0.0 and print error message
        else:
            percentage = 0.0
    return (bottom_range,top_range), percentage

# main function where everything executes       
def main():
    # sets each variable to open each function necessary
    fp, year = open_file()
    dl = read_file(fp)
    avg = find_average(dl)
    median = find_median(dl)
    
    # prints and formats year, median, and avg salary
    print("{:6s}{:6s}{:20s}".format("Year", "Mean", "Median"))
    print("{:<6d}${:<14,.2f}${:<14,.2f}".format(year, avg, median))
    #print("The average income was ${:<13,.2f}".format(avg))
    #print("The median income was ${:<1,.2f}".format(median))
    
    # asks user if he/she wants to see a plot value
    response = input("Do you want to plot values (yes/no)? ")
    
    # if "yes" then do calculations
    if response.lower() == 'yes':
        # counter set to 0
        counter = 0
        x_vals = []
        y_vals = []
        # reads each row in dl
        for row in dl:
            # sets x and y vals to designated row assignment
            x_vals.append(float(row[1].replace(",", "")))
            y_vals.append(float(row[4].replace(",","")))
            # increase counter by 1
            counter += 1
            # max 40 count limit then loop breaks
            if counter == 40:
                break
            
        do_plot(x_vals,y_vals,year)
    
    # asks user to input whether user wants a range or percent
    choice = \
    input("Enter a choice to get (r)ange, (p)ercent, or nothing to stop: ")
    
    while choice:
        # if statement to do necessary calculatons on if user enters "r" or "p"
        if choice == "r":
            prompt = float(input("Enter a percent: "))
            
            # if statement to test whether prompt is within range
            if prompt < 0 or prompt > 100:
                # prints error message if if statement is true
                print("Error in percent. Please try again")
            # if statement is not true, do caluclations
            else:
                salary_range, percentage, avg = get_range(dl,prompt)
                bottom_range = salary_range[0]
                print("{:4.2f}% of incomes are below ${:<13,.2f}.".format \
                      (prompt, bottom_range))
            
        
        elif choice == "p":
            prompt = float(input("Enter an income: \n"))
            
            # if statement to check whether prompt is positive value
            if prompt < 0:
                # prints error message if if statement is true
                print("Error: income must be positive")
            # if if statement is not true, program does calculations
            else:
                salary_range, percentage = get_percent(dl,prompt)
                print\
                ("An income of ${:<13,.2f} is in the top {:4.2f}% of incomes."\
                      .format(prompt, percentage))
         
        # if none of the inputs match, print error message in selection
        else:
            print("Error in selection.")
        # asks user again if user wants to see more ranges or percents
        choice = \
        input("Enter a choice to get (r)ange, (p)ercent, or nothing to stop: ")

# calling main function
if __name__ == "__main__":
    main()

