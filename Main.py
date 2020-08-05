import Commands as do
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
        do.PRINT(Config.Line)

    elif Config.Line[0:5] == "WHILE":
        do.WHILE()

    elif Config.Line[0:6] == "REPEAT":
        do.REPEAT()

    elif Config.Line[0:5] == "INPUT":
        do.INPUT(Config.Line)

    elif Config.Line[0:3] == "FOR":
        do.FOR()

    elif Config.Line[0:2] == "IF":
        do.IF()

    else:
        do.ASSIGNMENT(Config.Line)

    Config.counter += 1
    Config.i += 1
