import time, sys

#Constant for the profit percentage
PROFIT_PERCENT = .23

#Function that prints out the program title in ASCII art line by line in .1 second intervals
def printTitle():
    print("""  _____            __ _ _      _____      _      """)
    sys.stdout.flush()
    time.sleep(0.1)
    print(""" |  __ \          / _(_) |    / ____|    | |     """)
    sys.stdout.flush()
    time.sleep(0.1)
    print(""" | |__) | __ ___ | |_ _| |_  | |     __ _| | ___ """)
    sys.stdout.flush()
    time.sleep(0.1)
    print(""" |  ___/ '__/ _ \|  _| | __| | |    / _` | |/ __|""")
    sys.stdout.flush()
    time.sleep(0.1)
    print(""" | |   | | | (_) | | | | |_  | |___| (_| | | (__ """)
    sys.stdout.flush()
    time.sleep(0.1)
    print(""" |_|   |_|__\___/|_| |_|\__|__\_____\__,_|_|\___|""")
    sys.stdout.flush()
    time.sleep(0.1)
    print("""         |  _ \        |__   __| | |             """)
    sys.stdout.flush()
    time.sleep(0.1)
    print("""         | |_) |_   _     | |    | |             """)
    sys.stdout.flush()
    time.sleep(0.1)
    print("""         |  _ <| | | |    | |_   | |             """)
    sys.stdout.flush()
    time.sleep(0.1)
    print("""         | |_) | |_| |    | | |__| |             """)
    sys.stdout.flush()
    time.sleep(0.1)
    print("""         |____/ \__, |    |_|\____/              """)
    sys.stdout.flush()
    time.sleep(0.1)
    print("""                 __/ |                           """)
    sys.stdout.flush()
    time.sleep(0.1)
    print("""                |___/                            
    """)
    sys.stdout.flush()
    time.sleep(0.1)

#Function that prints out "Goodbye" in ASCII art line by line in .1 second intervals
def printGoodbye():
    print("""\n   _____                 _ _                """)
    sys.stdout.flush() 
    time.sleep(0.1)
    print("""  / ____|               | | |               """)
    sys.stdout.flush()
    time.sleep(0.1)
    print(""" | |  __  ___   ___   __| | |__  _   _  ___ """)
    sys.stdout.flush()
    time.sleep(0.1)
    print(""" | | |_ |/ _ \ / _ \ / _` | '_ \| | | |/ _ \\""")
    sys.stdout.flush()
    time.sleep(0.1)
    print(""" | |__| | (_) | (_) | (_| | |_) | |_| |  __/""")
    sys.stdout.flush()
    time.sleep(0.1)
    print("""  \_____|\___/ \___/ \__,_|_.__/ \__, |\___|""")
    sys.stdout.flush()
    time.sleep(0.1)
    print("""                                  __/ |     """)
    sys.stdout.flush()
    time.sleep(0.1)
    print("""                                 |___/      
    """)
    sys.stdout.flush()
    time.sleep(0.5)

#prints out "Calculating" with an elipse that builds up for effect
#then calculates and returns the profit
def profitMargin(sales):
    print("Calculating", end="")
    sys.stdout.flush()
    time.sleep(0.5)
    sys.stdout.flush()
    print(".", end="")
    sys.stdout.flush()
    time.sleep(0.5)
    print(".", end="")
    sys.stdout.flush()
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    return "$" + str(format(float(sales) * PROFIT_PERCENT, ",.2f"))

#determines if the parameter is able to be converted into a float using
#exceptions. For my purpose, it determines if data is numeric.
def isFloat(data):
    try:
        float(data)
    except ValueError:
        return False
    return True

#Removes dollar sign from sale entry
#in case user decides to include it. Note: Removes
#dollar sign regardless of location and frequency
def removeDollarSign(data):
    counter = 0                                 #counter for counting the number of times dollar sign is found
    index = -1                                  #counter for recording index of dataList
    dataList = list(data)                       #converts sales entry into list 
    for i in dataList:                          #loops over each index of dataList
        index += 1                              #counts up per loop iterance to record the current index of list
        if i == "$":
            counter += 1 
            char = dataList.pop(index)          #takes out the dollar sign found at the index
            dataList.insert(0, char)            #inserts dollar sign at the front of list 
    for i in range(counter):                    #pops off the front of the list for
        dataList.pop(0)                         #each time dollar sign was counted
    return "".join(dataList)                    #joins list elements back into a string

printTitle() #prints title 

try:
    while True: 
        while True:
            sales = input("What were your sales?\nEnter sales: ")       #records sales
            sales = removeDollarSign(sales)                             #removes any dollar signs from sales
            if isFloat(sales):                                          #sales is found to be a number, breaks out of nested loop
                break
            else:                                                       #if it is not a number, passes and continues the inner loop until a number is entered
                print("\nPlease enter a number.\n") 
                pass
        print("Profit: " + profitMargin(sales))                         #calculates profit and then prints it

        #second inner loop asks if the user would like to make another calc
        #if they do, it breaks out of the second nested loop to be looped around again
        #in the main loop to make another calculation, etc.
        while True: 
            decision = input("Would you like to do another profit calculation? Yes or No?\nEnter: ").lower()
            if decision == "yes" or decision == "y":
                break
            elif decision == "no" or decision == "n": #if user doesn't want to go again
                printGoodbye()                        #prints goodbye
                exit()                                #exits the program
            else: 
                print('\nPlease enter a valid decision("Yes", "No", "y", "n") Note: Not case sensitive\n')
                pass
#if the user presses CTRL+C and interrupts the program
#prints goodbye and then exits the program
except KeyboardInterrupt:
    printGoodbye()
    exit()


