import algorithm1
import getLines
import player
import normalize
import random


# test
def predictior(progsIn, progs, alg0Out, alg1Out, alg2Out):
    # A list of all the possible prorgessions

    # If the user gives more than 2 elements remove all but the last two
    if (len(progsIn)) > 2:
        workingProgs = progsIn[-2:]

    else:
        workingProgs = progsIn

    # If the user inputs 2 progressions we can see in the data
    if len(workingProgs) == 2 and sum(alg2Out[progs.index(workingProgs[0]) * len(progs) + progs.index(workingProgs[1])]) != 0:

        weights2 = alg2Out[progs.index(workingProgs[0]) * len(progs) + progs.index(workingProgs[1])]

        # Print probabilities for testing
        # for x in range(len(newWeights)):
        #     if normalize.main(newWeights)[x] != 0:
        #         print(str(progs[x]) + " " + str(normalize.main(newWeights)[x]))

        progsIn.append(random.choices(progs, weights=weights2, k=1)[0])
        #print(str(progsIn[len(progsIn)-1]) + " " + str(normalize.main(weights2)[progs.index(progsIn[len(progsIn)-1])]))

    # If the user only inputs 1 progression
    elif len(progsIn) >= 1 and sum(alg1Out[progs.index(progsIn[0])]) != 0:

        weights1 = alg1Out[progs.index(progsIn[0])]

        # for x in range(len((weights0 * weights1))):
        #     if (weights0 * weights1)[x] != 0:
        #         print(str(progs[x]) + " " + str(normalize.main((weights0 * weights1))[x]))

        progsIn.append(random.choices(progs, weights=weights1, k=1)[0])
        #print(str(progsIn[len(progsIn)-1]) + " " + str(normalize.main(weights1)[progs.index(progsIn[len(progsIn)-1])]))


    # If the user doesn't input a progression
    else:
        progsIn.append(random.choices(progs, weights=alg0Out, k=1)[0])
        #print(str(progsIn[len(progsIn)-1]) + " " + str(normalize.main(alg0Out)[progs.index(progsIn[len(progsIn)-1])]))

    return progsIn

def baysianModel(progs):
    alg0Out = normalize.main(algorithm1.possibleProgressions(progs))
    alg1Out = []
    alg2Out = []

    for part in progs:
        alg1Out.append(normalize.main(algorithm1.possibleProgressionsLast1(progs, part)))

    for part1 in progs:
        for part2 in progs:
            alg2Out.append(normalize.main(algorithm1.possibleProgressionsLast2(progs, part1, part2)))

    return [alg0Out, alg1Out, alg2Out]

def main():

    progLength = 10
    playSPeed = 120/60/4
    defaultBeats = 4

    playing = input("Play music? (Y/N)")

    # Get the user inputed list of progressons seperated by commas
    progsIn = input("Comma separated string of progressions: ")

    lines = getLines.main()
    progs = []

    for l in lines:
        for c in l.chords:
            if c not in progs:
                progs.append(c)
                #print(c)

    # Get the baysianModel from the data to reuse over multiple iterations of prediction
    modelOut = baysianModel(progs)

    # Remove spaces and turn comma seperated string into list
    progsIn = progsIn.replace(" ", "").split(",")

    # Generate more progressions until the length is as long as the progLength
    while (len(progsIn) < progLength):
        progsIn = predictior(progsIn, progs, modelOut[0], modelOut[1], modelOut[2])

    # Print out each progression and play if the user said to
    for x in progsIn:
        print(x)
        if playing == "Y":
            if True in [char.isdigit() for char in x]:
                currentBeat = int(x[-1])
                x = x[:-1]
            else:
                currentBeat = defaultBeats

            for y in range(currentBeat):
                player.translate(x, "G", playSPeed)
    #
    # print(progs)
    # for p in range(len(progs)):
    #     print(progs[p] + str(modelOut[1][p]))

    return None

if __name__ == '__main__':
    main()