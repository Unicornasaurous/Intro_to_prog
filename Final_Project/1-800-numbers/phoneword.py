from stringtools import StrTools as tools
from random import choice

map = {"abc": "2", "def": "3", "ghi": "4", "jkl": "5", 
"mno": "6", "pqrs": "7", "tuv": "8", "wxyz": "9"}

def converter(phoneword):
    index = -1
    for char in phoneword:
        index += 1
        for key in map:
            if char.lower() in key:
                phoneword = tools.char_replace(phoneword, index, map[key])
                break
    return phoneword

def inv_converter(phonenumber, full=False):
    phoneword=""
    for char in phonenumber:
        counter=0
        for key in map:
            if char.lower() == map[key]:
                if full:
                    phoneword+=f"({key})"
                else:
                    phoneword+=choice(list(key))
                break
            else:
                counter+=1
        if counter == len(map):
            phoneword+=char
    return phoneword



        
        
        


    

    