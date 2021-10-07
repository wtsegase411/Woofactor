class Song:
    name = ""
    progressions = []
    structures = []

    def __init__(self, n, p, s):
        self.name = n
        self.progressions = p
        self. structures = s


class Progression:
    name = ""
    key = ''
    line = []

    def __init__(self, n, k, ln):
        self.name = n
        self.key = k
        self.line = ln


class Line:
    identifier = ""
    chordProgression = []

    def __init__(self, i, c):
        self.identifier = i
        self.chordProgression = c


line1 = Line("Line1", ['Vim', 'IV', 'I', 'V'])
line2 = Line("Line2", ['IIm', 'IIm', 'IV', 'V'])
line3 = Line("Line3", ['I', 'I', 'VIm', 'VIm', 'IIm', 'IIm', 'V', 'V'])
line4 = Line("Line4", ['VIm', 'IV', 'I', 'V'])

intro = Progression("intro", 'C', [line1, line1])
verse = Progression("verse", 'C', [line1, line1, line1, line1])
pre_chorus = Progression("pre_chorus", 'C', [line2, line2])
chorus = Progression("chorus", 'C', [line3, line3, line4, line4])
outro = Progression("outro", 'C', [line1])

song = Song("All of me", [intro, verse, pre_chorus, chorus, outro], [intro.name, verse.name, pre_chorus.name, chorus.name, verse.name, pre_chorus.name, chorus.name, pre_chorus.name,outro.name])

