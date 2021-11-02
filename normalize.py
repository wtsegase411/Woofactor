
def main(inList):

    output = []

    for x in inList:
        if (sum(inList) != 0):
            output.append(round(x/sum(inList),2))

    return output