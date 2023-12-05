def getNums():
    wNums = []
    mNums = []
    with open('input.txt') as inputFile:
        for line in inputFile:
            line = line.strip()
            nums = line.split(':')[1]
            nums = nums.split('|')
            wNums.append(nums[0][:-1].split())
            mNums.append(nums[1][1:].split())
    return([wNums,mNums])

def getMatchesDict(nums):
    matchesDict = {}
    for index,mNums in enumerate(nums[1]):
        matches = 0
        for mNum in mNums:
            if mNum in nums[0][index]:
                matches += 1
        matchesDict[index + 1] = matches
    return(matchesDict)

def part1(nums):
    totalPoints = 0
    for index,mNums in enumerate(nums[1]):
        points = 0
        for mNum in mNums:
            if mNum in nums[0][index]:
                if points == 0: points = 1
                else: points = points * 2
        totalPoints += points
    return(totalPoints)

def part2(nums):
    matchesDict = getMatchesDict(nums)
    matchesList = []
    for key,value in matchesDict.items():
        matchesList.append([key,value])
    for each in matchesList:
        for index in range(1,matchesDict[each[0]]+1):
            matchesList.append([each[0]+index,matchesDict[each[0]+index]])
    return(len(matchesList))

def main():
    nums = getNums()
    print('Part 1 Solution: ' + str(part1(nums)))
    print('Part 2 Soluction: ' + str(part2(nums)))

if __name__ == '__main__':
    main()