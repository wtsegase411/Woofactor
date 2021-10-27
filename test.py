import algorithm1
import normalize
import random
import numpy as np

#test
def main():

    #A list of all the possible prorgessions
    progs = ["I", "Im", "I7", "II", "IIm", "II7", "III", "IIIm", "III7", "IV", "IVm", "IV7", "V", "Vm", "V7",  "VI", "VIm", "VI7", "VII", "VIIm", "VII7"]

    alg0Out = normalize.main(algorithm1.possibleProgressions(progs))
    alg1Out = []
    alg2Out = []

    for part in progs:
        alg1Out.append(normalize.main(algorithm1.possibleProgressionsLast1(progs, part)))

    for part1 in progs:
        for part2 in progs:
            alg2Out.append(normalize.main(algorithm1.possibleProgressionsLast2(progs, part1, part2)))


    #Print out the probabilities for testing
    # print(alg0Out)
    #
    # for x in range(len(alg1Out)):
    #     if sum(alg1Out[x]) > 0:
    #         print("Possibilities after " + str(progs[x]) + "  " + str(alg1Out[x]))
    #
    # for x in range(len(alg2Out)):
    #     if sum(alg2Out[x]) > 0:
    #         print("Possibilities after " + str(progs[int(x / len(progs))]) + "  " + str(progs[x % len(progs)]) + "  " + str(alg2Out[x]))


    # Weigths for each section
    prob0Weight = 1/3
    prob1Weight = 1/3
    prob2Weight = 1/3

    # Get the user inputed list of progressons seperated by commaas
    progsIn = input("Comma separated string of progressions: ")

    # remove spaces and turn comma seperated string into list
    progsIn = progsIn.replace(" ", "").split(",")

    # If the user doesn't input a progression
    if progsIn[0] == '':
        print(random.choices(progs, weights = alg0Out, k = 1))

    # If the user only inputs 1 progression
    elif len(progsIn) == 1:
        weights0 = np.array(alg0Out) * prob0Weight
        weights1 = np.array(alg1Out[progs.index(progsIn[0])]) * prob1Weight
        print(random.choices(progs, weights = weights0 + weights1, k = 1))

    # If the user inputs 2 progressions
    elif len(progsIn) == 2:
        weights0 = np.array(alg0Out) * prob0Weight
        weights1 = np.array(alg1Out[progs.index(progsIn[0])]) * prob1Weight
        weights2 = np.array(alg2Out[progs.index(progsIn[0]) * len(progs) + progs.index(progsIn[1])]) * prob2Weight

        # Print probabilities for testing
        # for x in range(len((weights0 * weights1 * weights2))):
        #     if (weights0 * weights1 * weights2)[x] != 0:
        #         print(str(progs[x]) + " " + str((weights0 * weights1 * weights2)[x]))

        print(random.choices(progs, weights=weights0 * weights1 * weights2, k=1))

    else:
        print("We don't have data for that progression")

    return None


if __name__ == '__main__':
    main()
