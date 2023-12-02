redMax = 12
greenMax = 13
blueMax = 15

def checkMax(indGrab):
    match indGrab[1]:
        case 'red':
            if int(indGrab[0]) > redMax:
                return False
        case 'green':
            if int(indGrab[0]) > greenMax:
                return False
        case 'blue':
            if int(indGrab[0]) > blueMax:
                return False
    return True

def part1():
    idSums = 0
    with open('input.txt') as inputFile:
        for line in inputFile:
            possible = True
            line = line.strip()
            for setGrab in (line[line.find(':')+1:]).split(';'):
                for indGrab in setGrab.split(','):
                    indGrab = indGrab.split()
                    if not checkMax(indGrab):
                        possible = False
            if possible:
                idSums += int(line[line.find(' '):line.find(':')])
    return(idSums)

def main():
    print('Part 1 Solution: ' + str(part1()))

if __name__ == '__main__':
    main()