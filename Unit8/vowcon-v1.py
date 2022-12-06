

class StringObj():
    """This class provides the functionality to manipulate and 
    extract info about a provided string"""

    def __init__(self, string):
        """The __init__ constructor method of StringObj"""
        self.string_content = string #This is the content of the string 
        self.vowels_definition = ("a", "e", "i", "o", "u") #What a vowel is defined as

    def counter(self, index=0, cons=0, vowels=0, digits=0,
        blanks=0, others=0, option=None):
        if index == len(self.string_content):
            options = {"cons":cons, "vowels":vowels, "digits":digits,
                "blanks":blanks, "others":others}
            return options[option]
        elif self.string_content[index] not in self.vowels_definition \
            and self.string_content[index].isalpha():
            index+=1
            cons+=1
            return self.counter(index=index, cons=cons, vowels=vowels, 
                digits=digits, blanks=blanks, others=others, option=option)
        elif self.string_content[index] in self.vowels_definition:
            index+= 1
            vowels+=1
            return self.counter(index=index, cons=cons, vowels=vowels, 
                digits=digits, blanks=blanks, others=others, option=option)
        elif self.string_content[index].isdigit():
            index+=1
            digits+=1
            return self.counter(index=index, cons=cons, vowels=vowels, 
                digits=digits, blanks=blanks, others=others, option=option)
        elif self.string_content[index] == " ":
            index+=1
            blanks+=1
            return self.counter(index=index, cons=cons, vowels=vowels, 
                digits=digits, blanks=blanks, others=others, option=option)
        else:
            index+=1
            others +=1
            return self.counter(index=index, cons=cons, vowels=vowels, 
                digits=digits, blanks=blanks, others=others, option=option)

    def cons_num(self):
        """Method counts and returns the number of consonants in the string obj"""
        return self.counter(option="cons")

    def vowels_num(self):
        """Method counts and returns the number of vowels in the string obj"""
        return self.counter(option="vowels")

    def digits_num(self):
        """Method returns the number of characters that are digits"""
        return self.counter(option="digits")

    def blanks_num(self):
        return self.counter(option="blanks")

    def others_num(self):
        """Method returns the number of characters that are neither a number 
        nor a letter"""
        return self.counter(option="others")

    def limit_len(self, max_len=20):
        """Method returns a truncated version of the string if the string
        is larger than the max allowable amount of characters"""
        if len(self.string_content) > max_len:
            return self.string_content[:max_len] + "..."
        else:
            return self.string_content


def main():
    """Main function of vowcon.py"""
    string = StringObj(input("Enter your string here: ")) # Instantiates string object with user's input as string
    num_of_consonants = string.cons_num() # Number of consonants in the string
    num_of_vowels = string.vowels_num()# Number of vowels in the string
    num_of_digits = string.digits_num()# Number of digits in the string
    num_of_blanks = string.blanks_num()
    num_of_others = string.others_num() # Number of other characters in the string
    print(f"Your string, '{string.limit_len(max_len=25)}', has {num_of_consonants} consonants and {num_of_vowels} vowels.") #Prints a sentence explaining how many consonants and vowels are in the users string
    print(f"There are also {num_of_digits} digits, {num_of_blanks} blank spaces, and {num_of_others} other character(s).") #Prints sentence explaining the number of other chars in the string


main()