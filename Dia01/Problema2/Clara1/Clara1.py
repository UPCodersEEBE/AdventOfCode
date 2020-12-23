# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


with open("clara1_input.txt") as f:
    lines = []
    for line in f:
        lines.append(int(line))
        
for num1 in lines:
    for num2 in lines:
        for num3 in lines:
            if num1+num2+num3==2020:
                print(num1)
                print(num2)
                print(num3)
                print(num1*num2*num3)
                
            