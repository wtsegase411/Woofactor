import os
from os.path import exists
import algorithm1
import getLines
import player
import normalize
import random
import modelSave
import romanNumeralToChord
import arrayVisualizer


# test
def predictior(progsIn, possibleChords, alg0Out, alg1Out, alg2Out):
    '''
            Predicts a following progression based on the user input (progsIn) or general probability if the user didn't
            give a list of progressions. If the user gave a list of progressions 2 or more elements look if we have a
            probability space for those progressions, if not look at only the last progression, if that also isn't in
            the data then use P(A). If the user gives a list of 1 progression use P(B|A) to generate the following
            progression, if that isn't available in the data then just use P(A) to generate the following chord. If the
            user inputs nothing then use P(A) to generate the new progression.

                Parameters:
                    progsIn (list): a list of progression input by the user or empty if they input nothing
                    possibleChords   (list): a list of every possible chord found in the data
                    alg0Out (list): P(A)
                    alg1Out (list): P(B|A)
                    alg2Out (list): P(C|AB)

                Returns:
                    progsIn (list): A list of strings that is progsIn with the next generated measure appended to the end
    '''

    currentOut = []

    # If the user gives more than 2 elements remove all but the last two
    if (len(progsIn)) > 2:
        workingProgs = progsIn[-2:]

    else:
        workingProgs = progsIn

    # If the user inputs 2 chords we can see in the data
    if len(workingProgs) == 2 and sum(alg2Out[possibleChords.index(workingProgs[0]) * len(possibleChords) + possibleChords.index(workingProgs[1])]) != 0:

        weights2 = alg2Out[possibleChords.index(workingProgs[0]) * len(possibleChords) + possibleChords.index(workingProgs[1])]

        currentOut.append(random.choices(possibleChords, weights=weights2, k=1)[0])

    # If the user only inputs 1 chord
    elif len(progsIn) >= 1 and progsIn[0] != '' and sum(alg1Out[possibleChords.index(progsIn[0])]) != 0:

        weights1 = alg1Out[possibleChords.index(progsIn[0])]

        currentOut.append(random.choices(possibleChords, weights=weights1, k=1)[0])

    # If the user doesn't input a progression
    else:
        currentOut = progsIn = (random.choices(possibleChords, weights=alg0Out, k=1))

    if len(currentOut) == 1 and chordInlcudesBeats(currentOut[0]) and currentOut[0][-1:] != '7':
        progsIn.append(currentOut[0])

        possibleFollow = random.choices(possibleChords, weights=alg1Out[possibleChords.index(currentOut[0])], k=1)[0]

        while(not chordInlcudesBeats(possibleFollow)):
            possibleFollow = random.choices(possibleChords, weights=alg1Out[possibleChords.index(currentOut[0])], k=1)[0]

        progsIn.append(possibleFollow)

    else:
        progsIn.append(currentOut[0])

    return progsIn


def baysianModel(possibleChords):
    '''
        calculates P(A), P(B|A), P(C|AB) where the probabilities were calculated by algorithm1's baysian probabilities
        looking through the data and finding the probabilities of each element in possibleChords.

            Parameters:
                possibleChords (list): a list of every possible chord found in the data

            Returns:
                [alg0Out, alg1Out, alg2Out] (list): a list of lists containing [P(A), P(B|A), P(C|AB)]
    '''

    alg0Out = normalize.main(algorithm1.possibleProgressions(possibleChords))
    alg1Out = []
    alg2Out = []

    for chord in possibleChords:
        alg1Out.append(normalize.main(algorithm1.possibleProgressionsLast1(possibleChords, chord)))

    for chord1 in possibleChords:
        for chord2 in possibleChords:
            alg2Out.append(normalize.main(algorithm1.possibleProgressionsLast2(possibleChords, chord1, chord2)))

    return [alg0Out, alg1Out, alg2Out]


