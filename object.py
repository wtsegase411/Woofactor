import loader
import Progressions


def main():
    print("START HERE *********************************************************")
    songList = loader.main()
    output = [] #list of Song objects
    for i in songList: #iterates through file by row
        name = ""
        lines = []
        progs = []
        forms = []
        j = 0
        while j < (len(i)-1): #iterates through each cell in row
            line = []
            if j == 0:
                name = i[j]
                j += 1
            elif "line" in i[j] and len(i[j+1]) <= 4: #Marking start of line
                x = j
                j += 1
                while j < i.index("intro"):
                    if "line" not in i[j]:
                        j += 1
                    else: #marking end of line, start of next line
                        lines.append(i[x:j])
                        x = j
                        j += 1
                lines.append(i[x:j])
            elif len(i[j]) >= 4 and "line" not in i[j] and ("II" or "V") not in i[j]: #Check for start of progression
                z = j
                j += 1
                success = False
                while j < (len(i)-2):
                    if len(i[j+1]) >= 4 and "line" not in i[j+1] and ("II" or "V") not in i[j+1]: #Check for end of progression
                        progs.append(i[z:j+1])
                        success = True
                        break
                    else:
                        j += 1
                if not success: #Grabs last progression
                    progs.append(i[z:])
            else:
                j += 1
        for k in range(len(lines)):
            lines[k] = Progressions.Line(lines[k][0], lines[k][1:])
        for l in range(len(progs)):
            for o in range(len(progs[l])):
                if "line" in progs[l][o]: #Replaces line strings with corresponding Line objects
                    progs[l][o] = lines[int(progs[l][o][-1])-1]
            progs[l][1] = Progressions.Progression(progs[l][1], progs[l][2:])
            progs[l] = progs[l][:2]
            if forms:
                for n in forms:
                    if (progs[l][0] == n.tag):
                        for q in n.chordProgressions:
                            if (q != progs[l][-1]): #Repeat progressions under the same tag are not allowed
                                n.chordProgressions.append(progs[l][-1])
                    elif n == forms[-1]:
                        forms.append(Progressions.Form(progs[l][0], progs[l][-1]))
            else:
                forms.append(Progressions.Form(progs[l][0], progs[l][-1]))
        output.append(Progressions.Song(name, forms))
    for song in output:
        print(song.name)
        for form in song.forms:
            print(form.tag)
            for y in form.chordProgressions:
                print(y.key)
                for q in y.line:
                    print(q.chords)
    return output
