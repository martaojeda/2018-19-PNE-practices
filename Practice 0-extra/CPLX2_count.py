with open("CPLX2.txt", "r") as f:
    sequence = f.read()
    print("The letter A appears", sequence.count("A"), "times.")
    print("The letter C appears", sequence.count("C"), "times.")
    print("The letter T appears", sequence.count("T"), "times.")
    print("The lleter G appears", sequence.count("G"), "times.")