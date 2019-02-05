def count_a(seq):
    """Counting the number of As in the string"""

    result = 0
    for b in seq:
        if b == "A":
            result += 1

    return result

#Main program

s = (input("Please, enter a valid sequence:")).replace(" ", "")
na = count_a(s)
print("The are {} As in the sequence.".format(na))

#Calculate the total length
tl = len(s)
if tl== 0:
    print("The sequence is {} bases in length".format(tl))
    print("The percentages of As is {}%".format(tl))
else:
    print("This sequence is {} bases in length".format(tl))
    print("The peercentages of As is {}%".format(round(100.0 * na/tl, 1)))