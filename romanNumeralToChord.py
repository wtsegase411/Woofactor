

def main(romanNumerals, key):
    '''
    Given a list of roman numerals and a starting key returns the list of chords

        Parameters:
            romanNumerals (list): the list of chords in the form of roman numerals
            key (string): the starting chord

        Returns:
            output (list): the list of roman numerals changed into chords using the starting key
    '''

    numbers = ["I",  "II",    "III",  "IV",  "V",   "VI",  "VII"]
    things = [["C",  "Dm",    "Em",   "F",   "G",   "Am",  "Bdim"],
              ["D",  "Em",    "F#m",  "G",   "A",   "Bm",  "C#dim"],
              ["E",  "F#m",   "G#m",  "A",   "B",   "C#m", "D#dim"],
              ["F",  "Gm",    "Am",   "Bb",  "C",   "Dm",  "Edim"],
              ["G",  "Am",    "Bm",   "C",   "D",   "Em",  "F#dim"],
              ["A",  "Bm",    "C#m",  "D",   "E",   "F#m", "G#dim"],
              ["B",  "C#m",   "D#m",  "E",   "F#",  "G#m", "A#dim"],
              ["Cm", "Ddim",  "Eb",   "Fm",  "Gm",  "Ab",  "Bb"],
              ["Dm", "Edim",  "F#",   "Gm",  "Am",  "Bb",  "C"],
              ["Em", "F#dim", "G#",   "Am",  "Bm",  "C",   "D"],
              ["Fm", "Gdim",  "Ab",   "Bbm", "Cm",  "Db",  "Eb"],
              ["Gm", "Adim",  "Bb",   "Cm",  "Dm",  "Eb",  "F"],
              ["Am", "Bdim",  "C#",   "Dm",  "Em",  "F",   "G"],
              ["Bm", "C#dim", "D#",   "Em",  "F#m", "G",   "A"]]

    output = []

    scale = [item for item in things if item[0] == key][0]

    for x in romanNumerals:

        if "m2" in x:
            output.append(scale[numbers.index(x[:-2])] + x[-1])

        elif "m" in x:
            output.append(scale[numbers.index(x[:-1])])

        elif "7" in x or "2" in x:
            output.append(scale[numbers.index(x[:-1])] + x[-1])

        else:
            output.append(scale[numbers.index(x)])

    return output