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

def checkForSymbol(char):
    if char.isdigit():
        return False
    elif char == '.':
        return False
    elif char.isalpha():
        return False
    else:
        return True


def numCheck(matrix,row,colIndex,num):
    start = colIndex - len(num)
    foundSymbol = False
    for i in range(0, len(num)):
        #check left/up
        if not start + i == 0 and not row == 0:
            checkForSymbol(matrix[row-1][start + i-1])
        #check up
        if not row == 0:
            checkForSymbol(matrix[row-1][start + i])
        # #check up/right
        if not start + i == len(matrix[0]) and not row == 0:
            checkForSymbol(matrix[row-1][start + i + 1])
        #check right
        if not start + i == len(matrix[0]):
            checkForSymbol(matrix[row][start + i + 1])
        #check right/down
        if not start + i == len(matrix[0]) and not row + 1  == len(matrix):
            checkForSymbol(matrix[row+1][start + i + 1])
        #check down
        if not row + 1 == len(matrix):
            checkForSymbol(matrix[row+1][start + i])
        #check down/left
        if not start + i -1 == 0 and not row +1 == len(matrix):
            checkForSymbol(matrix[row+1][start + i - 1])
        #check left
        if not start + i - 1 == 0:
            checkForSymbol(matrix[row][start + i - 1])

def part1(matrix):
    for rowIndex, row in enumerate(matrix):
        tempNum = ""
        num = ""
        for colIndex, char in enumerate(row):
            if char.isdigit():
                tempNum += char
            elif not tempNum == "":
                numCheck(matrix,rowIndex,colIndex,tempNum)
                tempNum = ""
            if colIndex == len(matrix[0]) - 1 and not tempNum == "":
                numCheck(matrix,rowIndex,colIndex,tempNum)
                tempNum = ""

def part2(matrix):
    return "TBD"

def main():
    matrix = buildMatrix()
    print('Part 1 Solution: ' + str(part1(matrix)))
    print('Part 2 Soluction: ' + str(part2(matrix)))

if __name__ == '__main__':
    main()