file = input("Please, introduce the name of the file:")
with open (file, "r") as f:
    sequences = f.read()
    sequences = sequences.replace(" ", "")
    print("The length of the sequence is:", len(sequences))
    print("The letter A appears ", sequences.count("A"), "times.")
    print("The letter C appears ", sequences.count("C"), "times.")
    print("The letter G appears ", sequences.count("G"), "times.")
    print("The letter T appears ", sequences.count("T"), "times.")

