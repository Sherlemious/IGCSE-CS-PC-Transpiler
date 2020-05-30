from Functions import *

# Variables
variables = {}
Flags = {}
LineList = []
counter = 0


# Functions
def IF():
    global Lst2, toc1, toc2, op1, Flags
    Lst2 = Line.split()
    # First Variable or Number
    if Lst2[1] in variables:
        toc1 = variables[Lst2[1]]
    elif type(float(Lst2[1])) == float or type(int(Lst2[1])) == int:
        toc1 = variables[Lst2[1]]
    else:
        Tocabsent.isprint()
    # Second Variable or Number
    if Lst2[3] in variables:
        toc2 = variables[Lst2[3]]
    elif type(Lst2[3]) == float or type(Lst2[3]) == int:
        toc2 = variables[Lst2[3]]
    # Comparison type
    if Lst2[2] == ("=" or ">" or "<" or "<=" or ">=" or "<>"):
        op1 = Lst2[2]
        if op1 == "=":
            Flags[counter] = toc1 == toc2
        elif op1 == ">":
            Flags[counter] = toc1 > toc2
        elif op1 == "<":
            Flags[counter] = toc1 < toc2
        elif op1 == "<=":
            Flags[counter] = toc1 <= toc2
        elif op1 == ">=":
            Flags[counter] = toc1 >= toc2
        elif op1 == "<>":
            Flags[counter] = toc1 != toc2
        else:
            OpInvalid.isprint()
    else:
        OpInvalid.isprint()


# Opening the file
File = open("F:\\Programming\\Python\\Projects\\IGCSE-CS-PC-Compiler\\To be translated", "r")
FileList = list(File)
File.close()
# Manipulating File Done

for i in range(len(FileList)):  # Iterates through the lines until no more lines are available
    Line = FileList[i]

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
        IF()

        Line = FileList[i]
        Lst = Line.split()
        LineList.append(Line)
        end2 += 1

        while Lst[0] != "ENDWHILE":
            st3 = counter
            end3 = counter
            i += 1
            Line = FileList[i]
            Lst = Line.split()
            LineList.append(Line)
            end3 += 1

        while Flags[counter]:
            for lf in LineList:

                if lf[0:5] == "PRINT":
                    lst1 = lf.split()
                    printed = ""
                    for w in range(1, len(lst1)):

                        word = lst1[w]

                        end = int(len(word))
                        if word in Variables and word[
                            0] != "\"":  # This checks if it is a variable and if the variable exists
                            printed += Variables[word]
                        else:
                            for c in range(end):
                                if w == 1 and c == 0 or w == len(lst1) - 1 and c == end - 1:
                                    pass
                                else:
                                    printed += word[c]
                            printed += " "
                        print(printed)

                elif lf[0:5] == "WHILE":
                    WHILE(File, Flags, no, Variables, Line)

                elif lf[0:6] == "REPEAT":
                    REPEAT()  # Haven't added repeat

                elif lf[0:5] == "INPUT":
                    Variables[Line[6:len(Line) - 1]] = input()

                elif lf[0:3] == "FOR":
                    FOR(Line, File)

                elif lf[0:2] == "IF":
                    IF(Line, Variables, Flags)
            IF()

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

        while Lst[0] != "ENDFOR":
            st2 = counter
            end2 = counter
            i += 1
            Line = FileList[i]
            Lst = Line.split()
            LineList.append(Line)
            end2 += 1

        for con in range(Start, End):
            for lf in LineList:

                if lf[0:5] == "PRINT":
                    lst1 = lf.split()
                    printed = ""
                    for w in range(1, len(lst1)):

                        word = lst1[w]

                        end = int(len(word))
                        if word in Variables and word[
                            0] != "\"":  # This checks if it is a variable and if the variable exists
                            printed += Variables[word]
                        else:
                            for c in range(end):
                                if w == 1 and c == 0 or w == len(lst1) - 1 and c == end - 1:
                                    pass
                                else:
                                    printed += word[c]
                            printed += " "
                        print(printed)

                elif lf[0:5] == "WHILE":
                    WHILE(File, Flags, no, Variables, Line)

                elif lf[0:6] == "REPEAT":
                    REPEAT()  # Haven't added repeat

                elif lf[0:5] == "INPUT":
                    Variables[Line[6:len(Line) - 1]] = input()

                elif lf[0:3] == "FOR":
                    FOR(Line, File)

                elif lf[0:2] == "IF":
                    IF(Line, Variables, Flags)

                # Assignment statement
                else:
                    pass  # This part should carry out an assignment statement

    elif Line[0:2] == "IF":
        IF()

    else:
        assignment()

    counter += 1
