from Functions import op_dict, op_list
from Main import Line, variables, counter, Flags
from Errors import *

global Flags


def IF():
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
    if Lst2[2] in op_list:
        Flags[counter] = op_dict(toc1, toc2)[Lst2[2]]
    else:
        OpInvalid.isprint()
