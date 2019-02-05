def count_bases(s):
    """Counting the number of As, Cs, Gs and Ts in the string"""

    result_a = 0
    result_c = 0
    result_g = 0
    result_t = 0
    for b in s:
        if b == "A":
            result_a += 1
        elif b == "C":
            result_c += 1
        elif b == "G":
            result_g += 1
        elif b == "T":
            result_t += 1
    return dict(As= result_a, Cs= result_c, Gs= result_g, Ts= result_t)

#Main program

s = (input("Please, enter a valid sequence:")).replace(" ", "")
print("The sequence is {} bases in length".format(len(s)))
na = count_bases(s)

#Count Base A
print("Base A:")
print("Counter: ", count_bases(s)["As"])
#Calculate the total length
tl = len(s)
if tl== 0:
    print("Percentages: ", tl, "%")
else:
    print("Percentage: ", round(100.0 * count_bases(s)["As"]/tl, 1),"%")

#Count Base C
print("Base C:")
print("Counter: ", count_bases(s)["Cs"])
tl = len(s)
if tl== 0:
    print("Percentages: ", tl, "%")
else:
    print("Percentage: ", round(100.0 * count_bases(s)["Cs"]/tl, 1), "%")

#Count Base G
print("Base G:")
print("Counter: ", count_bases(s)["Gs"])
tl = len(s)
if tl== 0:
    print("Percentages: ", tl,"%")
else:
    print("Percentage: ", round(100.0 * count_bases(s)["Gs"]/tl, 1), "%")

#Count Base T
print("Base T:")
print("Counter: ", count_bases(s)["Ts"])
tl = len(s)
if tl== 0:
    print("Percentages: ", tl,"%")
else:
    print("Percentage: ", round(100.0 * count_bases(s)["Ts"]/tl, 1),"%")


