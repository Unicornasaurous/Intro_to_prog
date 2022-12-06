

class StringInfo():
    """This class provides the functionality to manipulate and 
    extract info about a provided string"""

    def __init__(self, string):
        """The __init__ constructor method of StringInfo"""
        self.string_content = string #This is the content of the string 
        self.vowels_definition = ("a", "e", "i", "o", "u") #What a vowel is defined as
        self.counter()# Calls the counter method 

    def counter(self, index=0, cons=0, vowels=0, digits=0,
        blanks=0, others=0):
        """Method for counting all the types of characters in the string.
        Each number of type of character is assigned as an instance attribute
        of the string obj."""
        if index == len(self.string_content):
            self.num_of_consonants = cons# Number of consonants in the string
            self.num_of_vowels = vowels# Number of vowels in the string
            self.num_of_digits = digits# Number of digits in the string
            self.num_of_blanks = blanks# Number of blank spaces in the string
            self.num_of_others = others# Number of other characters in the string
        elif self.string_content[index].lower() in self.vowels_definition:
            index+= 1
            vowels+=1
            return self.counter(index=index, cons=cons, vowels=vowels, 
                digits=digits, blanks=blanks, others=others)
        elif self.string_content[index].isalpha():
            index+=1
            cons+=1
            return self.counter(index=index, cons=cons, vowels=vowels, 
                digits=digits, blanks=blanks, others=others)
        elif self.string_content[index].isdigit():
            index+=1
            digits+=1
            return self.counter(index=index, cons=cons, vowels=vowels, 
                digits=digits, blanks=blanks, others=others)
        elif self.string_content[index] == " ":
            index+=1
            blanks+=1
            return self.counter(index=index, cons=cons, vowels=vowels, 
                digits=digits, blanks=blanks, others=others)
        else:
            index+=1
            others +=1
            return self.counter(index=index, cons=cons, vowels=vowels, 
                digits=digits, blanks=blanks, others=others)

    def limit_len(self, max_len=20):
        """Method returns a truncated version of the string if the string
        is larger than the max allowable amount(max_len) of characters"""
        if len(self.string_content) > max_len:
            return self.string_content[:max_len] + "..."
        else:
            return self.string_content


def main():
    """Main function of vowcon.py"""
    # Instantiates string info object with user's input as string
    string = StringInfo(input("Enter your string here: "))
    # Prints a sentence explaining how many consonants and vowels are in the users string
    print(f"Your string, '{string.limit_len(max_len=25)}', has {string.num_of_consonants} consonants and {string.num_of_vowels} vowels.") 
    # Prints sentence explaining the number of other chars in the string
    print(f"There are also {string.num_of_digits} digits, {string.num_of_blanks} blank spaces, and {string.num_of_others} other character(s).") 


main()