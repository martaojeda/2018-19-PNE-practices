#Main program

s = (input("Please, enter a valid sequence:")).replace(" ", "")

from Bases import count_bases
count_bases(s)
na = count_bases(s)

print("The sequence is {} bases in length".format(len(s)))
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


