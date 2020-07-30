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
    for line in filename:
        counter += 1
    return counter


def comp(val1, val2, operand):
    Lst2 = Config.Line.split()
    # First Variable or Number
    if val1 in Config.variables:
        toc1 = Config.variables[val1]
    elif type(float(val1)) == float or type(int(val1)) == int:
        toc1 = float(val1)
    else:
        Errors.Tocabsent.isprint()
    # Second Variable or Number
    if val2 in Config.variables:
        toc2 = Config.variables[val2]
    elif type(float(val2)) == float or type(int(val2)) == int:
        toc2 = float(val2)
    # Comparison type
    if operand in Config.op_list:
        Config.Flags[Config.counter] = op_dict(toc1, toc2)[operand]
        return op_dict(toc1, toc2)[operand]
    else:
        Errors.OpInvalid.isprint()
