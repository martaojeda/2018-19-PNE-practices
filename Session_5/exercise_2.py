def count_bases(seq):
    """Counting the number of As, Cs, Gs and Ts in the string"""

    result_a = 0
    result_c = 0
    result_g = 0
    result_t = 0
    for b in seq:
        if b == "A":
            result_a += 1
        elif b == "C":
            result_c += 1
        elif b == "G":
            result_g += 1
        elif b == "T":
            result_t += 1
    return dict(As= result_a, Cs= result_c, Gs= result_g, Ts= result_t)

s_1 = (input("Please, enter the sequence 1:")).replace(" ", "")
s_2 = (input("Please, enter the sequence 2:")).replace(" ", "")
sequences = [s_1, s_2]
na = count_bases(sequences)

#Count Base A
print("Base A:")
print("Counter: ", count_bases(sequences)["As"][0])
#Calculate the total length
tl = len(sequences)[0]
if tl== 0:
    print("Percentages: ", tl, "%")
else:
    print("Percentage: ", round(100.0 * count_bases(sequences)["As"][0]/tl, 1),"%")

#Count Base C
print("Base C:")
print("Counter: ", count_bases(sequences)["Cs"])
tl = len(s)
if tl== 0:
    print("Percentages: ", tl, "%")
else:
    print("Percentage: ", round(100.0 * count_bases(sequences)["Cs"]/tl, 1), "%")

#Count Base G
print("Base G:")
print("Counter: ", count_bases(sequences)["Gs"])
tl = len(s)
if tl== 0:
    print("Percentages: ", tl,"%")
else:
    print("Percentage: ", round(100.0 * count_bases(sequences)["Gs"]/tl, 1), "%")

#Count Base T
print("Base T:")
print("Counter: ", count_bases(sequences)["Ts"])
tl = len(s)
if tl== 0:
    print("Percentages: ", tl,"%")
else:
    print("Percentage: ", round(100.0 * count_bases(sequences)["Ts"]/tl, 1),"%")

