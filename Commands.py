import Functions as Fun
import Config
import Classes


def main(line_used):
    if line_used[0:5] == "PRINT" or line_used[0:6] == "OUTPUT":
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

    elif "=" in line_used:
        ASSIGNMENT(line_used)

    elif line_used[0:2] == "//" or line_used == "":
        pass


def IF():
    Fun.object_gen()
    Config.Iteratables[-1] = Classes.COND_STATEMENT()

    found_endif = False
    alt_lines = True
    line_list = []

    line_split = Config.Iteratables[-2].line_list[Config.Iteratables[-2].line_number].split()

    if line_split[-1] == "THEN":
        del line_split[-1]
    else:
        Config.Iteratables[-2].line_number += 1

    Config.Iteratables[-1].Cond = line_split
    cond = Config.Iteratables[-1].Cond
    Config.Iteratables[-1].Cond = Fun.compare(cond)

    if Config.Iteratables[-1].Cond:

        while True:

            Config.Iteratables[-2].line_number += 1
            try:
                Config.Iteratables[-2].cur_line = Config.Iteratables[-2].line_list[Config.Iteratables[-2].line_number]

                line_list.append(Config.Iteratables[-2].cur_line)
                line_split = Config.Iteratables[-2].cur_line.split()

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

        Config.Iteratables[-1].line_list = line_list
        while not found_endif:
            Config.Iteratables[-2].line_number += 1
            Config.Iteratables[-2].cur_line = Config.Iteratables[-2].line_list[Config.Iteratables[-2].line_number]
            line_split = Config.Iteratables[-2].cur_line.split()
            if line_split[0] == "IF":
                Classes.Loop_Counts.If += 1
            if line_split[0] == "ENDIF":
                if Classes.Loop_Counts.If == 0:
                    break
                else:
                    Classes.Loop_Counts.If -= 1

    else:
        Classes.Loop_Counts.If = 1
        while not (Classes.Loop_Counts.If == 1 and line_split[0] == "ELSE"):
            Config.Iteratables[-2].line_number += 1
            Config.Iteratables[-2].cur_line = Config.Iteratables[-2].line_list[Config.Iteratables[-2].line_number]
            line_split = Config.Iteratables[-2].cur_line.split()
            if line_split[0] == "IF":
                Classes.Loop_Counts.If += 1
            if line_split[0] == "ENDIF":
                Classes.Loop_Counts.If -= 1
            if Classes.Loop_Counts.If == 0 and line_split[0] == "ENDIF":
                alt_lines = False
                break

        while Classes.Loop_Counts.If > 0 and line_split[0] != "ENDIF" and alt_lines:

            Config.Iteratables[-2].line_number += 1
            try:
                Config.Iteratables[-2].cur_line = Config.Iteratables[-2].line_list[Config.Iteratables[-2].line_number]

                line_list.append(Config.Iteratables[-2].cur_line)
                line_split = Config.Iteratables[-2].cur_line.split()

                if line_split[0] == "IF":
                    Classes.Loop_Counts.If += 1
                if line_split[0] == "ENDIF":
                    Classes.Loop_Counts.If -= 1
                    del line_list[-1]

            except IndexError:
                pass
        Config.Iteratables[-1].line_list = line_list

    while Config.Iteratables[-1].line_number < len(Config.Iteratables[-1].line_list):
        cur_line = Config.Iteratables[-1].line_list[Config.Iteratables[-1].line_number]
        main(cur_line)
        Config.Iteratables[-1].line_number += 1
    del Config.Iteratables[-1]


def FOR():
    Fun.object_gen()
    line_list = []

    cur_line_split = Config.Iteratables[-2].line_list[Config.Iteratables[-2].line_number].split()
    lcv = cur_line_split[1]
    Config.variables[lcv] = lcv
    start = int(cur_line_split[3])
    if cur_line_split[5] in Config.variables:
        end = int(Config.variables[cur_line_split[5]]) + 1
    else:
        end = int(cur_line_split[5]) + 1
    while True:
        Config.Iteratables[-2].line_number += 1
        try:
            Config.Iteratables[-2].cur_line = Config.Iteratables[-2].line_list[Config.Iteratables[-2].line_number]
            line_list.append(Config.Iteratables[-2].cur_line)
            cur_line_split = Config.Iteratables[-2].cur_line.split()
        except IndexError:
            pass
        if cur_line_split[0] == "NEXT" and cur_line_split[1] == lcv:
            del line_list[-1]
            break
    try:
        Config.Iteratables[-2].cur_line = Config.Iteratables[-2].line_list[Config.Iteratables[-2].line_number]
    except IndexError:
        pass

    Config.Iteratables[-1] = Classes.FOR_LOOP(line_list=line_list, lcv=lcv, start=start, end=end)
    for i in range(Config.Iteratables[-1].start, Config.Iteratables[-1].end):
        Config.variables[lcv] = i
        while Config.Iteratables[-1].line_number < len(Config.Iteratables[-1].line_list):
            cur_line = Config.Iteratables[-1].line_list[Config.Iteratables[-1].line_number]
            main(cur_line)
            Config.Iteratables[-1].line_number += 1
        Config.Iteratables[-1].line_number = 0
    del Config.Iteratables[-1]
    del Config.variables[lcv]


