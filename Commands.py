import Functions as Fun
import Config
import Classes


def main(line_used):
    if line_used[0:5] == "PRINT":
        PRINT(line_used)

    elif line_used[0:5] == "WHILE":
        WHILE()

    elif line_used[0:6] == "REPEAT":
        REPEAT()

    elif line_used[0:5] == "INPUT":
        INPUT(line_used)

    elif line_used[0:3] == "FOR":
        FOR()

    elif line_used[0:2] == "IF":
        IF()

    else:
        ASSIGNMENT(line_used)


def IF():
    Fun.object_gen()
    Config.iteratables[-1] = Classes.IF_STATEMENT()

    found_endif = False
    alt_lines = True
    line_list = []

    line_split = Config.iteratables[-2].line_list[Config.iteratables[-2].line_number].split()

    if line_split[-1] == "THEN":
        del line_split[-1]
    else:
        Config.iteratables[-2].line_number += 1

    Config.iteratables[-1].condition = line_split
    cond = Config.iteratables[-1].condition
    if len(cond) == 4:
        Config.iteratables[-1].condition = Fun.comp(cond[1], cond[3], cond[2])

    if Config.iteratables[-1].condition:

        while True:

            Config.iteratables[-2].line_number += 1
            try:
                Config.iteratables[-2].cur_line = Config.iteratables[-2].line_list[Config.iteratables[-2].line_number]

                line_list.append(Config.iteratables[-2].cur_line)
                line_split = Config.iteratables[-2].cur_line.split()

                if line_split[0] == "IF":
                    Classes.Loop_Counts.If += 1

                if line_split[0] == "ENDIF" and Classes.Loop_Counts.If == 0:
                    found_endif = True
                    del line_list[-1]
                    break

                if line_split[0] == "ELSE" and Classes.Loop_Counts.If == 0:
                    del line_list[-1]
                    break

                if line_split[0] == "ENDIF":
                    Classes.Loop_Counts.If -= 1

            except IndexError:
                pass

        Config.iteratables[-1].line_list = line_list
        while not found_endif:
            Config.iteratables[-2].line_number += 1
            Config.iteratables[-2].cur_line = Config.iteratables[-2].line_list[Config.iteratables[-2].line_number]
            line_split = Config.iteratables[-2].cur_line.split()
            if line_split[0] == "IF":
                Classes.Loop_Counts.If += 1
            if line_split[0] == "ENDIF":
                if Classes.Loop_Counts.If == 0:
                    break
                else:
                    Classes.Loop_Counts.If -= 1

    else:
        while Classes.Loop_Counts.If > 1 and line_split[0] != "ELSE":
            Config.iteratables[-2].line_number += 1
            Config.iteratables[-2].cur_line = Config.iteratables[-2].line_list[Config.iteratables[-2].line_number]
            line_split = Config.iteratables[-2].cur_line.split()
            if line_split[0] == "IF":
                Classes.Loop_Counts.If += 1
            if line_split[0] == "ENDIF":
                Classes.Loop_Counts.If -= 1
            if Classes.Loop_Counts.If == 1 and line_split[0] != "ENDIF":
                alt_lines = False
                break

        while Classes.Loop_Counts.If > 0 and line_split[0] != "ENDIF" and alt_lines:

            Config.iteratables[-2].line_number += 1
            try:
                Config.iteratables[-2].cur_line = Config.iteratables[-2].line_list[Config.iteratables[-2].line_number]

                line_list.append(Config.iteratables[-2].cur_line)
                line_split = Config.iteratables[-2].cur_line.split()

                if line_split[0] == "IF":
                    Classes.Loop_Counts.If += 1
                if line_split[0] == "ENDIF":
                    Classes.Loop_Counts.If -= 1

            except IndexError:
                pass
        Config.iteratables[-1].line_list = line_list

    while Config.iteratables[-1].line_number < len(Config.iteratables[-1].line_list):
        cur_line = Config.iteratables[-1].line_list[Config.iteratables[-1].line_number]
        main(cur_line)
        Config.iteratables[-1].line_number += 1


def FOR():
    Fun.object_gen()
    line_list = []

    cur_line_split = Config.iteratables[-2].line_list[Config.iteratables[-2].line_number].split()
    lcv = cur_line_split[1]
    Config.variables[lcv] = lcv
    start = int(cur_line_split[3])
    end = int(cur_line_split[5]) + 1
    while True:
        Config.iteratables[-2].line_number += 1
        try:
            Config.iteratables[-2].cur_line = Config.iteratables[-2].line_list[Config.iteratables[-2].line_number]
            line_list.append(Config.iteratables[-2].cur_line)
            cur_line_split = Config.iteratables[-2].cur_line.split()
        except IndexError:
            pass
        if cur_line_split[0] == "NEXT" and cur_line_split[1] == lcv:
            del line_list[-1]
            break
    try:
        Config.iteratables[-2].cur_line = Config.iteratables[-2].line_list[Config.iteratables[-2].line_number]
    except IndexError:
        pass

    Config.iteratables[-1] = Classes.FOR_LOOP(line_list=line_list, lcv=lcv, start=start, end=end)
    for i in range(Config.iteratables[-1].start, Config.iteratables[-1].end):
        Config.variables[lcv] = i
        while Config.iteratables[-1].line_number < len(Config.iteratables[-1].line_list):
            cur_line = Config.iteratables[-1].line_list[Config.iteratables[-1].line_number]
            main(cur_line)
            Config.iteratables[-1].line_number += 1
        Config.iteratables[-1].line_number = 0
    del Config.iteratables[-1]


def WHILE():
    pass


def REPEAT():
    pass


def ASSIGNMENT(line_used):
    to_be_eval = ""
    eq_found = False
    lst3 = line_used.split()
    for vr in lst3:
        try:
            vr = int(vr)
        except ValueError:
            pass
        if vr == '=' or eq_found:
            eq_found = True
        if eq_found:
            if vr in Config.variables:
                to_be_eval += str(Config.variables[vr])
            elif isinstance(vr, int):
                to_be_eval += str(vr)
            elif vr in Config.mops:
                to_be_eval += str(vr)
    Config.variables[lst3[0]] = eval(to_be_eval)


def INPUT(line_used):
    varwanted = line_used.split()
    varwanted = varwanted[1]
    Config.variables[varwanted] = input()


def PRINT(line_used):
    lst1 = line_used.split()
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
