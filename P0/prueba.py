file = input("Please, introduce the name of the file:")
data = open(file, "r")
count_a = 0
count_c = 0
count_g = 0
count_t = 0
length = 0
for line in data:
    line.replace(" ","" ).upper()
    count_a += line.count("A")
    count_c += line.count("C")
    count_g += line.count("G")
    count_t += line.count("T")
    length += len(line.replace(" ", "").replace("\n", ""))
print("The length of the sequence is:", length)
print("The letter A appears ", count_a, "times.")
print("The letter C appears ", count_c, "times.")
print("The letter G appears ", count_g, "times.")
print("The letter T appears ", count_t, "times.")