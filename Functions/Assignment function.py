from Main import Line, variables

global Line, variables


def ASSIGNMENT():
    tobeeval = ""
    eqfound = False
    lst3 = Line.split()
    for vr in lst3:
        if vr == "=" or eqfound:
            eqfound = True
        if eqfound:
            if vr in variables:
                tobeeval += str(variables[vr])
            elif isinstance(vr, int):
                tobeeval += vr
    variables[lst3[0]] = eval(tobeeval[1:])
