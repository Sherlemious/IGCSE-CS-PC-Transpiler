import Errors
import Functions as Fun
import Config
import Classes


def main(lineused):

    if lineused[0:5] == "PRINT":
        PRINT(lineused)

    elif lineused[0:5] == "WHILE":
        WHILE()

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
        print(Fun.comp(Lst2[1], Lst2[3], Lst2[2]))
    elif len(Lst2) == 8:
        if Lst2[5] == "AND":
            if Fun.comp(Lst2[1], Lst2[3], Lst2[2]) and Fun.comp(Lst2[5], Lst2[7], Lst2[6]):
                while Lst2[0] != "ENDIF":
                    main(lineused)
        elif Lst2[5] == "OR":
            try:
                if Fun.comp(Lst2[1], Lst2[3], Lst2[2]) or Fun.comp(Lst2[5], Lst2[7], Lst2[6]):
                    pass
            except IndexError:
                Errors.OpInvalid.isprint()


def listnumgen():
    Config.iteratables.append("Loop " + str(len(Config.iteratables)))


def FOR():
    listnumgen()
    linelist = []
    if len(Config.iteratables) == 1:
        curlinesplit = Config.Line.split()
        lcv = curlinesplit[1]
        Config.variables[lcv] = lcv
        Start = int(curlinesplit[3])
        End = int(curlinesplit[5])+1
        while True:
            Config.i += 1
            try:
                Config.Line = Config.FileList[Config.i]
                linelist.append(Config.Line)
                curlinesplit = Config.Line.split()
            except IndexError:
                pass
            if curlinesplit[0] == "NEXT" and curlinesplit[1] == lcv:
                del linelist[-1]
                break
        Config.i += 1
        try:
            Config.Line = Config.FileList[Config.i]
        except IndexError:
            pass

        Config.iteratables[-1] = Classes.Loop(linelist=linelist, LCV=lcv, start=Start, end=End)
        for i in range(Config.iteratables[-1].start, Config.iteratables[-1].end):
            Config.variables[lcv] = i
            while Config.iteratables[-1].curlinenumber < len(Config.iteratables[-1].linelist):
                curline = Config.iteratables[-1].linelist[Config.iteratables[-1].curlinenumber]
                main(curline)
                Config.iteratables[-1].curlinenumber += 1
            Config.iteratables[-1].curlinenumber = 0
        del Config.iteratables[-1]
    else:
        curlinesplit = Config.iteratables[-2].linelist[Config.iteratables[-2].curlinenumber].split()
        lcv = curlinesplit[1]
        Config.variables[lcv] = lcv
        Start = int(curlinesplit[3])
        End = int(curlinesplit[5])+1
        while True:
            Config.iteratables[-2].curlinenumber += 1
            try:
                Config.iteratables[-2].curline = Config.iteratables[-2].linelist[Config.iteratables[-2].curlinenumber]
                linelist.append(Config.iteratables[-2].curline)
                curlinesplit = Config.iteratables[-2].curline.split()
            except IndexError:
                pass
            if curlinesplit[0] == "NEXT" and curlinesplit[1] == lcv:
                del linelist[-1]
                break
        #Config.iteratables[-2].curlinenumber += 1
        try:
            Config.iteratables[-2].curline = Config.iteratables[-2].linelist[Config.iteratables[-2].curlinenumber]
        except IndexError:
            pass

        Config.iteratables[-1] = Classes.Loop(linelist=linelist, LCV=lcv, start=Start, end=End)
        for i in range(Config.iteratables[-1].start, Config.iteratables[-1].end):
            Config.variables[lcv] = i
            while Config.iteratables[-1].curlinenumber < len(Config.iteratables[-1].linelist):
                curline = Config.iteratables[-1].linelist[Config.iteratables[-1].curlinenumber]
                main(curline)
                Config.iteratables[-1].curlinenumber += 1
            Config.iteratables[-1].curlinenumber = 0
        del Config.iteratables[-1]


def WHILE():
    pass


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
