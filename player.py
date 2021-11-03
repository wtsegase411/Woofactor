import time
import mingus.core.chords as chords
from mingus.containers import Note, NoteContainer
from mingus.midi import fluidsynth

def translate(input, key, sleeptime):
    fluidsynth.init("Nice-Steinway-Lite-v3.0.sf2")

    if (input == "I"):
        fluidsynth.play_NoteContainer(NoteContainer(chords.I(key)))
        time.sleep(sleeptime)

    # Not in Mingus??
    # elif input == "Im":
    #     fluidsynth.play_NoteContainer(NoteContainer(chords.i(key)))
    #     time.sleep(sleeptime)

    elif input == "I7":
        fluidsynth.play_NoteContainer(NoteContainer(chords.I7(key)))
        time.sleep(sleeptime)

    elif (input == "II"):
        fluidsynth.play_NoteContainer(NoteContainer(chords.II(key)))
        time.sleep(sleeptime)

    elif input == "IIm":
        fluidsynth.play_NoteContainer(NoteContainer(chords.ii(key)))
        time.sleep(sleeptime)

    elif input == "II7":
        fluidsynth.play_NoteContainer(NoteContainer(chords.II7(key)))
        time.sleep(sleeptime)

    elif (input == "III"):
        fluidsynth.play_NoteContainer(NoteContainer(chords.III(key)))
        time.sleep(sleeptime)

    elif input == "IIIm":
        fluidsynth.play_NoteContainer(NoteContainer(chords.iii(key)))
        time.sleep(sleeptime)

    elif input == "III7":
        fluidsynth.play_NoteContainer(NoteContainer(chords.III7(key)))
        time.sleep(sleeptime)

    elif (input == "IV"):
        fluidsynth.play_NoteContainer(NoteContainer(chords.IV(key)))
        time.sleep(sleeptime)

    # Not in Mingus??
    # elif input == "IVm":
    #     fluidsynth.play_NoteContainer(NoteContainer(chords.iv(key)))
    #     time.sleep(sleeptime)

    elif input == "IV7":
        fluidsynth.play_NoteContainer(NoteContainer(chords.IV7(key)))
        time.sleep(sleeptime)

    elif (input == "V"):
        fluidsynth.play_NoteContainer(NoteContainer(chords.V(key)))
        time.sleep(sleeptime)

    # Not in Mingus??
    # elif input == "Vm":
    #     fluidsynth.play_NoteContainer(NoteContainer(chords.v(key)))
    #     time.sleep(sleeptime)

    elif input == "V7":
        fluidsynth.play_NoteContainer(NoteContainer(chords.V7(key)))
        time.sleep(sleeptime)

    elif (input == "VI"):
        fluidsynth.play_NoteContainer(NoteContainer(chords.VI(key)))
        time.sleep(sleeptime)

    elif input == "VIm":
        fluidsynth.play_NoteContainer(NoteContainer(chords.vi(key)))
        time.sleep(sleeptime)

    elif input == "VI7":
        fluidsynth.play_NoteContainer(NoteContainer(chords.VI7(key)))
        time.sleep(sleeptime)

    elif (input == "VII"):
        fluidsynth.play_NoteContainer(NoteContainer(chords.VII(key)))
        time.sleep(sleeptime)

    elif input == "VIIm":
        fluidsynth.play_NoteContainer(NoteContainer(chords.vii(key)))
        time.sleep(sleeptime)

    elif input == "VII7":
        fluidsynth.play_NoteContainer(NoteContainer(chords.VII7(key)))
        time.sleep(sleeptime)

    else:
        print("Can't play " + input)

    return None