class Blok:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.val = None
        self.top = None
        self.btm = None
        self.lef = None
        self.rgh = None

    def __repr__(self):
        return self.val

    def setValue(self, value):
        self.val = value
