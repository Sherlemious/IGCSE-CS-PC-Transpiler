import sys

from Functions import FOR, PRINT,assignment, WHILE, IF, REPEAT
from Functions import *
sys.path.append('F:\\Programming\\Python\\Projects\\IGCSE-CS-PC-Compiler')


Variables = {}
Flags = {}
no = 0
File = open("F:\\Programming\\Python\\Projects\\IGCSE-CS-PC-Compiler\\To be translated", "r")
for Line in File:  # Iterates through the lines until no more lines are available
    if Line[0:5] == "PRINT":  # Prints what is supposed to be printed. I still have to work on printing variables after strings
        PRINT(Line)

    elif Line[0:5] == "WHILE":
        WHILE(File, Flags, no, Variables, Line)

    elif Line[0:6] == "REPEAT":
        pass

    elif Line[0:5] == "INPUT":
        Variables[Line[6:len(Line) - 1]] = input()

    elif Line[0:3] == "FOR":
        FOR(Line, File)

    elif Line[0:2] == "IF":
        IF(Line, Variables, Flags)

    else:
        assignment()

    no += 1
