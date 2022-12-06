#The number of days the collector collects bugs
DAYS = 5
#Attempts to convert data type to int and return it. 
#if it fails with a ValueError(), it recursively asks for data and checks that data
#until it can convert that data to an int and return it
def dataChecker(data, day):
    try:
        return int(data)
    except ValueError:
        print("Please enter a number.")
        return dataChecker(input("How many bugs did you collect on day " + str(day) + "?\nEnter:"), day)
#Counts bugs for amount of days specified. It does this recursively.
#If more than 500 bugs are collected, the user is congratulated and called a weirdo.
def bugCollector(days, bugs = 0, day = 1, daystr = ""):
    if days == 0:
        insult = lambda x: " Congratulations, weirdo." if (x > 500) else ""
        print("You collected", str(bugs), "bugs in total!" + insult(bugs))
        print(daystr)
    else:
        bugs_per_day = dataChecker(input("How many bugs did you collect on day " + str(day) + "?\nEnter:"), day)
        bugs += bugs_per_day
        daystr += "Day " + str(day) + ": " + str(bugs_per_day) + " bugs" + "\n"
        bugCollector(days - 1, bugs, day + 1, daystr)

bugCollector(DAYS)