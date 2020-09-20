class FUNCTIONS:
    def __init__(self):
        self.curlinenumber = 0
        self.curline = ""


class FORLOOP(FUNCTIONS):
    def __init__(self, linelist, LCV, start, end):
        super().__init__()
        self.linelist = linelist
        self.LCV = LCV
        self.start = start
        self.end = end


class IFSTATEMENT(FUNCTIONS):
    def __init__(self, condition, iftrue, iffalse, elsestarter):
        super().__init__()
        self.condtion = condition
        self.iftrue = iftrue
        self.iffalse = iffalse
        self.elsestarter = elsestarter
