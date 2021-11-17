import algorithm1
import getLines
import player
import normalize
import random
import two_dimensional_visual


# test
def predictior(progsIn, progs, alg0Out, alg1Out, alg2Out):
    # A list of all the possible prorgessions

    # # If the user didn't input anything clear progsIn
    # if progsIn[0] == '':
    #     progsIn = []

    currentOut = []

    # If the user gives more than 2 elements remove all but the last two
    if (len(progsIn)) > 2:
        workingProgs = progsIn[-2:]

    else:
        workingProgs = progsIn

    # If the user inputs 2 progressions we can see in the data
    if len(workingProgs) == 2 and sum(alg2Out[progs.index(workingProgs[0]) * len(progs) + progs.index(workingProgs[1])]) != 0:

        weights2 = alg2Out[progs.index(workingProgs[0]) * len(progs) + progs.index(workingProgs[1])]

        currentOut.append(random.choices(progs, weights=weights2, k=1)[0])

    # If the user only inputs 1 progression
    elif len(progsIn) >= 1 and sum(alg1Out[progs.index(progsIn[0])]) != 0:

        weights1 = alg1Out[progs.index(progsIn[0])]

        currentOut.append(random.choices(progs, weights=weights1, k=1)[0])

    # If the user doesn't input a progression
    else:
        currentOut.append(random.choices(progs, weights=alg0Out, k=1))

    if len(currentOut) == 1 and has2Beats(currentOut[0]) and currentOut[0][-1:] != '7':
        progsIn.append(currentOut[0])

        possibleFollow = random.choices(progs, weights=alg1Out[progs.index(currentOut[0])], k=1)[0]

        while(not has2Beats(possibleFollow)):
            possibleFollow = random.choices(progs, weights=alg1Out[progs.index(currentOut[0])], k=1)[0]

        progsIn.append(possibleFollow)

    else:
        progsIn.append(currentOut[0])

    for x in progsIn:
        print(x)
    print("|")

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
    for x in range(progLength - len(progsIn)):
        progsIn = predictior(progsIn, progs, modelOut[0], modelOut[1], modelOut[2])
    printString = ""

    # Create a string of each progression seperated by |s for printing
    printString += "| "
    holdBar = False
    for x in range(len(progsIn)):
        printString += progsIn[x] + " "

        if has2Beats(progsIn[x]) and holdBar == False:
            holdBar = True

        elif has2Beats(progsIn[x]) and holdBar == True:
            printString += "| "
            holdBar = False

        else:
            printString += "| "

    print(printString)

    # Play each progression if the user requested
    if playing == "Y":
        for x in progsIn:
            if True in [char.isdigit() for char in x]:
                currentBeat = int(x[-1])
                x = x[:-1]
            else:
                currentBeat = defaultBeats

            for y in range(currentBeat):
                player.translate(x, "G", playSPeed)

    # prints the arrays of probabilities
    # print(progs)
    # for p in range(len(progs)):
    #     print(progs[p] + str(modelOut[1][p]))

    # outputs a visualization of the data's progressions
    #two_dimensional_visual.two_d_visualize(modelOut[1], progs, "P(B|A)")

    return None

def has2Beats(chord):
    return True in [char.isdigit() for char in chord] and chord[-1:] != '7'

if __name__ == '__main__':
    main()