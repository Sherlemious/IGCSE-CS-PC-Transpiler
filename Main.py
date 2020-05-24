import sys
from Functions import FOR, PRINT, assignment, WHILE, IF, REPEAT
from Functions import *

variables = {}
CurFlags = []
LineList = []
counter = 0

File = open("F:\\Programming\\Python\\Projects\\IGCSE-CS-PC-Compiler\\To be translated", "r")
FileList = list(File)
File.close()


for i in FileList:  # Iterates through the lines until no more lines are available
    Line = i
    
    if Line[0:5] == "PRINT":
        lst1 = Line.split()
        printed = ""
        for w in range(1, len(lst1)):

            word = lst1[w]
            end = int(len(word))
            if word in Variables and word[0] != "\"":  # This checks if it is a variable and if the variable exists
                printed += Variables[word]
            else:
                for c in range(end):
                    if w == 1 and c == 0 or w == len(lst1) - 1 and c == end - 1:
                        pass
                    else:
                        printed += word[c]
                printed += " "

        print(printed)

    elif Line[0:5] == "WHILE":
        # Defining the condition
        Lst2 = Line.split()
        if Lst2[1] in variables:
            toc1 = variables[Lst2[1]]
        elif type(Lst2[1]) == float or type(Lst2[1]) == int:
            toc1 = variables[Lst2[1]]
        op1 = Lst2[2]
        if Lst2[3] in variables:
            toc2 = variables[Lst2[3]]
        elif type(Lst2[3]) == float or type(Lst2[3]) == int:
            toc2 = variables[Lst2[3]]
        # Listing comparison scenarios for the Conditions
        if op1 == "=":
            CurFlags[counter] = toc1 == toc2
        elif op1 == ">":
            CurFlags[counter] = toc1 > toc2
        elif op1 == "<":
            CurFlags[counter] = toc1 < toc2
        elif op1 == "<=":
            CurFlags[counter] = toc1 <= toc2
        elif op1 == ">=":
            CurFlags[counter] = toc1 >= toc2

        else:
            print("There is an invalid operand")

        while Line[0:8] != "ENDWHILE" and CurFlags:
            if Line[0:5] == "PRINT":
                PRINT(Line)

            elif Line[0:5] == "WHILE":
                WHILE(file, CurFlags, counter, variables, Line)

            elif Line[0:6] == "REPEAT":
                pass

            elif Line[0:5] == "INPUT":
                variables[Line[6:len(Line) - 1]] = input()

            elif Line[0:3] == "FOR":
                FOR(Line, file)

            elif Line[0:2] == "IF":
                IF(Line, variables, CurFlags)

            # Assignment statement
            else:
                pass  # This part should carry out an assignment statement

            Lst2 = Line.split()
            if Lst2[1] in variables:
                toc1 = variables[Lst2[1]]
            elif type(Lst2[1]) == float or type(Lst2[1]) == int:
                toc1 = variables[Lst2[1]]
            op1 = Lst2[2]
            if Lst2[3] in variables:
                toc2 = variables[Lst2[3]]
            elif type(Lst2[3]) == float or type(Lst2[3]) == int:
                toc2 = variables[Lst2[3]]
            # Listing comparison scenarios for the Conditions
            if op1 == "=":
                CurFlags[counter] = toc1 == toc2
            elif op1 == ">":
                CurFlags[counter] = toc1 > toc2
            elif op1 == "<":
                CurFlags[counter] = toc1 < toc2
            elif op1 == "<=":
                CurFlags[counter] = toc1 <= toc2
            elif op1 == ">=":
                CurFlags[counter] = toc1 >= toc2

    elif Line[0:6] == "REPEAT":
        pass

    elif Line[0:5] == "INPUT":
        varwanted = Line.split()
        varwanted = varwanted[1]
        Variables[varwanted] = input()

    elif Line[0:3] == "FOR":
        Lst = Line.split()
        LCV = Lst[1]
        Start = int(Lst[3])
        End = int(Lst[5])

        while Lst[1] != "ENDFOR":
            st2 = counter
            end2 = counter
            LineList.append(Line)
            end2 += 1
        for ln in range(Start, End):
            for m in range(st2, end2):
                Lst = Line[m].split()

                if Line[0:5] == "PRINT":
                    lst1 = Line.split()
                    printed = ""
                    for w in range(1, len(lst1)):

                        word = lst1[w]
                        end = int(len(word))
                        if word in Variables and word[0] != "\"":  # This checks if it is a variable and if the variable exists
                            printed += Variables[word]
                        else:
                            for c in range(end):
                                if w == 1 and c == 0 or w == len(lst1) - 1 and c == end - 1:
                                    pass
                                else:
                                    printed += word[c]
                            printed += " "

                elif Line[0:5] == "WHILE":
                    WHILE(File, Flags, no, Variables, Line)

                elif Line[0:6] == "REPEAT":
                    REPEAT()  # Haven't added repeat

                elif Line[0:5] == "INPUT":
                    Variables[Line[6:len(Line) - 1]] = input()

                elif Line[0:3] == "FOR":
                    FOR(Line, File)

                elif Line[0:2] == "IF":
                    IF(Line, Variables, Flags)

                # Assignment statement
                else:
                    pass  # This part should carry out an assignment statement

    elif Line[0:2] == "IF":
        Lst2 = Line.split()
        if Lst2[1] in variables:
            toc1 = variables[Lst2[1]]
        elif type(Lst2[1]) == float or type(Lst2[1]) == int:
            toc1 = variables[Lst2[1]]
        op1 = Lst2[2]
        if Lst2[3] in variables:
            toc2 = variables[Lst2[3]]
        elif type(Lst2[3]) == float or type(Lst2[3]) == int:
            toc2 = variables[Lst2[3]]
        # Listing comparison scenarios for the
        if op1 == "=":
            flags.append(toc1 == toc2)
        elif op1 == ">":
            flags.append(toc1 > toc2)
        elif op1 == "<":
            flags.append(toc1 < toc2)
        elif op1 == "<=":
            flags.append(toc1 <= toc2)
        elif op1 == ">=":
            flags.append(toc1 >= toc2)
        else:
            OpInvalid.isprint()

    else:
        assignment()

    counter += 1