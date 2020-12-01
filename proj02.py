###########################################################
# Computer Project #2
# Algorithm
# User inputs a purchase price
# User inputs a dollar price
# Program will calculate the change reauired
# If the user inputs a dollar amount greater than purchase, an error is printed
# When user enteres 'q', program displays remaining change  
###########################################################

# Initializing denominations available for dispention
quarters = 10
dimes = 10
nickels = 10
pennies = 10

# Initializing amount of coins used to 0
quarters_spent = 0
dimes_spent = 0
nickels_spent = 0
pennies_spent = 0

# Prints welcome message and starting stock
print("Welcome to change-making program.\n")
print("Stock: {} quarters, {} dimes, {} nickels, and {} pennies".format(
            quarters, dimes, nickels, pennies))

# While loop to continue asking for user input
while True:
    price_str = (input("Enter the purchase price (xx.xx) or 'q' to quit: "))
    
    # If user enters 'q', then program quits and displays remaining change
    if price_str.lower() == "q":
        break
    #converts price to float
    price_float = float(price_str)
    # if price is negative, program displays error message
    if price_float < 0:
        print("Error: purchase price must be non-negative.")
        print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies"
              .format(quarters, dimes, nickels, pennies))
        continue
    
    # If price is greater than 0, then program asks user for dollars input
    if price_float > 0:
        dollars_paid_float = int(input("Input dollars paid (int): "))
        
        # If dollars paid is less than purchase price, it displays an error
        while dollars_paid_float < price_float:
            print("Error: insufficient payment.")
            dollars_paid_float = int(input("Input dollars paid (int): "))
            continue
            
        change = dollars_paid_float - price_float
        change = round(change * 100)
        
    # Prints no change if change is 0
    if change == 0:
        print("No change.")
        print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies"
                  .format(quarters, dimes, nickels, pennies))
        continue
            
    # Reinitializing change spent to 0
    quarters_spent = 0
    dimes_spent = 0
    nickels_spent = 0
    pennies_spent = 0
            
    # Calculates required change
    # Continue looping unitl change is 0
    while quarters > 0 and change >= 25:
        quarters = quarters - 1
        quarters_spent += 1
        change = change - 25
                
    # While loop to calculate number of dimes in change   
    while dimes > 0 and change >= 10:
        dimes = dimes - 1
        dimes_spent += 1
        change = change - 10
    # While loop to calculate number of nickels in change
    while nickels > 0 and change >= 5:
        nickels = nickels - 1
        nickels_spent += 1
        change = change - 5
    # While loop to calculate number of pennies in change   
    while pennies > 0 and change >= 1:
        pennies = pennies - 1
        pennies_spent += 1
        change = change - 1
            
    # If statement to display an out of coins error
    if quarters == 0 and dimes == 0 and nickels == 0 and pennies == 0:
        print("Error: ran out of coins.") 
        break
    # Prints change spent and stock remaining
    else: 
        print("Collect change below: ")
        if quarters_spent > 0:
            print("Quarters:", quarters_spent)
        if dimes_spent > 0:
            print("Dimes:", dimes_spent)
        if nickels_spent > 0:
            print("Nickels:", nickels_spent)
        if pennies_spent > 0:
            print("Pennies:", pennies_spent)
        print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies"
                  .format(quarters, dimes, nickels, pennies))
        
        
    
    
    
             













