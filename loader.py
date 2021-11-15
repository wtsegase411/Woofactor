import csv


def main():
    '''
    Returns nested list of rows from 'Digital Representation.csv' and each sublist is processed so blank cells and cells with irrelevent values are removed.
    
        Parameters:
            None
            
        Returns:
            info (list): nested list containing each row in 'Digial Representation.csv' as a sublist
    '''
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
