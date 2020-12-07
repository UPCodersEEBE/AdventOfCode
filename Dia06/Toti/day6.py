def CountDifAnswers(group):
    c = 0
    for i in "abcdefghijklmnopqrstuvwxyz":
        if i in group:
            c += 1
    return c

def CountEveryoneAnsweredYes(group):
    PeopleAnswers = group.split(" ")
    c = 0
    for i in PeopleAnswers[0]:
        x = 0
        for j in PeopleAnswers[1:]:
            x += 1 if i in j else 0
        c +=1 if x == len(PeopleAnswers) - 1 else 0     
    return(c)

    # Manera amb intereseccio de sets, algoritme mes avorrit que el que no esta comentat

    # PeopleAnswers = group.split(" ")
    # x = set(PeopleAnswers[0])
    # for i in PeopleAnswers:
    #     x = x & set(i)
    # return(len(x))

f = open("day6input.txt", "r")
data = f.read()
AnswersRaw = data.split("\n\n")

answers = []
for answer in AnswersRaw:
    x = ""
    for char in answer:
        if char != "\n":
            x += char
        else:
            x += " "
    answers.append(x)

count1 = 0
count2 = 0
for i in answers:
    count1 += CountDifAnswers(i)
    count2 += CountEveryoneAnsweredYes(i)
print(count1, count2)

