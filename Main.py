import Commands as Do
import Config

# Opening the file
File = open("F:\\Projects\\Applications\\IGCSE-CS-PC-Transpiler\\To be translated", "r")
Config.FileList = list(File)
File.close()
# Manipulating File Done

while Config.i < len(Config.FileList):  # Iterates through the lines until no more lines are available
    Config.Line = Config.FileList[Config.i]
    Config.Line = Config.Line.rstrip('\n')

    if Config.Line[0:5] == "PRINT":
        Do.PRINT(Config.Line)

    elif Config.Line[0:5] == "WHILE":
        Do.WHILE(Config.Line)

    elif Config.Line[0:6] == "REPEAT":
        Do.REPEAT()

    elif Config.Line[0:5] == "INPUT":
        Do.INPUT(Config.Line)

    elif Config.Line[0:3] == "FOR":
        Do.FOR()

    elif Config.Line[0:2] == "IF":
        Do.IF(Config.Line)

    else:
        Do.ASSIGNMENT(Config.Line)

    Config.counter += 1
    Config.i += 1
