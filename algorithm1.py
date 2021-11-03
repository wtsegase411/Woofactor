import getLines


def possibleFirstChord():
    # List of each unique line from the dataset
    lines = getLines.main()
    # list of possible chords in a beginning of line
    possibleChord = []
    output = []

    for l in lines:
        # Adds chords that are present in a beginning of a line
        possibleChord.append(l.chords[0])

    for y in set(possibleChord):
        output.append(str(y) + " " + str(round((possibleChord.count(y) / len(possibleChord) * 100), 2)) + "%")
    return output


def possibleProgressions(progs):
    # List of each unique line from the dataset
    lines = getLines.main()
    # list of progressions in a line
    progCount = [0] * len(progs)

    for l in lines:
        for c in range(len(l.chords)):
            # Add progressions that are present in a line
            progCount[progs.index(l.chords[c])] += 1

    return progCount


def possibleProgressionsLast1(progs, inProg):
    # List of each unique line from the dataset
    lines = getLines.main()

    # list of possible following progressions
    progCount = [0] * len(progs)

    for l in lines:
        for c in range(len(l.chords)):
            # If the progression from inProg is there and not at the end of a line add the following element to possibleFollow
            if l.chords[c] == inProg and c != len(l.chords) - 1:
                progCount[progs.index(l.chords[c + 1])] += 1

    return progCount


def possibleProgressionsLast2(progs, inProg1, inProg2):
    # List of each unique line from the dataset
    lines = getLines.main()

    progCount = [0] * len(progs)

    for l in lines:
        for c in range(len(l.chords)):
            # If the progression from inProg is there and not at the end of a line add the following element to possibleFollow
            if l.chords[c] == inProg1 and c < len(l.chords) - 2 and l.chords[c + 1] == inProg2:
                progCount[progs.index(l.chords[c + 2])] += 1

    return progCount
