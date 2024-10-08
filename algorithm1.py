import getLines

# ***********************************************************************************
# outdated but might be useful for further development of the algorithms
# ***********************************************************************************
# def possibleFirstChord():
#     # List of each unique line from the dataset
#     lines = getLines.main()
#     # list of possible chords in a beginning of line
#     possibleChord = []
#     output = []
#
#     for l in lines:
#         # Adds chords that are present in a beginning of a line
#         possibleChord.append(l.chords[0])
#
#     for y in set(possibleChord):
#         output.append(str(y) + " " + str(round((possibleChord.count(y) / len(possibleChord) * 100), 2)) + "%")
#     return output


def possibleProgressions(possibleChords):
    '''
        Calls getLines() and counts how many times each chord occurs to find P(A)

            Parameters:
                possibleChords (list): a list of every possible progression found in the data


            Returns:
                progCount (list): a list of the count of each value in possibleChords
    '''

    # List of each unique line from the dataset
    lines = getLines.main()
    # list of progressions in a line
    progCount = [0] * len(possibleChords)

    for l in lines:
        for c in range(len(l.chords)):
            # Add progressions that are present in a line
            progCount[possibleChords.index(l.chords[c])] += 1

    return progCount


def possibleProgressionsLast1(possibleChords, inProg):
    '''
        Calls getLines() and counts how many times each element in possibleChords occurs after
        a specific chord (inProg) to find P(B|A) or P(B|inProg)

            Parameters:
                possibleChords (list): a list of every possible progression found in the data
                inProg (string): a chord which is 'A' in P(B|A)


            Returns:
                progCount (list): a list of the count of each value in possibleChords following inProg
    '''

    # List of each unique line from the dataset
    lines = getLines.main()

    # list of possible following progressions
    progCount = [0] * len(possibleChords)

    for l in lines:
        for c in range(len(l.chords)):
            # If the progression from inProg is there and not at the end of a line,
            # add the following element to possibleFollow
            if l.chords[c] == inProg and c != len(l.chords) - 1:
                progCount[possibleChords.index(l.chords[c + 1])] += 1

    return progCount


def possibleProgressionsLast2(possibleChords, inProg1, inProg2):
    '''
        Calls getLines() and counts how many times each element in possibleChords occurs after
        two specific chords (inProg1 and inProg2) to find P(C|AB) or P(C|inProg1, inProg2)

            Parameters:
                possibleChords (list): a list of every possible progression found in the data
                inProg1 (string): a chord which is 'A' in P(C|AB)
                inProg2 (string): a chord which is 'B' in P(C|AB)


            Returns:
                progCount (list): a list of the count of each value in possibleChords following inProg1, inProg2
    '''

    # List of each unique line from the dataset
    lines = getLines.main()

    progCount = [0] * len(possibleChords)

    for l in lines:
        for c in range(len(l.chords)):
            # If the progression from inProg is there and not at the end of a line,
            # add the following element to possibleFollow
            if l.chords[c] == inProg1 and c < len(l.chords) - 2 and l.chords[c + 1] == inProg2:
                progCount[possibleChords.index(l.chords[c + 2])] += 1

    return progCount
