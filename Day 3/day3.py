def buildMatrix():
    matrix = []
    with open('test.txt') as inputFile:
        for line in inputFile:
            line = line.strip()
            row = []
            for char in line:
                row.append(char)
            matrix.append(row)
    return(matrix)

def part1(matrix):
    return "TBD"

def part2(matrix):
    return "TBD"

def main():
    matrix = buildMatrix()
    print('Part 1 Solution: ' + str(part1(matrix)))
    print('Part 2 Soluction: ' + str(part2(matrix)))

if __name__ == '__main__':
    main()