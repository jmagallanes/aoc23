#Template python file for each day.
def getNums():
    wNums = []
    mNums = []
    with open('test.txt') as inputFile:
        for line in inputFile:
            line = line.strip()
            nums = line.split(':')[1]
            nums = nums.split('|')
            wNums.append(nums[0][:-1].split())
            mNums.append(nums[1][1:].split())
    return([wNums,mNums])

def part1():
    return 'TBD'

def part2():
    return 'TBD'

def main():
    nums = getNums()
    print('Part 1 Solution: ' + str(part1()))
    print('Part 2 Soluction: ' + str(part2()))

if __name__ == '__main__':
    main()