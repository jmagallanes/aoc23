sum = 0
with open('input.txt') as inputFile:
    for line in inputFile:
        digits = []
        for char in line:
            if char.isdigit():
                digits.append(char)
        twoDigits = digits[0] + digits[-1]
        sum += int(twoDigits)
print(sum)