import object


def main():
    songList = object.main()
    output = []  # each line from each song
    for i in songList:
        songLines = []
        for j in i.forms:
            for y in j.chordProgressions:
                for q in y.line:
                    if not ((q in output) and (q in songLines)):
                        output.append(q)
                        songLines.append(q)

    return output
