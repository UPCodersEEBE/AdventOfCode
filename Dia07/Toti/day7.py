l = [line.split("\n")[0] for line in open("day7input.txt", "r")]

rules = {}
for i in l:
    rules[i.split(" contain ")[0]] = i.split(" contain ")[1].split(", ")


def RemoveNumberAndDotFromString(str):
    x = ""
    for i in str:
        if i in "abcdefghijklmnopqrstuvwxyz ":
            x += i
    if x[:2] == "no":
        return(x)
    if x[-1] == "g":
        x += "s"
    return(x[1:])

def ContainsShinyGold(bag):
    # print("IN " + str(bag))
    # print("----------")
    for i in rules[bag]:
        # print(RemoveNumberAndDotFromString(i))
        if RemoveNumberAndDotFromString(i) == "shiny gold bags":
            # print("FOUND! +1")
            return True
        elif RemoveNumberAndDotFromString(i) == "no other bags":
            return False
        else:
            # print("---------->")
            if ContainsShinyGold(RemoveNumberAndDotFromString(i)):
                return True
            else:
                continue
    return False

c = 0
for i in rules:
    if i == "shiny gold bags":
        continue
    else:
        # print("SUPER IN "+ i)
        if ContainsShinyGold(i):
            c += 1
            # print("count: "+ str(c))

print(c)

