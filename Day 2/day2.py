redMax = 12
greenMax = 13
blueMax = 15

def getGames():
    games = []
    with open('input.txt') as inputFile:
        for line in inputFile:
            line = line.strip()
            game = []
            for setGrab in (line[line.find(':')+1:]).split(';'):
                indSet = []
                for indGrab in setGrab.split(','):
                    indGrab = indGrab.split()
                    indSet.append(indGrab)
                game.append(indSet)
            games.append(game)
    return games

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

def part1(games):
    idSums = 0
    for index, game in enumerate(games):
        possible = True
        for setGrab in game:
            for indGrab in setGrab:
                if not checkMax(indGrab):
                    possible = False
        if possible:
            idSums += index + 1
    return(idSums)

def part2(games):
    powerSum = 0
    for game in games:
        redCubes = 0
        greenCubes = 0
        blueCubes = 0
        for setGrab in game:
            for indGrab in setGrab:
                match indGrab[1]:
                    case 'red':
                        if int(indGrab[0]) > redCubes:
                            redCubes = int(indGrab[0])
                    case 'green':
                        if int(indGrab[0]) > greenCubes:
                            greenCubes = int(indGrab[0])
                    case 'blue':
                        if int(indGrab[0]) > blueCubes:
                            blueCubes = int(indGrab[0])
        powerSum += redCubes*blueCubes*greenCubes
    return(powerSum)


def main():
    games = getGames()
    print('Part 1 Solution: ' + str(part1(games)))
    print('Part 2 Soluction: ' + str(part2(games)))

if __name__ == '__main__':
    main()