import Commands as Do
import Config
import Functions as Fun

# Opening the file
File = open("F:\\Projects\\Applications\\IGCSE-CS-PC-Transpiler\\To be translated", "r")
Config.FileList = list(File)
File.close()
# Manipulating File Done
Fun.Removeend(Config.FileList)

while Config.i < len(Config.FileList):  # Iterates through the lines until no more lines are available
    Config.Line = Config.FileList[Config.i]

    if Config.Line[0:5] == "PRINT":
        Do.PRINT(Config.Line)
        continue

    elif Config.Line[0:5] == "WHILE":
        Do.WHILE(Config.Line)
        continue

    elif Config.Line[0:6] == "REPEAT":
        Do.REPEAT()
        continue

    elif Config.Line[0:5] == "INPUT":
        Do.INPUT(Config.Line)
        continue

    elif Config.Line[0:3] == "FOR":
        Do.FOR()
        continue

    elif Config.Line[0:2] == "IF":
        Do.IF(Config.Line)
        continue

    else:
        Do.ASSIGNMENT(Config.Line)

    Config.counter += 1
    Config.i += 1
