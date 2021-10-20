import object


def possibleProgressionsLast1(inProg):
    # List of each unique line from the dataset
    lines = getLines()

    # list of possible following progressions
    possibleFollow = []

    for l in lines:
        for c in range(len(l.chords)):
            # If the progression from inProg is there and not at the end of a line add the following element to possibleFollow
            if l.chords[c] == inProg and c != len(l.chords) - 1:
                possibleFollow.append(l.chords[c + 1])

    print("Possible followings for " + inProg)

    for y in set(possibleFollow):
        print(y + " " + str(round((possibleFollow.count(y) / len(possibleFollow) * 100), 2)) + "%")

    return None


def getUniqueLines():
    songList = object.main()
    output = []  # each line from each song

    for i in songList:
        for j in i.forms:
            for y in j.chordProgressions:
                for q in y.line:
                    if not (q in output):
                        output.append(q)

    return output

def getLines():
    songList = object.main()
    output = []  # each line from each song

    for i in songList:
        for j in i.forms:
            for y in j.chordProgressions:
                for q in y.line:
                    output.append(q)

    return output


if __name__ == '__main__':
    possibleProgressionsLast1("V")
