def dataChecker(data, type):
    if type == "float" or type == "num":
        try: 
            float(data)
            return True
        except ValueError:
            return False
    elif type == "int":
        try:
            int(data)
            return True
        except ValueError:
            return False
    elif type == "str":
        try:
            str(data)
            return True
        except ValueError:
            return False