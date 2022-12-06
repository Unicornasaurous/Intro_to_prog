from datachecker import dataChecker

def inputChecker(prompt):
    while True:
        value = input(prompt)
        if dataChecker(value, "num"):
            break
        else:
            print("Please enter a number")
    return value

def exponent(power, powerto, newval=1):
    if powerto == 0:
        return 1
    if powerto == 1:
        if newval == 1:
            return power
        else:
            return newval
    elif newval == 1:
        newval = power*power
        return exponent(power, powerto-1, newval)
    else:
        newval = newval*power
        return exponent(power, powerto-1, newval)

def main():
    p = float(inputChecker("Enter current bank balance:"))
    i = float(inputChecker("Enter interest rate:"))
    t = float(inputChecker("Enter the amount of time that passes:"))
    f = p * exponent((1 + i), t)
    return "$" + format(f, ".2f")

print(main())
