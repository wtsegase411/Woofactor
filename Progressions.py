class Song:
    def __init__(self, n, p, s):
        self.name = n
        self.progressions = p
        self. structures = s
        pass


class Progression:
    def __init__(self, n, k, ln):
        self.name = n
        self.key = k
        self.line = ln
        pass


class Line:
    def __init__(self, i, c):
        self.identifier = i
        self.chordProgression = c
        pass
