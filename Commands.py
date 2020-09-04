import Errors
import functions as f
import Config


def main(lineused):
    lineused = lineused.rstrip('\n')

    if lineused[0:5] == "PRINT":
        PRINT(lineused)

    elif lineused[0:5] == "WHILE":
        WHILE(Config.i)

    elif lineused[0:6] == "REPEAT":
        REPEAT()

    elif lineused[0:5] == "INPUT":
        INPUT(lineused)

    elif lineused[0:3] == "FOR":
        FOR()

    elif lineused[0:2] == "IF":
        IF(lineused)

    else:
        ASSIGNMENT(lineused)


def IF(lineused):
    Lst2 = Config.Line.split()
    if len(Lst2) == 4:
        print(f.comp(Lst2[1], Lst2[3], Lst2[2]))
    elif len(Lst2) == 8:
        if Lst2[5] == "AND":
            if f.comp(Lst2[1], Lst2[3], Lst2[2]) and f.comp(Lst2[5], Lst2[7], Lst2[6]):
                while Lst2[0] != "ENDIF":
                    main(lineused)
        elif Lst2[5] == "OR":
            try:
                if f.comp(Lst2[1], Lst2[3], Lst2[2]) or f.comp(Lst2[5], Lst2[7], Lst2[6]):
                    pass
            except IndexError:
                Errors.OpInvalid.isprint()


def FOR():
    curline = Config.Line.split()
    LCV = curline[1]
    Start = int(curline[3])
    End = int(curline[5])
    Config.variables[LCV] = LCV
    while curline[0] != "ENDFOR":
        end2: int = Config.counter
        Config.i += 1
        try:
            Config.Line = Config.FileList[Config.i]
            Config.Line = Config.Line.rstrip('\n')
            curline = Config.Line.split()
        except IndexError:
            pass
        if curline[0] == "ENDFOR":
            break
        Config.LineList.append(Config.Line)
        end2 += 1
    try:
        Config.Line = Config.FileList[Config.i + 1]
    except IndexError:
        pass
    for con in range(Start, End + 1):
        Config.variables[LCV] = con
        for lf in Config.LineList:
            main(lf)


def WHILE(lineused):
    # Defining the condition
    end2 = 0
    IF(lineused)

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
            main(lf)
        # Recheck condition


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


def INPUT(lineused):
    varwanted = lineused.split()
    varwanted = varwanted[1]
    Config.variables[varwanted] = input()


def PRINT(lineused):
    lst1 = lineused.split()
    printed = ""
    for w in range(1, len(lst1)):

        word = lst1[w]
        end = int(len(word))
        if word in Config.variables and word[0] != "\"":  # This checks if it is a variable and if the variable exists
            printed += str(Config.variables[word])
        else:
            for c in range(end-1):
                if w == 1 and c == 0:
                    pass
                else:
                    printed += word[c]
            printed += " "

    print(printed)
