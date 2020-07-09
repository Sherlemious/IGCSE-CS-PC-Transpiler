op_list = ['=', '>', '<', '<=', '>=', '<>']


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
