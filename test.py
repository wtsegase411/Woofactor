import algorithm1
import normalize
import random
import numpy as np


# test
def predictior(progsIn):
    # A list of all the possible prorgessions
    progs = ["I", "Im", "I7", "II", "IIm", "II7", "III", "IIIm", "III7", "IV", "IVm", "IV7", "V", "Vm", "V7", "VI",
             "VIm", "VI7", "VII", "VIIm", "VII7"]

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
    prob0Weight = 1
    prob1Weight = 2
    prob2Weight = 4

    # If the user gives more than 2 elements remove all but the last two
    if (len(progsIn)) > 2:
        workingProgs = progsIn[-2:]

    else:
        workingProgs = progsIn

    # If the user doesn't input a progression
    if progsIn[0] == '':
        progsIn.append(random.choices(progs, weights=alg0Out, k=1)[0])

    # If the user only inputs 1 progression
    elif len(progsIn) == 1 and sum(alg1Out[progs.index(progsIn[0])]) != 0:
        weights0 = np.array(alg0Out) * prob0Weight
        weights1 = np.array(alg1Out[progs.index(progsIn[0])]) * prob1Weight

        # for x in range(len((weights0 * weights1))):
        #     if (weights0 * weights1)[x] != 0:
        #         print(str(progs[x]) + " " + str(normalize.main((weights0 * weights1))[x]))

        progsIn.append(random.choices(progs, weights=weights0 + weights1, k=1)[0])

    # If the user inputs 2 progressions
    elif len(workingProgs) == 2 and sum(alg2Out[progs.index(workingProgs[0]) * len(progs) + progs.index(workingProgs[1])]) != 0:
        weights0 = np.array(alg0Out) * prob0Weight
        weights1 = np.array(alg1Out[progs.index(workingProgs[0])]) * prob1Weight
        weights2 = np.array(alg2Out[progs.index(workingProgs[0]) * len(progs) + progs.index(workingProgs[1])]) * prob2Weight

        newWeights = probability3(weights0, weights1, weights2)

        # Print probabilities for testing
        # for x in range(len(newWeights)):
        #     if normalize.main(newWeights)[x] != 0:
        #         print(str(progs[x]) + " " + str(normalize.main(newWeights)[x]))

        progsIn.append(random.choices(progs, weights=newWeights, k=1)[0])

    else:
        print("We don't have data for that progression")

    for x in progsIn:
        print(x)

    return progsIn

def probability3(P1, P2, P3):

    return P1+P2+P3-(P1*P2)-(P1*P3)-(P2*P3)+(P1*P2*P3)

def main():
    # Get the user inputed list of progressons sepera
    # ted by commaas
    progsIn = input("Comma separated string of progressions: ")

    # remove spaces and turn comma seperated string into list
    progsIn = progsIn.replace(" ", "").split(",")

    while (True):
        progsIn = predictior(progsIn)
        input("Enter to continue.")

    return None

if __name__ == '__main__':
    while True:
        main()
