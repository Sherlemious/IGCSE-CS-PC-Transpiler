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


def listnumgen():
    Config.iteratables.append("Statement " + str(len(Config.iteratables)))


def IF(lineused):
    listnumgen()
    linelisttrue = []
    linelistfalse = []
    elsestarter = 1
    if len(Config.iteratables) == 1:
        lst = Config.Line.split()
        cond = lst
        while True:
            Config.i += 1
            try:
                Config.Line = Config.FileList[Config.i]
                if Config.Line != "THEN":
                    linelisttrue.append(Config.Line)
                curlinesplit = Config.Line.split()
                elsestarter += 1
                if curlinesplit[0] == "ELSE" or curlinesplit[0] == "ENDIF":
                    del linelisttrue[-1]
                    if curlinesplit[0] == "ELSE":
                        while True:
                            Config.i += 1
                            try:
                                Config.Line = Config.FileList[Config.i]
                                linelistfalse.append(Config.Line)
                                curlinesplit = Config.Line.split()
                            except IndexError:
                                pass
                            if curlinesplit[0] == "ENDIF":
                                del linelistfalse[-1]
                                break
                        ending = Config.i
                        break

            except IndexError:
                pass

        if len(cond) == 4:
            Config.iteratables[-1] = Classes.IFSTATEMENT(condition=cond, iffalse=linelistfalse, iftrue=linelisttrue,
                                                         elsestarter=elsestarter, falsending=ending)
            Config.iteratables[-1].condition = Fun.comp(cond[1], cond[3], cond[2])
            if Config.iteratables[-1].condition:
                while Config.iteratables[-1].curlinenumber < len(Config.iteratables[-1].iftrue):
                    curline = Config.iteratables[-1].iftrue[Config.iteratables[-1].curlinenumber]
                    main(curline)
                    Config.iteratables[-1].curlinenumber += 1
            else:
                Config.iteratables[-1].curline = Config.iteratables[-1].elsestarter
                while Config.iteratables[-1].curline < (Config.iteratables[-1].falsending-1):
                    curline = Config.iteratables[-1].iffalse[Config.iteratables[-1].elsecurline]
                    main(curline)
                    Config.iteratables[-1].curline += 1
                    Config.iteratables[-1].elsecurline += 1

        elif len(lst) == 8:
            if lst[5] == "AND":
                if Fun.comp(lst[1], lst[3], lst[2]) and Fun.comp(lst[5], lst[7], lst[6]):
                    while lst[0] != "ENDIF":
                        main(lineused)
            elif lst[5] == "OR":
                try:
                    if Fun.comp(lst[1], lst[3], lst[2]) or Fun.comp(lst[5], lst[7], lst[6]):
                        pass
                except IndexError:
                    Errors.OpInvalid.isprint()


def FOR():
    listnumgen()
    linelist = []
    if len(Config.iteratables) == 1:
        curlinesplit = Config.Line.split()
        lcv = curlinesplit[1]
        Config.variables[lcv] = lcv
        start = int(curlinesplit[3])
        end = int(curlinesplit[5]) + 1
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

    else:
        curlinesplit = Config.iteratables[-2].linelist[Config.iteratables[-2].curlinenumber].split()
        lcv = curlinesplit[1]
        Config.variables[lcv] = lcv
        start = int(curlinesplit[3])
        end = int(curlinesplit[5]) + 1
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
        # Config.iteratables[-2].curlinenumber += 1 # I have no idea why removing this line works but it does.
        try:
            Config.iteratables[-2].curline = Config.iteratables[-2].linelist[Config.iteratables[-2].curlinenumber]
        except IndexError:
            pass

    Config.iteratables[-1] = Classes.FORLOOP(linelist=linelist, LCV=lcv, start=start, end=end)
    for i in range(Config.iteratables[-1].start, Config.iteratables[-1].end):
        Config.variables[lcv] = i
        while Config.iteratables[-1].curlinenumber < len(Config.iteratables[-1].linelist):
            curline = Config.iteratables[-1].linelist[Config.iteratables[-1].curlinenumber]
            main(curline)
            Config.iteratables[-1].curlinenumber += 1
        Config.iteratables[-1].curlinenumber = 0
    del Config.iteratables[-1]


# TODO: Add the code to the WHILE and REPEAT FUNCTIONS

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
            if word[-1] == "\"":
                for c in range(end - 1):
                    if w == 1 and c == 0:
                        pass
                    else:
                        printed += word[c]
                printed += " "
            else:
                for c in range(end):
                    if w == 1 and c == 0:
                        pass
                    else:
                        printed += word[c]
                printed += " "

    print(printed)
