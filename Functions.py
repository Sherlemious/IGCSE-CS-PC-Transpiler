import Config
import Errors


def op_dict(toc1, toc2):
    return {
        "=": toc1 == toc2,
        ">": toc1 > toc2,
        "<": toc1 < toc2,
        "<=": toc1 <= toc2,
        ">=": toc1 >= toc2,
        "<>": toc1 != toc2
    }


def LineCounter(filename):
    counter = 0
    for _ in range(filename):
        counter += 1
    return counter


def comp(val1, val2, operand):
    # First Variable or Number
    flag1 = False
    flag2 = False
    if val1 in Config.variables:
        toc1 = Config.variables[val1]
        flag1 = True
    elif type(float(val1)) == float or type(int(val1)) == int:
        toc1 = float(val1)
        flag1 = True
    else:
        Errors.Tocabsent.isprint()
    # Second Variable or Number
    if flag1:
        if val2 in Config.variables:
            toc2 = Config.variables[val2]
            flag2 = True
        elif type(float(val2)) == float or type(int(val2)) == int:
            toc2 = float(val2)
            flag2 = True
        # Comparison type
        if flag1 and flag2:
            if operand in Config.op_list:
                Config.Flags[Config.counter] = op_dict(toc1, toc2)[operand]
                return op_dict(toc1, toc2)[operand]
            else:
                Errors.OpInvalid.isprint()



def Removeend(thelist):
    for line in range(len(thelist)):
        thelist[line] = thelist[line].rstrip('\n')
