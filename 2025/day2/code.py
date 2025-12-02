intervals = []
with open("input.txt", "r") as file:
        input = file.readlines()
        for line in input:
            # .extend() is different from .append() -> adds multiple elements from an iterable to the end of the list, while .append() adds a single element to the end of the list.
            # .split() splits a string into a list where each word is a list item
            intervals.extend(line.split(','))

def get_digit(number, n):
    return number // 10**n % 10

sumids = 0
for interval in intervals:
    first, last = interval.split('-') # works because there is only one '-'
    for i in range(int(first), int(last) + 1): # numbers inside the inverval
        invalidid = True
        leng = len(str(i))
        if (leng % 2) != 0: # odd number of digits
            invalidid = False
        else:
            for digit in range(leng // 2): # half of the digits
                if get_digit(i, digit) != get_digit(i, leng // 2 + digit): # compare the two parts digit by digit, right to left
                    invalidid = False

        if invalidid == True:
            sumids += i
        
print(f"sum of all IDs for part 1: {sumids}")
