from Main import variables, Line

global variables, Line


def INPUT():
    varwanted = Line.split()
    varwanted = varwanted[1]
    variables[varwanted] = input()
