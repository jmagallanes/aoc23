def parseFile():
    seeds = []
    with open('test.txt') as inputFile:
        for index, line in enumerate(inputFile):
            line = line.strip()
            #Create list of seeds
            if index == 0:
                for each in line.split(":")[1].split():
                    seeds.append(each)
    return(seeds)

def part1():
    return 'TBD'

def part2():
    return 'TBD'

def main():
    print(parseFile())
    print('Part 1 Solution: ' + str(part1()))
    print('Part 2 Soluction: ' + str(part2()))

if __name__ == '__main__':
    main()