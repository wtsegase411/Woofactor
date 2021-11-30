import object


def main():
    '''
        Creates a list of each line of each song to easily look though the lines and their chords.

            Parameters:
                None

            Returns:
                output (list): a list of each line from each song
    '''

    songList = object.main()
    output = []  # each line from each song

    for i in songList:
        for j in i.forms:
            for y in j.chordProgressions:
                for q in y.line:
                        output.append(q)

    return output


def uniqueLines():
    '''
        Creates a list of each line of each song without repeats of lines
        to easily look though the lines and their chords.

            Parameters:
                None

            Returns:
                output (list): a list of each line from each song without repeats
    '''

    songList = object.main()
    output = []  # each line from each song

    for i in songList:
        for j in i.forms:
            for y in j.chordProgressions:
                for q in y.line:
                    if not q in output:
                        output.append(q)

    return output