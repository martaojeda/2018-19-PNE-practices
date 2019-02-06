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
        return self.count(base)*100/self.length()

    def reverse(self):
        return self.strbases[::-1]


s_1 = Seq("ACTGA")
str_1 = s_1.strbases


l_1 = s_1.length()
r_1 = s_1.reverse()
c_1 = s_1.complement()
counter_C= s_1.count("C")
counter_A = s_1.count("A")
counter_G = s_1.count("G")
counter_T = s_1.count("T")
percentage_A = s_1.perc("A")
percentage_C = s_1.perc("C")
percentage_G = s_1.perc("G")
percentage_T = s_1.perc("T")

print(l_1)
print(r_1)
print(c_1.strbases)
print(counter_A)
print(counter_C)
print(counter_G)
print(counter_T)
print(percentage_A)
print(percentage_C)
print(percentage_G)
print(percentage_T)

