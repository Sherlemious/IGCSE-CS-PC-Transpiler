import Errors
import functions as f
import Config
import Main

def IF():
    Lst2 = Config.Line.split()
    if len(Lst2) == 4:
        print(f.comp(Lst2[1], Lst2[3], Lst2[2]))
    elif len(Lst2) == 8:
        if Lst2[5] == "AND":
            if f.comp(Lst2[1], Lst2[3], Lst2[2]) and f.comp(Lst2[5], Lst2[7], Lst2[6]):
                while Lst2[0] != "ENDIF":
                    Main.main()
        elif Lst2[5] == "OR":
            if f.comp(Lst2[1], Lst2[3], Lst2[2]) or f.comp(Lst2[5], Lst2[7], Lst2[6]):
                pass

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
            Main.main(lf)


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
            Main.main(lf)
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
