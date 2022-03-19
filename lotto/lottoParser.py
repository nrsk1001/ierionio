file = open("lotto.txt", "r", encoding="utf-8")
lines = file.readlines()
file.close()


file = open("result.txt", "w")
for line in lines:
    chapter, date, numWinner, winnings, a, b, c, d, e, f, bonus = line.split()
    numbers = [a, b, c, d, e, f]
    message = chapter
    for number in numbers:
        message += (" " + number)
    message += "\n"
    file.write(message)

file.close()