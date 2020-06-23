import re
from string import ascii_lowercase

input = open("D:\\Programmieren\\Projekte\\AdventOfCode18\\5.txt", "r")
original = input.readlines()[0]

polymer = original

for x in range(1000):
    for char in ascii_lowercase:
        polymer = polymer.replace(char + char.capitalize(), "")
        polymer = polymer.replace(char.capitalize() + char, "")

print(len(polymer))

#Aufgabe 2

removed = []

for char in ascii_lowercase:
    polymer = original
    polymer = polymer.replace(char, "")
    polymer = polymer.replace(char.capitalize(), "")
    for x in range(3000):
        for c in ascii_lowercase:
            polymer = polymer.replace(c + c.capitalize(), "")
            polymer = polymer.replace(c.capitalize() + c, "")
    removed.append([char, len(polymer)])

for char in removed:
    print(char)