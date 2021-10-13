import object

def main():
    songList = object.main()
    for i in songList:
        print(i.name)
        for j in i.forms:
            print(j.tag)
            for y in j.chordProgressions:
                print(y.key)
                for q in y.line:
                    print(q.chords)
    return None


if __name__ == '__main__':
    main()