def WHILE():
    Fun.object_gen()
    Config.Iteratables[-1] = Classes.COND_STATEMENT()

    line_list = []

    line_split = Config.Iteratables[-2].line_list[Config.Iteratables[-2].line_number].split()

    if line_split[-1] == "DO":
        del line_split[-1]

    Config.Iteratables[-1].Cond = line_split
    cond = Config.Iteratables[-1].Cond

    Config.Iteratables[-1].Cond = Fun.compare(cond)

    while True:
        Config.Iteratables[-2].line_number += 1
        try:
            Config.Iteratables[-2].cur_line = Config.Iteratables[-2].line_list[Config.Iteratables[-2].line_number]

            line_list.append(Config.Iteratables[-2].cur_line)
            line_split = Config.Iteratables[-2].cur_line.split()

            if line_split[0] == "WHILE":
                Classes.Loop_Counts.While += 1

            if line_split[0] == "ENDWHILE" and Classes.Loop_Counts.While == 0:
                del line_list[-1]
                break

            if line_split[0] == "ENDWHILE":
                Classes.Loop_Counts.While -= 1

        except IndexError:
            pass

    # Config.Iteratables[-2].line_number -= 1
    Config.Iteratables[-1].line_list = line_list

    while Config.Iteratables[-1].Cond:

        while Config.Iteratables[-1].line_number < len(Config.Iteratables[-1].line_list):
            cur_line = Config.Iteratables[-1].line_list[Config.Iteratables[-1].line_number]
            main(cur_line)
            Config.Iteratables[-1].line_number += 1

        Config.Iteratables[-1].line_number = 0
        Config.Iteratables[-1].Cond = Fun.compare(cond)
    del Config.Iteratables[-1]


def REPEAT():
    Fun.object_gen()
    Config.Iteratables[-1] = Classes.COND_STATEMENT()

    line_list = []

    while True:
        Config.Iteratables[-2].line_number += 1
        try:
            Config.Iteratables[-2].cur_line = Config.Iteratables[-2].line_list[Config.Iteratables[-2].line_number]

            line_list.append(Config.Iteratables[-2].cur_line)
            line_split = Config.Iteratables[-2].cur_line.split()

            if line_split[0] == "REPEAT":
                Classes.Loop_Counts.Repeat += 1

            if line_split[0] == "UNTIL" and Classes.Loop_Counts.Repeat == 0:

                Config.Iteratables[-1].Cond = line_split
                cond = Config.Iteratables[-1].Cond

                Config.Iteratables[-1].Cond = Fun.compare(cond)

                del line_list[-1]
                break

            if line_split[0] == "UNTIL":
                Classes.Loop_Counts.Repeat -= 1

        except IndexError:
            pass

    # Config.Iteratables[-2].line_number -= 1
    Config.Iteratables[-1].line_list = line_list

    while True:

        while Config.Iteratables[-1].line_number < len(Config.Iteratables[-1].line_list):
            cur_line = Config.Iteratables[-1].line_list[Config.Iteratables[-1].line_number]
            main(cur_line)
            Config.Iteratables[-1].line_number += 1

        Config.Iteratables[-1].line_number = 0
        Config.Iteratables[-1].Cond = Fun.compare(cond)

        if Config.Iteratables[-1].Cond:
            break
    del Config.Iteratables[-1]


def ASSIGNMENT(line_used):
    lst = line_used.split()
    # check if this is an array declaration
    if not Fun.check_array_declaration(lst):
        Fun.assign(line_used)
    else:
        Fun.declare_array(lst)


def INPUT(line_used):
    varwanted = line_used.split()
    varwanted = varwanted[1]
    if "[" in line_used:
        A_S = varwanted.find("[")
        pos_num = varwanted[A_S + 1:-1]
        try:
            pos_num = int(pos_num)
        except ValueError:
            pos_num = Config.variables[pos_num]
        var = varwanted[:A_S]
        if var not in Config.variables:
            Config.variables[var] = {}
        Config.variables[var][pos_num] = input()
    else:
        Config.variables[varwanted] = input()


def PRINT(line_used):
    lst = line_used.split()
    string_flag = False
    printed = ""
    del lst[0]
    for w in range(len(lst)):

        word = lst[w]
        if word[0] == '\"':
            string_flag = True
            if word[-1] == '\"':
                string_flag = False
                printed += word[1:-1]
                continue
            else:
                printed += word[1:]
            printed += " "
        elif word[-1] == '\"':
            string_flag = False
            printed += word[:-1]
            printed += " "
        elif string_flag:
            printed += word[:]
            printed += " "
        if not string_flag:
            if word in Config.variables:  # This checks if it is a variable and if the variable exists
                printed += str(Config.variables[word])
                continue
            elif "[" in word:
                printed += str(Fun.fetch_value(word))
            elif word == ",":
                printed += " "
    print(printed)
