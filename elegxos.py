class ValueTooSmallError(Exception):
    def __init__(self, val, message):
        self.val = val
        self.message = message

    def __str__(self):
        return f"{self.message}:{str(self.val)} is too small"
    
class ValueTooLargeError(Exception):
    def __init__(self, val, message):
        self.val = val
        self.message = message

    def __str__(self):
        return f"{self.message}:{str(self.val)} is too large"

"""class NotMultipleOfFiveError(Exception):
    def __init__(self, val, message):
        self.val = val
        self.message = message

    def __str__(self):
        return f"{self.message}:{str(self.val)} is not a multiple of 5"""
    


def get_integer(text):
    while True:
        try:
            number = input(text)
            if number == "":
                raise ValueError("No digits entered.")
            elif number.isalpha():
                raise ValueError("Wrong Input. Only digits please.")
            elif number.isnumeric() == False:
                raise ValueError("Wrong Input. Only integers please.") 
        except ValueError as v:
            print(v)
        except Exception as e:
            print(e)
        else:
            return int(number)
            break


def get_integer_con(start, stop):
    while True:
        try:
            number = input(f"Παρακαλώ εισάγετε έναν αριθμό ανάμεσα στις τίμες {start} και {stop}: ")
            if number == "":
                raise ValueError("No digits entered.")
            elif number.isalpha():
                raise ValueError("Wrong Input. Only digits please.")
            elif number.isnumeric() == False:
                raise ValueError("Wrong Input. Only integers please.")
            
            number = int(number)
            if number < start:
                raise ValueTooSmallError(number, "ValueTooSmallError")
            elif number > stop:
                raise ValueTooLargeError(number, "ValueTooLargeError")
            #elif number % 5 != 0:
                #raise NotMultipleOfFiveError(number, "NotMultipleOfFiveError")

        except ValueError as v:
            print(v)
        except Exception as e:
            print(e)
        else:
            return number
            break

def get_string(input_text):
    while True:
        try:
            my_str = input(input_text)
            if my_str.isalpha() == False:
                raise ValueError("Only letters allowed")
            elif len(my_str) == 0:
                raise ValueError("You haven't type anything yet.")
        except ValueError as v:
            print(v)
        except ValueError as e:
            print(e)
        else:
            return my_str
            break

