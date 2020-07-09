from Main import Line, variables, counter, i, FileList, LineList

global Line, variables, counter, i, FileList, LineList


def FOR():
    global Line, variables, counter, i, FileList, LineList
    Lst = Line.split()
    LCV = Lst[1]
    Start = int(Lst[3])
    End = int(Lst[5])
    variables[LCV] = LCV
    while Lst[0] != "ENDFOR":
        st2 = counter
        end2 = counter
        i += 1
        Line = FileList[i]
        Lst = Line.split()
        if Lst[0] == "ENDFOR":
            break
        LineList.append(Line)
        end2 += 1
    Line = FileList[i]
    for con in range(Start, End + 1):
        variables[LCV] = con
        for lf in LineList:
            pass
