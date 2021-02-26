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


def take_input():
    x = input()
    x = find_type(x)
    return x


def find_type(Obj):
    try:
        if "." in Obj:
            Obj = float(Obj)
        else:
            Obj = int(Obj)
    except ValueError:
        obj = str(Obj)
    return Obj


def find_value(val):
    if val in Config.variables:
        try:
            toc = float(Config.variables[val])
        except ValueError:
            toc = Config.variables[val]
    elif "[" in val:
        toc = fetch_value(val)
    elif "\"" in val:
        toc = val[1:-1]
    else:
        try:
            toc = float(val)
            toc = float(val)
        except ValueError:
            pass
    return toc


def comp(val1, val2, operand):
    # First Variable or Number
    toc1 = find_value(val1)

    # Second Variable or Number
    toc2 = find_value(val2)
    # Comparison
    if operand in Config.op_list:
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
    elif lst[1] == "DIV" or lst[1] == "MOD":
        return comp(op_dict(lst[0], lst[2]), lst[2], lst[1])


# Removes the escape character at the end of all lines
def rem_end(the_list):
    for line in range(len(the_list)):
        the_list[line] = the_list[line].strip()


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


def assign(line_used):
    to_be_eval = ""
    lst = line_used.split()
    var = lst[0]
    pos_num = 0
    array = False
    string = False
    # Check for array
    A_S = var.find("[")
    if A_S == -1:
        if var not in Config.variables:
            Config.variables[var] = 0
    else:
        array = True
        pos_num = var[A_S + 1:-1]
        try:
            pos_num = int(pos_num)
        except ValueError:
            pos_num = Config.variables[pos_num]
        var = var[:A_S]
        if var not in Config.variables:
            Config.variables[var] = {}
        if pos_num not in Config.variables[var]:
            Config.variables[var][pos_num] = 0
    del lst[0:2]

    if lst[0] != "USERINPUT":
        for V in lst:
            if V[0] == '"' and V[-1] == '"':
                string = True
                to_be_eval += V[1:-1]
                continue
            elif "[" in str(V):
                to_be_eval += str(fetch_value(V))
                continue
            elif V in Config.variables:
                to_be_eval += str(Config.variables[V])
            elif isinstance(find_type(V), float) or isinstance(find_type(V), int):
                to_be_eval += str(V)
            elif V in Config.mops:
                to_be_eval += str(V)
            elif V == "DIV" or V == "MOD":
                if V == "MOD":
                    to_be_eval += "%"
                else:
                    to_be_eval += "//"
            else:
                to_be_eval += " " + str(V)
        if not string:
            try:
                to_be_eval = eval(to_be_eval)
            except ValueError:
                pass
            except NameError:
                pass
    else:
        to_be_eval = take_input()

    if array:
        Config.variables[var][pos_num] = to_be_eval
    else:
        Config.variables[var] = to_be_eval
