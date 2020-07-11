import Errors
import functions as f
import Config


def IF():
    Lst2 = Config.Line.split()
    # First Variable or Number
    if Lst2[1] in Config.variables:
        toc1 = Config.variables[Lst2[1]]
    elif type(float(Lst2[1])) == float or type(int(Lst2[1])) == int:
        toc1 = Config.variables[Lst2[1]]
    else:
        Errors.Tocabsent.isprint()
    # Second Variable or Number
    if Lst2[3] in Config.variables:
        toc2 = Config.variables[Lst2[3]]
    elif type(Lst2[3]) == float or type(Lst2[3]) == int:
        toc2 = Config.variables[Lst2[3]]
    # Comparison type
    if Lst2[2] in Config.op_list:
        Config.Flags[Config.counter] = f.op_dict(toc1, toc2)[Lst2[2]]
    else:
        Errors.OpInvalid.isprint()


def FOR():
    Lst = Config.Line.split()
    LCV = Lst[1]
    Start = int(Lst[3])
    End = int(Lst[5])
    Config.variables[LCV] = LCV
    while Lst[0] != "ENDFOR":
        end2: int = Config.counter
        Config.i += 1
        Config.Line = Config.FileList[Config.i]
        Config.Line = Config.Line.rstrip('\n')
        Lst = Config.Line.split()
        if Lst[0] == "ENDFOR":
            break
        Config.LineList.append(Config.Line)
        end2 += 1
    Config.Line = Config.FileList[Config.i + 1]
    for con in range(Start, End + 1):
        Config.variables[LCV] = con
        for lf in Config.LineList:
            if lf[0:5] == "PRINT":
                PRINT()

            elif lf[0:5] == "WHILE":
                WHILE()

            elif lf[0:6] == "REPEAT":
                REPEAT()

            elif lf[0:5] == "INPUT":
                INPUT()

            elif lf[0:3] == "FOR":
                FOR()

            elif lf[0:2] == "IF":
                IF()

            else:
                ASSIGNMENT(lf)


def WHILE():
    # Defining the condition
    end2 = 0
    IF()

    Line = Config.FileList[Config.i]
    Lst = Line.split()
    Config.LineList.append(Line)
    end2 += 1

    while Lst[0] != "ENDWHILE":
        end3 = Config.counter
        Config.i += 1
        Line = Config.FileList[Config.i]
        Lst = Line.split()
        Config.LineList.append(Line)
        end3 += 1

    while Config.Flags[Config.counter]:
        for lf in Config.LineList:
            if Line[0:5] == "PRINT":
                PRINT()

            elif Line[0:5] == "WHILE":
                WHILE()

            elif Line[0:6] == "REPEAT":
                REPEAT()

            elif Line[0:5] == "INPUT":
                INPUT()

            elif Line[0:3] == "FOR":
                FOR()

            elif Line[0:2] == "IF":
                IF()

            else:
                ASSIGNMENT(lf)
        IF()


def REPEAT():
    pass


def ASSIGNMENT(lineused):
    tobeeval = ""
    eqfound = False
    lst3 = lineused.split()
    for vr in lst3:
        try:
            vr = int(vr)
        except ValueError:
            pass
        if vr == '=' or eqfound:
            eqfound = True
        if eqfound:
            if vr in Config.variables:
                tobeeval += str(Config.variables[vr])
            elif isinstance(vr, int):
                tobeeval += str(vr)
            elif vr in Config.mops:
                tobeeval += str(vr)
    Config.variables[lst3[0]] = eval(tobeeval)


def INPUT():
    varwanted = Config.Line.split()
    varwanted = varwanted[1]
    Config.variables[varwanted] = input()


def PRINT():
    lst1 = Config.Line.split()
    printed = ""
    for w in range(1, len(lst1)):

        word = lst1[w]
        end = int(len(word))
        if word in Config.variables and word[0] != "\"":  # This checks if it is a variable and if the variable exists
            printed += str(Config.variables[word])
        else:
            for c in range(end):
                if w == 1 and c == 0:
                    pass
                else:
                    printed += word[c]
            printed += " "

    print(printed)
