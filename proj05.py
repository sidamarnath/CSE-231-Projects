#####################################
# Project #5
# Algorithm
# Prompts user to input file
# Collect data from csv files
# Display max and min years and amount for each state and crop
#####################################

# importing csv
import csv


# Variable states equal to all 50 states
STATES = ['Alaska', 'Alabama', 'Arizona', 'Arkansas', 'California', 
          'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia',
          'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 
          'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 
          'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 
          'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico',
          'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 
          'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 
          'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia',
          'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']


def open_file():
    ''' function will ask user to input function and use try/except to open it '''
    
    # asks user to input a file name
    filename = input("Enter a file: ")
    
    # loop to continue asking user for input until entered correctly
    while True:
        # try/ except to oen file
        try:
            fp = open(filename, "r")
            break
        # Error message is printed when incorrect file name is entered
        # Asks user to enter file name again
        except:
            print("Error in filename")
            
        # Asks user for input again 
        filename = input("Enter a file: ")
        
    return fp

def read_file(fp):
    ''' function will read the file entered and call another function
    that will return a dictionary'''
    
    # empty list
    data_list = []
    
    # reader to get csv file to be read 
    reader = csv.reader(fp)
    
    #skips the first line of the file
    next(reader, None)
    
    # loops through each line in file
    for line in reader:
        
        # strip spaces from first column
        state = line[0].strip()
        
        # checks for Missouri 2/ and changes header to "Missouri"
        if state == "Missouri 2/":
            state = "Missouri"
            line.pop(0)
            line.insert(0, state)
        
        # if empty line, then continue through loop
        if len(line) == 0:
            continue
        # nested if statements to check "All GE varieties"
        # appends line to data list
        else:
            if state in STATES:
                if line[3].strip() == "All GE varieties":
                    if line[6].strip().isdigit():
                        data_list.append(line)         
        
    # calls build map function
    # closes file
    data_map = build_map(data_list)
    fp.close()
        
    return data_map
        


def build_map(data_list):
    ''' function returns min/max year and value for each state'''
    
    # data map set to empty dictionary
    data_map = {}
    
    # loops through each line in list
    for line in data_list:
        
        crop = line[1].strip()
        state = line[0].strip()
        # populate dictionary
        if crop not in data_map:
            
            # second dictionary created
            data_map[crop] = {}
            data_map[crop][state] =[]
        else:
            if state not in data_map[crop]:
                data_map[crop][state] = []
    
    # initializing variables to 0 and empty strings
    min_value = 0
    max_value = 0
    min_year = ""
    max_year = ""
    prev_crop = ""
    prev_state = ""
    
    # loops through line in data list
    # appends max/min year and value to second empty dictionary
    for line in data_list:
        crop = line[1].strip()
        state = line[0].strip()
        year = line[4].strip()
        value = int(line[6].strip())
        if crop != prev_crop or state != prev_state:
            min_year = year
            max_year = year
            min_value = value
            max_value = value
            data_map[crop][state].append(max_year)
            data_map[crop][state].append(max_value)
            data_map[crop][state].append(min_year)
            data_map[crop][state].append(min_value)
        
# calculating min/max value and year from file                                 
        else:
            if value < min_value:
                min_value = value
                min_year = year
                data_map[crop][state].pop(2)
                data_map[crop][state].pop(2)
                data_map[crop][state].insert(2, min_year)
                data_map[crop][state].insert(3, min_value)
                
                
            if value > max_value:
                max_value = value
                max_year = year
                
                data_map[crop][state].pop(0)
                data_map[crop][state].pop(0)
                data_map[crop][state].insert(0, max_year)
                data_map[crop][state].insert(1, max_value)
        
        prev_crop = crop
        prev_state = state
        
    return data_map

def display(data_map):
    ''' function will display results from build map function '''
    
    # crop list created from data map
    crop_list = list(data_map.keys())
    #sorts data list alphabetically
    crop_list.sort()
    
    # loops through each crop in crop list
    for crop in crop_list:
        print("Crop: "+ "{}".format(crop)) 
        # state list created and sorted
        state_list = list(data_map[crop].keys())
        state_list.sort()
        
        # formatting and displaying results
        print("{:<20s}{:<8s}{:<6s}{:<8s}{:<6s}".format("State", "Max Yr",
                                                       "Max", "Min Yr", "Min"))
        
        for state in state_list:
            min_max_list = list(data_map[crop][state])
            
            print("{:<20s}{:<8s}{:<6d}{:<8s}{:<6d}".format(state,
                                                        min_max_list[0],
                                                        int(min_max_list[1]),
                                                        min_max_list[2],
                                                        int(min_max_list[3])))
        
        print()
    
def main():
    ''' function will call all other functions and executes main flow'''
    fp = open_file()
    data_map = read_file(fp)
    display(data_map)

if __name__ == "__main__":
     main()

        

            
            
        
        