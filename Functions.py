import Classes
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


def log_dict(exp1, exp2):
    return {
        "AND": exp1 and exp2,
        "OR": exp1 or exp2,
        "XOR": exp1 != exp2,
        "NAND": not (exp1 and exp2),
        "NOR": not (exp1 or exp2)
    }


def comp(val1, val2, operand):
    # First Variable or Number
    flag1 = False
    flag2 = False
    if val1 in Config.variables:
        toc1 = float(Config.variables[val1])
        flag1 = True
    elif type(float(val1)) == float or type(int(val1)) == int:
        toc1 = float(val1)
        flag1 = True
    else:
        Errors.Tocabsent.isprint()
    # Second Variable or Number
    if flag1:
        if val2 in Config.variables:
            toc2 = float(Config.variables[val2])
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


# Compares two expressions by using comp function
def compExpressions(exp1, exp2, logic_gate):
    logic_eval = None
    if logic_gate in Config.logic_list:
        # expressions should be passed in as array in form [val1,val2,operand]
        flag1 = comp(exp1[0], exp1[1], exp1[2])
        flag2 = comp(exp2[0], exp2[1], exp2[2])
        logic_eval = log_dict(flag1, flag2)[logic_gate]
    else:
        Errors.LogInvalid.isprint()

    if logic_eval is not None:
        return log_dict(flag1, flag2)[logic_gate]


def rem_end(the_list):
    for line in range(len(the_list)):
        the_list[line] = the_list[line].rstrip('\n')


def object_gen():
    Config.iteratables.append("Statement " + str(len(Config.iteratables)))


def check_opener_ending(line):
    cm = line.split()[0]
    if cm == "IF":
        Classes.Loop_Counts.If += 1
    else:
        if cm == "ENDIF":
            Classes.Loop_Counts.If -= 1
        else:
            if cm == "WHILE":
                Classes.Loop_Counts.While += 1
            else:
                if cm == "ENDWHILE":
                    Classes.Loop_Counts.While -= 1
                else:
                    if cm == "REPEAT":
                        Classes.Loop_Counts.Repeat += 1
                    else:
                        if cm == "UNTIL":
                            Classes.Loop_Counts.Repeat -= 1


# Switch cases
# def Inc_If():
#     Classes.Loop_Counts.If += 1
#
#
# def Dec_If():
#     Classes.Loop_Counts.If -= 1
#
#
# def Inc_While():
#     Classes.Loop_Counts.While += 1
#
#
# def Dec_While():
#     Classes.Loop_Counts.While -= 1
#
#
# def Inc_Repeat():
#     Classes.Loop_Counts.Repeat += 1
#
#
# def Dec_Repeat():
#     Classes.Loop_Counts.Repeat -= 1
#
#
# def check_opener_ending(line):
#     line = line.strip()
#     cases = {
#         "IF": Inc_If(),
#         "ENDIF": Dec_If(),
#         "WHILE": Inc_While(),
#         "ENDWHILE": Dec_While(),
#         "REPEAT": Inc_Repeat(),
#         "UNTIL": Dec_Repeat(),
#     }
#     function = cases.get(line[0])
#     return function
