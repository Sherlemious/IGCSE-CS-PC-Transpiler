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
    elif "[" in val1:
        fetch_value(val1)
    else:
        Errors.Absent.isprint()
    # Second Variable or Number
    if flag1:
        if val2 in Config.variables:
            toc2 = float(Config.variables[val2])
            flag2 = True
        elif type(float(val2)) == float or type(int(val2)) == int:
            toc2 = float(val2)
            flag2 = True
        elif "[" in val2:
            fetch_value(val2)
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
        flag1 = comp(exp1[0], exp1[2], exp1[1])
        flag2 = comp(exp2[0], exp2[2], exp2[1])
        logic_eval = log_dict(flag1, flag2)[logic_gate]
    else:
        Errors.LogInvalid.isprint()

    if logic_eval is not None:
        return log_dict(flag1, flag2)[logic_gate]


def compare(lst):
    if lst[0] == "IF" or lst[0] == "WHILE" or lst[0] == "UNTIL":
        del lst[0]
    if len(lst) == 3:
        return comp(lst[0], lst[2], lst[1])
    elif len(lst) == 7:
        return compExpressions(lst[0:3], lst[4:], lst[3])


# Removes the escape character at the end of all lines
def rem_end(the_list):
    for line in range(len(the_list)):
        the_list[line] = the_list[line].rstrip('\n')


# Creates a string that is appended to the objects list. This string is to be of a function class, where it is going
# to contain the attributes of the loop/ function
def object_gen():
    Config.Iteratables.append("Statement " + str(len(Config.Iteratables)))


def fetch_value(word):
    var = word
    A_S = var.find("[")
    pos_num = var[A_S + 1:-1]
    var = var[:A_S]
    try:
        pos_num = int(pos_num)
    except ValueError:
        pos_num = int(Config.variables[pos_num])
    return Config.variables[var][pos_num]


def listToString(s):
    Str = " "
    return Str.join(s)


def check_array_declaration(lst):
    st = lst[2:]
    st = listToString(st)
    if st[0] == "[" and st[-1] == "]":
        return True
    else:
        return False


def declare_array(lst):
    st = lst
    array_name = st[0]
    del st[0:2]
    old = listToString(st)
    lst = ""
    for ch in range(1, len(old) - 1):
        lst += str(old[ch])
    Config.variables[array_name] = {}
    added = ""
    c = 1
    for ch in range(len(lst)):
        if lst[ch] == ",":
            try:
                added = float(added)
            except ValueError:
                pass
            Config.variables[array_name][c] = added
            added = ""
            c += 1
        elif lst[ch] == " ":
            continue
        else:
            added += str(lst[ch])
    try:
        added = float(added)
    except ValueError:
        pass
    Config.variables[array_name][c] = added
