import algorithm1


def main():
    progs = ["I", "Im", "I7", "II", "IIm", "II7", "III", "IIIm", "III7", "IV", "IVm", "IV7", "V", "Vm", "V7",  "VI", "VIm", "VI7", "VII", "VIIm", "VII7"]

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

    for x in range(len(alg2Out)):
        if len(alg2Out[x]) > 0:
            print("Possibilities for " + str(progs[int(x / len(progs))]) + "  " + str(progs[x % len(progs)]) + "  " + str(alg2Out[x]))


    return None


if __name__ == '__main__':
    main()
