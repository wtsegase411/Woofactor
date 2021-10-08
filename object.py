import loader
import Progressions


def main():
    chords = ["I", "II", "III", "IV", "V", "VI", "VII"]

    songList = loader.main()
    output = [] #list of Song objects
    nameList = []
    linesList = []
    progressionsList = []
    for i in songList:
        name = ""
        progressions = []
        lines = []
        structure = []
        for j in i:
            line = []
            if j.index() == 0:
                name = j
            elif "line" in j:
                line += j
            elif j in chords:
                line += j
            elif chordChecker(j):
                line += j
            elif j in progressions:
                for m in range(j.index()+1,len(i)):
                    if "line" not in m:
                        progressions += i[j.index():m-1]
            elif intChecker(j):
                for n in range(j.index()+1,len(i)):
                    if "line" not in n:
                        progressions += i[j.index():n-1]
            elif j == "structure":
                structure = i[j.index():]
            lines += line
        for k in lines:
            lines[k] = Progressions.Line(k[0], k[1:])
        for l in progressions:


def chordChecker(string):
    chars = ["m", "7"]
    for i in string:
        if i in chars:
            return True
    return False


def intChecker(string):
    ints = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    for i in string:
        if i in ints:
            return True
    return False