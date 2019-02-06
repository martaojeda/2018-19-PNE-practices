s_1 = (input("Please, enter the sequence 1:")).replace(" ", "")
s_2 = (input("Please, enter the sequence 2:")).replace(" ", "")
sequences = [s_1, s_2]

from Bases import count_bases
count_bases(sequences)
#This is to calculate the data of sequence 1.

tl = len(sequences[0])
print("Sequence 1 is {} bases in length.".format(tl))

#Count Base A
print("Base A")
print("   Counter: ", count_bases(sequences[0])["As"])
#Calculate the total length
if tl== 0:
    print("   Percentages: ", tl, "%")
else:
    print("   Percentage: ", round(100.0 * count_bases(sequences[0])["As"]/tl, 1),"%")

#Count Base C
print("Base C")
print("   Counter: ", count_bases(sequences[0])["Cs"])
if tl== 0:
    print("   Percentages: ", tl, "%")
else:
    print("   Percentage: ", round(100.0 * count_bases(sequences[0])["Cs"]/tl, 1), "%")

#Count Base C
print("Base C")
print("   Counter: ", count_bases(sequences[0])["Cs"])
if tl== 0:
    print("   Percentages: ", tl, "%")
else:
    print("   Percentage: ", round(100.0 * count_bases(sequences[0])["Cs"]/tl, 1), "%")

#Count Base T
print("Base T")
print("   Counter: ", count_bases(sequences[0])["Ts"])
if tl== 0:
    print("   Percentages: ", tl,"%")
else:
    print("   Percentage: ", round(100.0 * count_bases(sequences[0])["Ts"]/tl, 1),"%")


#This is to calculate the data of sequence 2.

tl = len(sequences[1])
print("Sequence 2 is {} bases in length.".format(tl))

# Count Base A
print("Base A")
print("   Counter: ", count_bases(sequences[1])["As"])
# Calculate the total length
if tl == 0:
    print("   Percentages: ", tl, "%")
else:
    print("   Percentage: ", round(100.0 * count_bases(sequences[1])["As"] / tl, 1), "%")

# Count Base C
print("Base C")
print("   Counter: ", count_bases(sequences[1])["Cs"])
if tl == 0:
    print("   Percentages: ", tl, "%")
else:
    print("   Percentage: ", round(100.0 * count_bases(sequences[1])["Cs"] / tl, 1), "%")

# Count Base C
print("Base C")
print("   Counter: ", count_bases(sequences[1])["Cs"])
if tl == 0:
    print("   Percentages: ", tl, "%")
else:
    print("   Percentage: ", round(100.0 * count_bases(sequences[1])["Cs"] / tl, 1), "%")

# Count Base T
print("Base T")
print("   Counter: ", count_bases(sequences[1])["Ts"])
if tl == 0:
    print("   Percentages: ", tl, "%")
else:
    print("   Percentage: ", round(100.0 * count_bases(sequences[1])["Ts"] / tl, 1), "%")




