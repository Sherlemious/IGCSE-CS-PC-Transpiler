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


def check_opener(line):
    line = line.strip()
    if line[0] == "IF":
        Config.CountDict["IFSTATEMENT"] += 1
    if line[0] == "WHILE":
        Config.CountDict["WHILELOOP"] += 1
    if line[0] == "REPEAT":
        Config.CountDict["REPEATLOOP"] += 1


def check_ending(line):
    line = line.strip()
    if line[0] == "ENDIF":
        Config.CountDict["IFSTATEMENT"] -= 1
    if line[0] == "ENDWHILE":
        Config.CountDict["WHILELOOP"] -= 1
    if line[0] == "UNTIL":
        Config.CountDict["REPEATLOOP"] -= 1


def object_gen():
    Config.iteratables.append("Statement " + str(len(Config.iteratables)))


def IF():
    outer_list = []
    object_gen()
    true_lines = []
    false_lines = []
    Config.CountDict["IFSTATEMENT"] += 1
    # then_found = False

    if len(Config.iteratables) == 1:
        else_starter = Config.i
        lst = Config.Line.split()
        cond = lst
        while True:
            Config.i += 1
            try:
                Config.Line = Config.FileList[Config.i]
                check_opener(Config.Line)
                check_ending(Config.Line)
                if Config.Line != "THEN":
                    outer_list.append(Config.Line)
                    true_lines.append(Config.Line)
                    # then_found = True
                cur_line_split = Config.Line.split()
                else_starter += 1
                if (cur_line_split[0] == "ELSE" or cur_line_split[0] == "ENDIF") and Config.CountDict["IFSTATEMENT"] == 1:
                    del true_lines[-1]
                    if cur_line_split[0] == "ELSE":
                        while True:
                            Config.i += 1
                            try:
                                Config.Line = Config.FileList[Config.i]
                                false_lines.append(Config.Line)
                                cur_line_split = Config.Line.split()
                            except IndexError:
                                pass
                            if cur_line_split[0] == "ENDIF":
                                del false_lines[-1]
                                Config.CountDict["IF_ST"] -= 1
                                break
                        ending = Config.i
                        break

            except IndexError:
                pass

        if len(cond) == 4:
            Config.iteratables[-1] = Classes.IFSTATEMENT(condition=cond, iffalse=false_lines, iftrue=true_lines,
                                                         elsestarter=else_starter, falsending=ending,
                                                         outerlinelist=outer_list)
            Config.iteratables[-1].condition = Fun.comp(cond[1], cond[3], cond[2])
            if Config.iteratables[-1].condition:
                while Config.iteratables[-1].curlinenumber < len(Config.iteratables[-1].iftrue):
                    cur_line = Config.iteratables[-1].iftrue[Config.iteratables[-1].curlinenumber]
                    main(cur_line)
                    Config.iteratables[-1].curlinenumber += 1
            else:
                Config.iteratables[-1].curline = Config.iteratables[-1].else_starter
                while Config.iteratables[-1].curline < (Config.iteratables[-1].falsending - 1):
                    cur_line = Config.iteratables[-1].iffalse[Config.iteratables[-1].elsecurline]
                    main(cur_line)
                    Config.iteratables[-1].curline += 1
                    Config.iteratables[-1].elsecurline += 1
                    Config.iteratables[-2].curlinenumber += 1
    else:
        else_starter = Config.iteratables[-2].curlinenumber
        lst = Config.iteratables[-2].line_list[Config.iteratables[-2].curlinenumber].split()
        cond = lst
        while True:
            Config.iteratables[-2].curlinenumber += 1
            try:
                outer_list.append(Config.Line)
                Config.iteratables[-2].curline = Config.FileList[Config.iteratables[-2].curlinenumber]
                if Config.Line != "THEN":
                    true_lines.append(Config.iteratables[-2].curline)
                cur_line_split = Config.iteratables[-2].curline.split()
                else_starter += 1
                if (cur_line_split[0] == "ELSE" or cur_line_split[0] == "ENDIF") and Config.CountDict["IF_ST"] == 1:
                    del true_lines[-1]
                    if cur_line_split[0] == "ELSE":
                        while True:
                            Config.iteratables[-2].curlinenumber += 1
                            try:
                                Config.iteratables[-2].curline = Config.iteratables[-2].line_list[
                                    Config.iteratables[-2].curlinenumber]
                                false_lines.append(Config.Line)
                                cur_line_split = Config.iteratables[-2].curline.split()
                            except IndexError:
                                pass
                            if (cur_line_split[0] == "ELSE" or cur_line_split[0] == "ENDIF") and Config.CountDict["IF_ST"] == 1:
                                del false_lines[-1]
                                Config.CountDict["IF_ST"] -= 1
                                break
                        ending = Config.i
                        break

            except IndexError:
                pass

        if len(cond) == 4:
            Config.iteratables[-1] = Classes.IFSTATEMENT(condition=cond, iffalse=false_lines, iftrue=true_lines,
                                                         elsestarter=else_starter, falsending=ending,
                                                         outerlinelist=outer_list)
            Config.iteratables[-1].condition = Fun.comp(cond[1], cond[3], cond[2])
            if Config.iteratables[-1].condition:
                Config.iteratables[-1].line_list = Config.iteratables[-1].iftrue
            else:
                Config.iteratables[-1].line_list = Config.iteratables[-1].iffalse
            while Config.iteratables[-1].curlinenumber < len(Config.iteratables[-1].iftrue):
                cur_line = Config.iteratables[-1].line_list[Config.iteratables[-1].curlinenumber]
                main(cur_line)
                Config.iteratables[-1].curlinenumber += 1

        # elif len(lst) == 8:
        #     if lst[5] == "AND":
        #         if Fun.comp(lst[1], lst[3], lst[2]) and Fun.comp(lst[5], lst[7], lst[6]):
        #             while lst[0] != "ENDIF":
        #                 main(line_used)
        #     elif lst[5] == "OR":
        #         try:
        #             if Fun.comp(lst[1], lst[3], lst[2]) or Fun.comp(lst[5], lst[7], lst[6]):
        #                 pass
        #         except IndexError:
        #             Errors.OpInvalid.isprint()


