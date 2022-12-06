# Imports data and puts each line into a list
with open('day3.in') as file:
    rucksacks = [compartment for compartment in file.read().strip().split("\n")]

print(rucksacks)

# Establishes a dictionary with a priority value for each letter
priorities = {
    "a":1, "b":2, "c":3,
    "d":4, "e":5, "f":6,
    "g":7, "h":8, "i":9,
    "j":10, "k":11, "l":12,
    "m":13, "n":14, "o":15,
    "p":16, "q":17, "r":18,
    "s":19, "t":20, "u":21,
    "v":22, "w":23, "x":24,
    "y":25, "z":26, "A":27,
    "B":28, "C":29, "D":30,
    "E":31, "F":32, "G":33,
    "H":34, "I":35, "J":36,
    "K":37, "L":38, "M":39,
    "N":40, "O":41, "P":42,
    "Q":43, "R":44, "S":45,
    "T":46, "U":47, "V":48,
    "W":49, "X":50, "Y":51,
    "Z":52
}

# Creates new variables of empty lists and strings
new_list = []
letter_list = []
value_list = []
compartment_1 = ''
compartment_2 = ''
priority_total = 0
# for loop to split each rucksack into two compartments, the first half of the string is compartment 1 and the second
# half is compartment 2. Adds these compartments to a new list
for compartment in rucksacks:
    compartment_1 = compartment[:len(compartment)//2]
    compartment_2 = compartment[len(compartment)//2:]
    new_list.append(compartment_1)
    new_list.append(compartment_2)
# Searches each rucksack for the common letter between the first and second compartment
    for letter in compartment_1[0:]:
# Adds the letters that are in each compartment to a new list, stops iterating through compartment 1 after it finds one match
        if letter in compartment_2:
            letter_list.append(letter)
            break
# Creates a new list with the assigned priority values
for value in letter_list:
    value_list.append(priorities[value])
# Sums the total priority values across all rucksacks
for value in letter_list:
    priority_total += priorities[value]

for compartment in rucksacks:
    elf_1 = ''
    elf_2 = ''
    elf_3 = ''




print(new_list)
print(letter_list)
print(value_list)
print(priority_total)


