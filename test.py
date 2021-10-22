import algorithm1

#test
def main():
    progs = ["I", "Im", "II", "IIm", "III", "IIIm", "IV", "IVm", "V", "Vm", "VI", "VIm", "VII", "VIIm", ]

    alg1Out = []
    alg2Out = []

    for part in progs:
        alg1Out.append(algorithm1.possibleProgressionsLast1(part))

    for part1 in progs:
        for part2 in progs:
            alg2Out.append(algorithm1.possibleProgressionsLast2(part1, part2))

    for x in range(len(alg1Out)):
        if len(alg1Out[x]) > 0:
            print("Possibilities for " + str(progs[x]) + "  " + str(alg1Out[x]))

    return None


if __name__ == '__main__':
    main()
