import Config
import sys


class Error:
    def __init__(self, error_name):
        self.printed = error_name

    def isprint(self):
        print(self.printed)
        print(f"This error has been generated in Line number #{Config.Iteratables[0].line_number}")
        sys.exit(-1)


VarNotPresent = Error("Variable Identifier does not exist.")

NoEqualSpaces = Error(
    "Please make sure that there is a space " " character between each identifier(variable) operand, or an equal sign")

OpInvalid = Error("There is an invalid operand")

LogInvalid = Error("There is an invalid logic gate")

Absent = Error("There is an invalid operand. Please input a valid variable or number")

Backslash = Error("Please Do not use a backslash in a string : \\")
