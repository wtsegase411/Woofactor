
def main(inList):
    '''
        Normalizes a list of integers by dividing each element by the sum of the list.

        Parameters:
            inList (list): a series of numbers to be normalized

        Returns:
            output (list): a normalized list of numbers rounded to the 2 decimals.
    '''

    output = []

    for x in inList:
        if (sum(inList) != 0):
            output.append(round(x/sum(inList),2))

    return output