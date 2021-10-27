import csv


def main():
    with open('Digital Representation.csv', newline='') as file:
        reader = csv.reader(file)
        info = []
        for row in reader:
            for i in range(len(row)):
                if ' ' in row[i]:
                    row[i] = ''
                elif '\r\n' in row[i]:
                    row[i] = row[i][:-2]
                elif row[i] == '' and row[i + 1] == '':
                    row = row[:i]
                    break
            info.append(row)
    return info
