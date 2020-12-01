 ###########################################################
#  Computer Project #1
#  Algorithm
#    prompt for an integer/float
#    input an integer
#    loop while negative
#       use conversion functions 
#       output the conversion for rods distance
###########################################################


DECIMAL_PLACE = 3

#This function converts from rods to meters
def rods_to_meters(number_of_rods):
    number_of_meters = number_of_rods*5.0292
    return round(number_of_meters,DECIMAL_PLACE)

#This function converts rods to furlong
def rods_to_furlong(number_of_rods):
    number_of_furlongs = number_of_rods/40
    return round(number_of_furlongs,DECIMAL_PLACE)
 
#This function converts rods to feet
def rods_to_feet(number_of_rods):
    number_of_meters = number_of_rods*5.0292
    number_of_feet = number_of_meters/0.3048
    return round(number_of_feet,DECIMAL_PLACE)

#This functin converts rods to miles
def rods_to_miles(number_of_rods):
    number_of_meters = number_of_rods*5.0292
    number_of_miles = number_of_meters/1609.34
    return round(number_of_miles,DECIMAL_PLACE)

#This function converts rods to minutes to walk
def minutes_to_walk(number_of_rods):
    number_of_meters = number_of_rods*5.0292
    number_of_miles = number_of_meters/1609.34
    minutes = (60*number_of_miles)/3.1
    return round(minutes,DECIMAL_PLACE)

#While loop and if statement will eliminate a negative input    
number_of_rods = -1 
while number_of_rods < 0:  
    #Captures the user input and converts to float in one line
    number_of_rods = float(input("Input rods: "))
    if number_of_rods < 0:
        print("Number of rods can't be negative")
    else:
        print("You input", number_of_rods, "rods.\n")
        print("Conversions")
        print("Meters:", rods_to_meters(number_of_rods))
        print("Feet:", rods_to_feet(number_of_rods))
        print("Miles:", rods_to_miles(number_of_rods))
        print("Furlongs:", rods_to_furlong(number_of_rods))
        print("Minutes to walk", number_of_rods, "rods:", \
             minutes_to_walk(number_of_rods))

    
    


