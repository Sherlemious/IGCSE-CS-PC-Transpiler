import os
import Commands as Do
import Config
import Functions as Fun

# Opening the file
dirname = os.path.dirname(__file__)
dirname += "\\To be translated"
File = open(dirname, "r")
Config.FileList = list(File)
File.close()

# Manipulating File Done
Fun.Removeend(Config.FileList)

while Config.i < len(Config.FileList):
    Config.Line = Config.FileList[Config.i]
    splitlines = Config.Line.split()

    if Config.Line[0:5] == "PRINT":
        Do.PRINT(Config.Line)

    elif Config.Line[0:5] == "WHILE":
        Do.WHILE()

    elif Config.Line[0:6] == "REPEAT":
        Do.REPEAT()

    elif Config.Line[0:5] == "INPUT":
        Do.INPUT(Config.Line)

    elif Config.Line[0:3] == "FOR":
        Do.FOR()
        continue

    elif Config.Line[0:2] == "IF":
        Do.IF()

    elif Config.Line[0:2] == "//":
        pass

    elif splitlines[1] == "=":
        Do.ASSIGNMENT(Config.Line)

    Config.counter += 1
    Config.i += 1
