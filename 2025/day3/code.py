banks = []
with open("input.txt", "r") as file:
    input = file.readlines()
    for line in input:
        banks.append(int(line.strip()))

def get_char(number, n):
    return number // 10**n % 10

totaljoltage = 0
for bank in banks:
    first = 0
    second = 0
    for c in range(len(str(bank))):
        if get_char(bank, c) >= first and c > 0:
            if first > second:
                second = first
            first = get_char(bank, c)
        elif c == 0:
            second = get_char(bank, c)
    totaljoltage += int(str(first) + str(second))

print(f"TOTAL JOLTABLE: {totaljoltage}")