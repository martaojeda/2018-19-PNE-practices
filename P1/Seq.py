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
        return Seq(self.strbases[::-1])

#This is the main program only for Sequence 1.
s_1 = Seq("CTAATAGG")
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

print("Sequence 1 is: {}".format(s_1))
print("Length:  {}".format(l_1))
print("Bases count: A:",counter_A, ",  C:",counter_C, ",  G:",counter_G, ",  T:",counter_T)
print("Bases percentage: A:",percentage_A,"%  C:",percentage_C,"%  G:",percentage_G,"%  T:",percentage_T,"%")
print("The complementary sequence is:  {}".format(c_1.strbases))
print("The reverse sequence is:  {}".format(r_1.strbases))
print("                ")
print("                ")

#This is the main program for sequence 2.
s_2 = Seq("TTGACTGATTACCCGG")
str_2 = s_2.strbases
l_2 = s_2.length()
r_2 = s_2.reverse()
c_2 = s_2.complement()
counter_C= s_2.count("C")
counter_A = s_2.count("A")
counter_G = s_2.count("G")
counter_T = s_2.count("T")
percentage_A = s_2.perc("A")
percentage_C = s_2.perc("C")
percentage_G = s_2.perc("G")
percentage_T = s_2.perc("T")

print("Sequence 2 is: {}".format(s_2))
print("Length:  {}".format(l_2))
print("Bases count: A:",counter_A, ",  C:",counter_C, ",  G:",counter_G, ",  T:",counter_T)
print("Bases percentage: A:",percentage_A,"%  C:",percentage_C,"%  G:",percentage_G,"%  T:",percentage_T,"%")
print("The complementary sequence is:  {}".format(c_2.strbases))
print("The reverse sequence is:  {}".format(r_2.strbases))
print("                ")
print("                ")

#This is the main program for sequence 3 that is the complement of sequence 1.
s_3 = Seq(c_1.strbases)
str_3 = s_3.strbases
l_3= s_3.length()
r_3 = s_3.reverse()
c_3 = s_3.complement()
counter_C= s_3.count("C")
counter_A = s_3.count("A")
counter_G = s_3.count("G")
counter_T = s_3.count("T")
percentage_A = s_3.perc("A")
percentage_C = s_3.perc("C")
percentage_G = s_3.perc("G")
percentage_T = s_3.perc("T")

print("Sequence 3 is: {}".format(c_1.strbases))
print("Length:  {}".format(l_3))
print("Bases count: A:",counter_A, ",  C:",counter_C, ",  G:",counter_G, ",  T:",counter_T)
print("Bases percentage: A:",percentage_A,"%  C:",percentage_C,"%  G:",percentage_G,"%  T:",percentage_T,"%")
print("The complementary sequence is:  {}".format(c_3.strbases))
print("The reverse sequence is:  {}".format(r_3.strbases))
print("                ")
print("                ")

#This is the main program for sequence 4 that is the reverse of sequence 2.

s_4 = Seq(r_2.strbases)
str_4 = s_4.strbases
l_4= s_4.length()
r_4 = s_4.reverse()
c_4 = s_4.complement()
counter_C= s_4.count("C")
counter_A = s_4.count("A")
counter_G = s_4.count("G")
counter_T = s_4.count("T")
percentage_A = s_4.perc("A")
percentage_C = s_4.perc("C")
percentage_G = s_4.perc("G")
percentage_T = s_4.perc("T")

print("Sequence 4 is: {}".format(r_2.strbases))
print("Length:  {}".format(l_4))
print("Bases count: A:",counter_A, ",  C:",counter_C, ",  G:",counter_G, ",  T:",counter_T)
print("Bases percentage: A:",percentage_A,"%  C:",percentage_C,"%  G:",percentage_G,"%  T:",percentage_T,"%")
print("The complementary sequence is:  {}".format(c_4.strbases))
print("The reverse sequence is:  {}".format(r_4.strbases))
print("                ")
print("                ")








