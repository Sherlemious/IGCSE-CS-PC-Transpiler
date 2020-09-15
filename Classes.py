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
    def __init__(self, condtion, iftrue, iffalse):
        super().__init__()
        self.condtion = condtion
        self.iftrue = iftrue
        self.iffalse = iffalse
