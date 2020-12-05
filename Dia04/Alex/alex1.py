# Pro tip: he afegit 2 enters al final del input :) sino no pillava un dels passaports

passports = []

with open("d2pr1.dat") as f:
    passport = ""
    for line in f:
        passportraw = line.split(" ")
        for i in range(len(passportraw)):
            passport += str(passportraw[i].replace("\n", "") + " ")
        if line == "\n":
            passports.append(passport)
            passport = ""


def ButIsItReallyValid(p):
    psplit = p.split()
    ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    for atr in psplit:
        if "byr" in atr:
            if int(atr[4:]) < 1920 or int(atr[4:]) > 2002:
                return False
        elif "iyr" in atr:
            if int(atr[4:]) < 2010 or int(atr[4:]) > 2020:
                return False
        elif "eyr" in atr:
            if int(atr[4:]) < 2020 or int(atr[4:]) > 2030:
                return False
        elif "hgt" in atr:
            if atr[-2:] == "cm":
                if int(atr[4:-2]) < 150 or int(atr[4:-2]) > 193:
                    return False
            elif atr[-2:] == "in":
                if int(atr[4:-2]) < 59 or int(atr[4:-2]) > 76:
                    return False
            else:
                return False
        elif "hcl" in atr:
            if atr[4] != "#":
                return False
            else:
                for c in atr[-6:]:
                    if c not in "0123456789abcdef":
                        return False
        elif "ecl" in atr:
            if atr[-3:] not in ecl:
                return False
        elif "pid" in atr:
            for n in atr[-9:]:
                if n not in "0123456789":
                    return False
    return True


check = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

valid = True
t = 0
reallyt = 0
for passport in passports:
    for c in check:
        if c not in passport:
            valid = False
    if valid:
        t += 1
        reallyt += ButIsItReallyValid(passport)
    valid = True

print(t, reallyt)

test = ""
print(ButIsItReallyValid(passport))