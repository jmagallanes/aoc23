import re

numbers = [('one','1'),('two','2'),('three','3'),('four','4'),('five','5'),('six','6'),('seven','7'),('eight','8'),('nine','9')]

sum = 0
with open('input.txt') as inputFile:
    for line in inputFile:
        matches = []
        for num in numbers:
            for match in re.finditer(num[0],line):
                matches.append((match.start(),num[1]))
        matches = sorted(matches, reverse=True)
        for match in matches:
            line = line[:match[0]] + match[1] + line[match[0]:]
        digits = []
        for char in line:
            if char.isdigit():
                digits.append(char)
        twoDigits = digits[0] + digits[-1]
        sum += int(twoDigits)
print(sum)