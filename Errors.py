from Main import *

class Error:
    def __init__(self,varname):
        self.printed=varname
    def isprint(self):
        print(self.printed)
        print(f"This error has been generated in Line number #{no}")       

VarNotPresent=Error("Variable Identifier does not exist.")

NoEqualSpaces=Error("Please make sure that there is a space " " character between each identifier(variable) operand, or an equal sign")

