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
    for rowIndex, row in enumerate(matrix):
        tempNum = ""
        num = ""
        for colIndex, char in enumerate(row):
            if char.isdigit():
                tempNum += char
            else:
                if not tempNum == "":
                    print(tempNum + " " + str(rowIndex) + ", " + str(colIndex))
                tempNum = ""

def part2(matrix):
    return "TBD"

def main():
    matrix = buildMatrix()
    print('Part 1 Solution: ' + str(part1(matrix)))
    print('Part 2 Soluction: ' + str(part2(matrix)))

if __name__ == '__main__':
    main()