def main():
    '''
        Asks the user if they want the music played
        Asks the user to input a comma separated list of progressions
        Generates a list of every possible progression in the dataset and saves it to possibleChords
        Calls BayseanModel with possibleChords and saves the model
        Generates a preset number of following progressions and prints them out seperated by bars like a chart.

            Parameters:
                None

            Returns:
                None
    '''

    # How long the progression should end up
    progLength = 10

    bpm = 120
    defaultBeats = 4

    lines = getLines.main()
    possibleChords = []

    for l in lines:
        for c in l.chords:
            if c not in possibleChords:
                possibleChords.append(c)

    if exists("model.txt"):
        genModel = input("Would you like to generate a model? (Y/N)")

        if genModel == "N":
            modelOut = modelSave.reads()

        else:
            modelOut = baysianModel(possibleChords)
            modelSave.saves(modelOut)

    else:
        modelOut = baysianModel(possibleChords)
        modelSave.saves(modelOut)

    cont = True

    while cont != "stop" and cont != "Stop":

        playing = input("Play music? (Y/N)")

        key = input("What key would you like the final out put to be in? ")

        while key not in ["C", "D", "E", "F", "G", "A", "B", "Cm", "Dm", "Em", "Fm", "Gm", "Am", "Bm"]:
            key = input("Invalid key please reenter: ")

        # Get the user inputted list of possibleChords separated by commas
        progsIn = input("Comma separated list of possibleChords in roman numeral form: ")

        # Remove spaces and turn comma seperated string into list
        progsIn = progsIn.replace(" ", "").split(",")

        # Check if there is an element in progsIn that wasn't found in the data
        unknownChord = False
        for x in progsIn:
            if x not in possibleChords:
                unknownChord = True

        if unknownChord:
            print("There was an unknown chord in the input, please try a different progression")

        # If the user inputted chords are contained in  possibleChords
        else:
            # Generate more progressions until the length is as long as the progLength
            for x in range(progLength - len(progsIn)):
                progsIn = predictior(progsIn, possibleChords, modelOut[0], modelOut[1], modelOut[2])

            print(chartFormat(progsIn))

            print(chartFormat(romanNumeralToChord.main(progsIn, key)))

            # Play each progression if the user requested
            if playing == "Y":
                for x in progsIn:
                    if True in [char.isdigit() for char in x]:
                        currentBeat = int(x[-1])
                        x = x[:-1]
                    else:
                        currentBeat = defaultBeats

                    for y in range(currentBeat):
                        player.translate(x, key, bpm/60/defaultBeats)

            # prints the arrays of probabilities
            # print(possibleChords)
            # for p in range(len(possibleChords)):
            #     print(possibleChords[p] + str(modelOut[1][p]))

            # outputs a visualization of the data's progressions
            #two_dimensional_visual.two_d_visualize(modelOut[1], possibleChords, "P(B|A)")

            cont = input("Generate another? ('stop') to end: ")

    return None


def chartFormat(progsIn):
    '''
        Takes in a list of chords and returns a version of them that is seperated by |s depending on their number
        of beats

            Parameters:
                progsIn (list): A list of chords

            Returns:
                printString (string): A string containing all the elements from progsIn seperated by |s between measures.
    '''

    # Create a string of each chord seperated by |s for printing
    printString = "| "
    holdBar = False

    for x in range(len(progsIn)):

        # If the element has beats or '7' or 'm' after the chord
        if chordInlcudesBeats(progsIn[x]):
            printString += progsIn[x][:-1] + " "

            if holdBar == False:
                holdBar = True

            else:
                printString += "| "
                holdBar = False

        else:
            printString += progsIn[x] + " "
            printString += "| "

    return printString


def chordInlcudesBeats(chord):
    '''
    Determines if a chord contains a beat by checking if the chord
    contains a number excluding '7', which would be a beat in our data scheme

        Parameters:
            chord (string): a series of roman numerals possibly followed buy an integer

        Returns:
            boolean true if there is a number in the given chord that isn't a '7'
    '''

    return True in [char.isdigit() for char in chord] and chord[-1:] != '7'


if __name__ == '__main__':
    main()