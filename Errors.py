import Config
no = 0


class Error:
    def __init__(self, Error_name):
        self.printed = Error_name

    def isprint(self):
        print(self.printed)
        print(f"This error has been generated in Line number #{no+1}")


VarNotPresent = Error("Variable Identifier does not exist.")

NoEqualSpaces = Error(
    "Please make sure that there is a space " " character between each identifier(variable) operand, or an equal sign")

OpInvalid = Error("There is an invalid operand")

Tocabsent = Error("There is an invalid operand. Please input a valid variable or number")

Backslash = Error("Please do not use a backslash in a string : \\")

