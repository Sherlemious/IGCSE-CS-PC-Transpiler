class FUNCTIONS:
    def __init__(self):
        self.curlinenumber = 0
        self.curline = ""


class FORLOOP(FUNCTIONS):
    def __init__(self, line_list, lcv, start, end):
        super().__init__()
        self.line_list = line_list
        self.LCV = lcv
        self.start = start
        self.end = end


class IFSTATEMENT(FUNCTIONS):
    def __init__(self, condition, iftrue, iffalse, elsestarter, falsending, outerlinelist):
        super().__init__()
        self.condtion = condition
        self.iftrue = iftrue
        self.iffalse = iffalse
        self.else_starter = elsestarter
        self.falsending = falsending
        self.elsecurline = 0
        self.linelist = outerlinelist
