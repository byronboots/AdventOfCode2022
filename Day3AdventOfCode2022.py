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

# Part 2
# Creates new lists for each group
group_1 = []
group_2 = []
group_3 = []
new_letter_list = []
new_value_list = []
group_bag_1 = ''
group_bag_2 = ''
group_bag_3 = ''
new_priority_total = 0
# Takes every 3rd rucksack starting at the first rucksack and adds to group 1 list
for compartment in rucksacks[0::3]:
    # group_bag_1 = compartment
    group_1.append(compartment)
# Takes every 3rd rucksack starting at the second rucksack and adds to group 2 list
for compartment in rucksacks[1::3]:
    # group_bag_2 = compartment
    group_2.append(compartment)
# Takes every 3rd rucksack starting at the third rucksack and adds to group 3 list
for compartment in rucksacks[2::3]:
    # group_bag_3 = compartment
    group_3.append(compartment)

# letter_set = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


# Sets a counter index to 0
index = 0
# While loop that runs as long as the index is less than the length of the remaining rucksacks list to iterate through
while index < len(rucksacks):
    # Sets 3 variables equal to be the first, second, and third strings up next in the rucksacks list each time the loop runs
    group_bag_1 = rucksacks[index]
    group_bag_2 = rucksacks[index+1]
    group_bag_3 = rucksacks[index+2]
    # iterates through the letters in the first bag from the group of rucksacks to see if any letters appear in both of
    # the other two bags in the group. Once found the letter is added to a new list, the index is increased by 3 and
    # the loop is broken so we stop searching through letters for a match
    for letter in group_bag_1:
        if letter in group_bag_2 and letter in group_bag_3:
            new_letter_list.append(letter)
            index += 3
            break

# Creates a new list with the assigned priority values
for value in new_letter_list:
    new_value_list.append(priorities[value])
# Sums the total priority values across all rucksacks
for value in new_letter_list:
    new_priority_total += priorities[value]



# print(new_list)
# print(letter_list)
# print(value_list)
# print(priority_total)
print(group_1)
print(group_2)
print(group_3)
print(new_letter_list)
print(new_value_list)
print(new_priority_total)


