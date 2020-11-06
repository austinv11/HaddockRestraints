def main():
    print("Interactive program to produce HADDOCK restraints (TBL) files")
    seg1 = input("Enter the segid for model1: ")
    seg2 = input("Enter the segid for model2: ")

    restraints = []
    while True:
        resid1 = input("Enter residue number from model 1 (blank to finish): ")
        if not resid1:
            break
        resid2 = input("Enter residue number from model 2: ")

        distance_restraint = input("Enter distance restraint in angstroms (default: 10): ")
        if not distance_restraint:
            distance_restraint = 10
        else:
            distance_restraint = int(distance_restraint)

        restraints.append((resid1, resid2, distance_restraint))

    output_file = input("Enter the output file path: ")

    # file format described in Box 4 of "The HADDOCK web server for data-driven biomolecular docking (2010)"
    with open(output_file, 'w') as f:
        for restraint in restraints:
            f.write(f"assign (resid {restraint[0]} and segid {seg1}) (resid {restraint[1]} and segid {seg2}) {restraint[2]} {restraint[2]} 0\n")


if __name__ == "__main__":
    main()
