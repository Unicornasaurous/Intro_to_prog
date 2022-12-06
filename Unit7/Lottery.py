from random import randint
def lottery_gen(length=7, span=(0, 9)):
    lottery_list = []
    for i in range(length):
        lottery_list.append(randint(span[0], span[1]))
    print("Your lottery number is: ", end="")
    for num in lottery_list:
        print(num, end=" ")
    print()
lottery_gen()
