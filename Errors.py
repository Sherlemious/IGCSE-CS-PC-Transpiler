import Config
import sys


class Error:
    def __init__(self, Error_name):
        self.printed = Error_name

    def isprint(self):
        print(self.printed)
        print(f"This error has been generated in Line number #{Config.i}")
        #added system exit on error 
        sys.exit(-1)


VarNotPresent = Error("Variable Identifier does not exist.")

NoEqualSpaces = Error(
    "Please make sure that there is a space " " character between each identifier(variable) operand, or an equal sign")

OpInvalid = Error("There is an invalid operand")

LogInvalid = Error("There is an invalid logic gate")

Tocabsent = Error("There is an invalid operand. Please input a valid variable or number")

Backslash = Error("Please Do not use a backslash in a string : \\")