def FOR():
    object_gen()
    line_list = []
    if len(Config.iteratables) == 1:
        cur_line_split = Config.Line.split()
        lcv = cur_line_split[1]
        Config.variables[lcv] = lcv
        start = int(cur_line_split[3])
        end = int(cur_line_split[5]) + 1
        while True:
            Config.i += 1
            try:
                Config.Line = Config.FileList[Config.i]
                line_list.append(Config.Line)
                cur_line_split = Config.Line.split()
            except IndexError:
                pass
            if cur_line_split[0] == "NEXT" and cur_line_split[1] == lcv:
                del line_list[-1]
                break
        Config.i += 1
        try:
            Config.Line = Config.FileList[Config.i]
        except IndexError:
            pass

    else:
        cur_line_split = Config.iteratables[-2].line_list[Config.iteratables[-2].curlinenumber].split()
        lcv = cur_line_split[1]
        Config.variables[lcv] = lcv
        start = int(cur_line_split[3])
        end = int(cur_line_split[5]) + 1
        while True:
            Config.iteratables[-2].curlinenumber += 1
            try:
                Config.iteratables[-2].curline = Config.iteratables[-2].line_list[Config.iteratables[-2].curlinenumber]
                line_list.append(Config.iteratables[-2].curline)
                cur_line_split = Config.iteratables[-2].curline.split()
            except IndexError:
                pass
            if cur_line_split[0] == "NEXT" and cur_line_split[1] == lcv:
                del line_list[-1]
                break
        # Config.iteratables[-2].curlinenumber += 1 # I have no idea why removing this line works but it does.
        try:
            Config.iteratables[-2].curline = Config.iteratables[-2].line_list[Config.iteratables[-2].curlinenumber]
        except IndexError:
            pass

    Config.iteratables[-1] = Classes.FORLOOP(line_list=line_list, lcv=lcv, start=start, end=end)
    for i in range(Config.iteratables[-1].start, Config.iteratables[-1].end):
        Config.variables[lcv] = i
        while Config.iteratables[-1].curlinenumber < len(Config.iteratables[-1].line_list):
            cur_line = Config.iteratables[-1].line_list[Config.iteratables[-1].curlinenumber]
            main(cur_line)
            Config.iteratables[-1].curlinenumber += 1
        Config.iteratables[-1].curlinenumber = 0
    del Config.iteratables[-1]


# TODO: Add the code to the WHILE and REPEAT FUNCTIONS

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
