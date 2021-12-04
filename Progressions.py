class Song:
    def __init__(self, n, f):
        self.name = n
        self.forms = f
        pass


class Progression:
    def __init__(self, k, ln):
        self.key = k
        self.line = ln
        pass


class Line:
    def __init__(self, i, c):
        self.identifier = i
        self.chords = c
        pass


class Form:
    def __init__(self, t, p):
        self.tag = t
        self.chordProgressions = [p]