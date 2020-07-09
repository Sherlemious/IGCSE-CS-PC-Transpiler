from Main import Line, variables
global Line, variables


def PRINT():
    lst1 = Line.split()
    printed = ""
    for w in range(1, len(lst1)):

        word = lst1[w]
        end = int(len(word))
        if word in variables and word[0] != "\"":  # This checks if it is a variable and if the variable exists
            printed += str(variables[word])
        else:
            for c in range(end):
                if w == 1 and c == 0:
                    pass
                else:
                    printed += word[c]
            printed += " "

    print(printed)
