import Commands as cc
# Variables
import Config

# Opening the file
File = open("F:\\Projects\\Applications\\IGCSE-CS-PC-Compiler\\To be translated", "r")
Config.FileList = list(File)
File.close()
# Manipulating File Done

while Config.i < len(Config.FileList):  # Iterates through the lines until no more lines are available
    Config.Line = Config.FileList[Config.i]
    Config.Line = Config.Line.rstrip('\n')

    if Config.Line[0:5] == "PRINT":
        cc.PRINT()

    elif Config.Line[0:5] == "WHILE":
        cc.WHILE()

    elif Config.Line[0:6] == "REPEAT":
        cc.REPEAT()

    elif Config.Line[0:5] == "INPUT":
        cc.INPUT()

    elif Config.Line[0:3] == "FOR":
        cc.FOR()

    elif Config.Line[0:2] == "IF":
        cc.IF()

    else:
        cc.ASSIGNMENT(Config.Line)

    Config.counter += 1
    Config.i += 1
