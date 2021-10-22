import getLines


def possibleProgressionsLast1(inProg):
    # List of each unique line from the dataset
    lines = getLines.main()

    # list of possible following progressions
    possibleFollow = []
    output = []

    for l in lines:
        for c in range(len(l.chords)):
            # If the progression from inProg is there and not at the end of a line add the following element to possibleFollow
            if l.chords[c] == inProg and c != len(l.chords) - 1:
                possibleFollow.append(l.chords[c + 1])

    #print("Possible followings for " + inProg)

    for y in set(possibleFollow):
        #print(y + " " + str(round((possibleFollow.count(y) / len(possibleFollow) * 100), 2)) + "%")
        output.append(str(y) + " " + str(round((possibleFollow.count(y) / len(possibleFollow) * 100), 2)) + "%")

    return output


def possibleProgressionsLast2(inProg1, inProg2):
    # List of each unique line from the dataset
    lines = getLines.main()

    # list of possible following progressions
    possibleFollow = []
    output = []

    for l in lines:
        for c in range(len(l.chords)):
            # If the progression from inProg is there and not at the end of a line add the following element to possibleFollow
            if l.chords[c] == inProg1 and c < len(l.chords) - 2 and l.chords[c + 1] == inProg2:
                possibleFollow.append(l.chords[c + 2])

    #print("Possible followings for " + inProg1 + " " + inProg2)

    #print("Found " + str(len(possibleFollow)) + " cases of " + inProg1 + " " + inProg2)

    for y in set(possibleFollow):
        #print(y + " " + str(round((possibleFollow.count(y) / len(possibleFollow) * 100), 2)) + "%")
        output.append(y + " " + str(round((possibleFollow.count(y) / len(possibleFollow) * 100), 2)) + "%")

    return output
