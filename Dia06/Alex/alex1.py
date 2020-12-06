# Pro tip: he afegit 1 enter al final del input :) sino no em pillava un dels passaports

answers = []

with open("d6") as f:
    answer = ""
    n = 0
    for line in f:
        answerraw = line.split(" ")
        n += 1
        for i in range(len(answerraw)):
            answer += str(answerraw[i].replace("\n", ""))
        if line == "\n":
            n -= 1
            answers.append([answer, n])
            answer = ""
            n = 0
c1 = 0
c2 = 0
for answer in answers:
    for char in "qwertyuiopasdfghjklzxcvbnm":
        if char in answer[0]:
            c1 += 1
        if answer[0].count(char) == answer[1]:
            c2 += 1

print(c1, c2)
