class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):
        self.strbases = strbases

    def length(self):
        return len(self.strbases)

    def complement(self):
        out = ''
        for l in self.strbases:
            if l == "A":
                out += "T"
            if l == "T":
                out += "A"
            if l == "C":
                out += "G"
            if l == "G":
                out += "C"
        return Seq(out)

    def count(self,base):
        counter= 0
        for e in self.strbases:
            if e == base:
                counter += 1
        return counter

    def perc(self, base):
        return round(self.count(base)*100/self.length(), 1)

    def reverse(self):
        return Seq(self.strbases[::-1])

