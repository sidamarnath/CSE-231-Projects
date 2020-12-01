# Computer Project #3
# Algorithm
# extract data from a file and use information to display GDP information
# Using different functions to seperate process 

# open_file function to ask user to enter a file name and open the GDP.txt file
def open_file():
    #While loop to continue asking for file name until user enters it correctly
    fp_good = False
    while not fp_good:
        input_file = input("Enter a file name: ")
        try:
            fp = open(input_file)
            fp_good = True
        #using try and except for incorrect file input from user
        except FileNotFoundError:
            print("Error. Please try again")
            continue

    return fp

# find_min_percent function takes in a line from GDP.txt
def find_min_percent(line):
    #Initializing all variables 
    #Initialized minimum_value to a number well above data maximum
    minimum_value = 10000000.0
    index = 76
    return_index_min = 0
    line_size = len(line)
                                                           
    
    #while(index < line_size):
    for index in range(0, line_size):
        try:
            value =  line[index:index+12]
        # Converting temp_value to a float
            temp_value = float(value.strip())
            # if statement to determine minimum value 
            if temp_value < minimum_value:
                minimum_value = temp_value
                # add 5 to offset spaces
                return_index_min = index + 5
            
            index += 12
        except ValueError:
            continue

    # Returning minimum value and return index for that value
    return minimum_value, return_index_min

# find_max_percent function same as find_min_percentage 
# finding max values of two lines instead 
def find_max_percent(line):
    maximum_value = 0
    index = 0
    return_index_max = 0
    line_size = len(line)
                                                           
#    while(index < line_size):
    for index in range(0, line_size):
        try:
            value =  line[index:index+12]
            temp_value = float(value.strip())
            # if statement to find max value
            if temp_value > maximum_value:
                maximum_value = temp_value
                # add 5 to offset spaces
                return_index_max = index + 5
           
            index += 12
        except ValueError:
            continue
     # returning max value and index for that value
    return maximum_value, return_index_max

# find_gdp gets that value from the file using index calculated previously
def find_gdp(line, index):
    gdp_value = line[index:index+12]
    return float(gdp_value)

#display function to format output in the kernel
def display(minimum_value, minimum_year, minimum_value_gdp, maximum_value,
            maximum_year, maximum_value_gdp):
    #printing all headers and values calculated
    print()
    print("Gross Domestic Product")
    print("{:<10s}{:>8.6s}{:>6s}{:>18.16s}".format("min/max", "change", "year"
          , "GDP (trillions)"))
    print("{:<10s}{:>8.1f}{:>6d}{:>18.2f}".format("min", float(minimum_value),
          int(minimum_year), round(minimum_value_gdp/1000,2)))
    print("{:<10s}{:>8.1f}{:>6d}{:>18.2f}".format("max", float(maximum_value),
          int(maximum_year), round(maximum_value_gdp/1000,2)))
 
# main function to extract two lines from file required   
def main():
    fp = open_file()
    counter_line = 1
    gdp_percentage = ""
    gdp_value = ""
    # setting each line required as a different variable 
    for line in fp:
        if counter_line == 9:
            gdp_percentage = line
        if counter_line == 44:
            gdp_value = line
        if counter_line == 8:
            gdp_year_percentage = line
        if counter_line == 43:
            gdp_value = line
        counter_line += 1
    
    # getting max percentage and it's index from line 9    
    percent_max, max_index = find_max_percent(gdp_percentage)
    # Getting data for year by passing line 8 and max index
    maximum_year = find_gdp(gdp_year_percentage, max_index)    
    # calling find min percent and find gdp functions        
    percent_min, min_index = find_min_percent(gdp_percentage)
    minimum_year = find_gdp(gdp_year_percentage, min_index)
    minimum_value_gdp = find_gdp(gdp_value, int(min_index))
    # extracting max value from lines in file
    maximum_value_gdp = find_gdp(gdp_value, int(max_index))
    # calling display function
    display(percent_min, minimum_year, minimum_value_gdp, percent_max,
            maximum_year,maximum_value_gdp) 
    fp.close()
    return percent_min, minimum_year, minimum_value_gdp, percent_max,
    maximum_year,maximum_value_gdp

# Calls the 'main' function only when you execute within Spyder (or console)
# Do not modify the next two lines.
if __name__ == "__main__":
    main()






    


    

