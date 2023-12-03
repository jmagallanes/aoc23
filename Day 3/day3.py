def buildMatrix():
    matrix = []
    with open('input.txt') as inputFile:
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


def numCheck(matrix,row,col,num):
    foundSymbol = False
    for i in range(0, len(num)):
        #check left/up
        if not col + i == 0 and not row == 0 and not foundSymbol:
            foundSymbol = checkForSymbol(matrix[row - 1][col + i - 1])
        #check up
        if not row == 0 and not foundSymbol:
            foundSymbol = checkForSymbol(matrix[row - 1][col + i])
        # #check up/right
        if not col + i == len(matrix[0]) - 1 and not row == 0 and not foundSymbol:
            foundSymbol = checkForSymbol(matrix[row - 1][col + i + 1])
        #check right
        if not col + i == len(matrix[0]) - 1 and not foundSymbol:
            foundSymbol = checkForSymbol(matrix[row][col + i + 1])
        #check right/down
        if not col + i == len(matrix[0]) - 1 and not row + 1  == len(matrix) and not foundSymbol:
            foundSymbol = checkForSymbol(matrix[row + 1][col + i + 1])
        #check down
        if not row + 1 == len(matrix) and not foundSymbol:
            foundSymbol = checkForSymbol(matrix[row + 1][col + i])
        #check down/left
        if not col + i == 0 and not row +1 == len(matrix) and not foundSymbol:
            foundSymbol = checkForSymbol(matrix[row + 1][col + i - 1])
        #check left
        if not col + i == 0 and not foundSymbol:
            foundSymbol = checkForSymbol(matrix[row][col + i - 1])
        if foundSymbol:
            return(int(num))
    return 0

def part1(matrix):
    sum = 0
    for rowIndex, row in enumerate(matrix):
        tempNum = ""
        num = ""
        for colIndex, char in enumerate(row):
            if char.isdigit():
                tempNum += char
            elif not tempNum == "":
                sum += numCheck(matrix,rowIndex,colIndex-len(tempNum),tempNum)
                tempNum = ""
            if colIndex == len(matrix[0]) - 1 and not tempNum == "":
                sum += numCheck(matrix,rowIndex,colIndex-len(tempNum)+1,tempNum)
                tempNum = ""
    return sum

def part2(matrix):
    return "TBD"

def main():
    matrix = buildMatrix()
    print('Part 1 Solution: ' + str(part1(matrix)))
    print('Part 2 Soluction: ' + str(part2(matrix)))

if __name__ == '__main__':
    main()