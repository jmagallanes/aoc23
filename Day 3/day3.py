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

def buildNumDict(matrix):
    numDict = {}
    for rowIndex, row in enumerate(matrix):
        tempNum = ""
        num = ""
        for colIndex, char in enumerate(row):
            if char.isdigit():
                tempNum += char
            elif not tempNum == "":
                start = colIndex-len(tempNum)
                for i in range(0,len(tempNum)):
                        numDict[(rowIndex,colIndex-i-1)] = tempNum
                tempNum = ""
    return numDict

def part2(matrix,numDict):
    answer = 0
    for rowIndex, row in enumerate(matrix):
        for colIndex, char in enumerate(row):
            if matrix[rowIndex][colIndex] == "*":
                values = []
                adjCoordinates = [(rowIndex,colIndex-1),(rowIndex,colIndex+1)]
                if matrix[rowIndex-1][colIndex-1].isdigit() and matrix[rowIndex-1][colIndex].isdigit() and matrix[rowIndex-1][colIndex+1].isdigit():
                    adjCoordinates.append((rowIndex-1,colIndex-1))
                elif matrix[rowIndex-1][colIndex-1].isdigit() and matrix[rowIndex-1][colIndex].isdigit():
                    adjCoordinates.append((rowIndex-1,colIndex-1))
                elif matrix[rowIndex-1][colIndex].isdigit() and matrix[rowIndex-1][colIndex+1].isdigit():
                    adjCoordinates.append((rowIndex-1,colIndex))
                else:
                    adjCoordinates.append((rowIndex-1,colIndex-1))
                    adjCoordinates.append((rowIndex-1,colIndex+1))
                if matrix[rowIndex+1][colIndex-1].isdigit() and matrix[rowIndex+1][colIndex].isdigit() and matrix[rowIndex+1][colIndex+1].isdigit():
                    adjCoordinates.append((rowIndex+1,colIndex-1))
                elif matrix[rowIndex+1][colIndex-1].isdigit() and matrix[rowIndex+1][colIndex].isdigit():
                    adjCoordinates.append((rowIndex+1,colIndex-1))
                elif matrix[rowIndex+1][colIndex].isdigit() and matrix[rowIndex+1][colIndex+1].isdigit():
                    adjCoordinates.append((rowIndex+1,colIndex))
                else:
                    adjCoordinates.append((rowIndex+1,colIndex-1))
                    adjCoordinates.append((rowIndex+1,colIndex+1))
                for co in adjCoordinates:
                    if co in numDict.keys():
                        values.append(numDict[co])
                if len(values) == 2:
                    answer += int(values[0])*int(values[1])
    return answer

def main():
    matrix = buildMatrix()
    numDict = buildNumDict(matrix)
    print('Part 1 Solution: ' + str(part1(matrix)))
    print('Part 2 Soluction: ' + str(part2(matrix,numDict)))

if __name__ == '__main__':
    main()