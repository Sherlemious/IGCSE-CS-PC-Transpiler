import sys

from Functions import FOR, PRINT,assignment, WHILE, IF, REPEAT
from Functions import *


Variables = {}

no = 0
File = open("F:\\Programming\\Python\\Projects\\IGCSE-CS-PC-Compiler\\To be translated", "r")

count = LineCounter(File)

for i in range(count):  # Iterates through the lines until no more lines are available
    Line = File.readline()
    if Line[0:5] == "PRINT":
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
