#Template python file for each day.
def parseFile():
    with open('input.txt') as inputFile:
        for line in inputFile:
            line = line.strip()
    return 'TBD'

def part1():
    return 'TBD'

def part2():
    return 'TBD'

def main():
    data = parseFile()
    print('Part 1 Solution: ' + str(part1(data)))
    print('Part 2 Soluction: ' + str(part2(data)))

if __name__ == '__main__':
    main()