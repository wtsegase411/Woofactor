import csv


def test():
    with open('Digital Representation.csv', newline='') as file:
        reader = csv.reader(file)
        info = []
        for row in reader:
            i = 0
            while i < len(row):
                if ' ' in row[i] and i != 0:
                    row[i] = ''
                elif '\r\n' in row[i]:
                    row[i] = row[i][:-2]
                elif row[i] == '':
                    row = row[:i]
                i += 1

            info.append(row)
    return info
