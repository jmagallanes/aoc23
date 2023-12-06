def parseFile():
    seeds = []
    maps = {}
    fullMaps = {}
    with open('test.txt') as inputFile:
        for index, line in enumerate(inputFile):
            line = line.strip()
            #Create list of seeds
            if index == 0:
                for each in line.split(":")[1].split():
                    seeds.append(each)
            #Skip empty lines
            elif line == "": continue
            #Add new dictionary keys
            elif line[0].isalpha():
                maps[line.split()[0]] = []
            #Add map lines to map
            else:
                numList = []
                for num in line.split():
                    numList.append(int(num))
                maps[list(maps)[-1]].append(numList)
    for each in maps:
        fullMaps[each] = {}
        for index in range(100):
            fullMaps[each][index] = index
        for indMap in maps[each]:
            for index in range(indMap[2]):
                fullMaps[each][indMap[1]+index] = indMap[0] + index
    return(fullMaps)

def part1(data):
    return 'TBD'

def part2(data):
    return 'TBD'

def main():
    print('Part 1 Solution: ' + str(part1(data)))
    print('Part 2 Soluction: ' + str(part2(data)))

if __name__ == '__main__':
    main()