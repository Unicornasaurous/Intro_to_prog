class StrTools():
    """This class provides tools to manipulate strings"""
    
    def char_replace(string, index, newchar):
        string_list = []
        for char in string:
            string_list.append(char)
        string_list[index] = newchar
        new_string = ""
        for item in string_list:
            new_string += item
        return new_string

    def char_remove(string, index):
        string_list = []
        for char in string:
            string_list.append(char)
        try:
            del string_list[index]
        except IndexError:
            pass
        new_string = ""
        for item in string_list:
            new_string += item
        return new_string

    
    def char_add(string, index, newchar):
        front_slice = string[:index]
        back_slice = string[index:]
        string = front_slice + newchar + back_slice
        return string



            




    