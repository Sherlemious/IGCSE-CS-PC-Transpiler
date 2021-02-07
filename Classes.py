class FUNCTION:
    def __init__(self, line_list):
        self.line_number = 0
        self.cur_line = ""
        self.line_list = line_list


class FOR_LOOP(FUNCTION):
    def __init__(self, lcv, start, end, line_list):
        super().__init__(self)
        self.LCV = lcv
        self.start = start
        self.end = end
        self.line_list = line_list


class IF_STATEMENT(FUNCTION):
    def __init__(self):
        super().__init__(self)
        self.Condition = ""


class Loop_Counts:
    def __init__(self):
        pass
    While = 0
    Repeat = 0
    If = 0
