import cmath

def parseFile():
    time = []
    distance = []
    with open('input.txt') as inputFile:
        for index,line in enumerate(inputFile):
            if index == 0:
                time = line.split(':')[1].split()
            else:
                distance = line.split(':')[1].split()
    return(time,distance)

def getFirstWin(time,distance):
    dis = (time**2) - (4*distance)
    return(int(((abs((-time+cmath.sqrt(dis))/(2)))//1))+1)


def part1(data):
    time = data[0]
    distance = data[1]
    answer = 1
    for index in range(len(time)):
       answer *= int(time[index]) - (getFirstWin(int(time[index]),int(distance[index])))*2+1
    return(answer)

def part2(data):
    return 'TBD'

def main():
    data = parseFile()
    print('Part 1 Solution: ' + str(part1(data)))
    print('Part 2 Soluction: ' + str(part2(data)))

if __name__ == '__main__':
    main()