
# Input data into a list where each elf pair is a single index in the list
with open('day4.in') as file:
    pairs = [elf for elf in file.read().strip().split("\n")]

print(pairs)

# Split created list into a list where each elf assigned section is a single index in the list
new_pairs = []
for elf in pairs:
    elf_1 = elf.split(',')[0]
    elf_2 = elf.split(',')[1]
    new_pairs.append(elf_1)
    new_pairs.append(elf_2)

print(new_pairs)

# new_pairs = ['37-87', '36-87', '3-98', '3-84']

# Sets a counter index to 0
index = 0
# Sets a counter index to 0 for all pairs that have one elf which fully contains another elf section
count_fully_contain = 0
# A loop to go through and take each elf starting number and ending number and put them into their own start and end
# variable
while index < len(new_pairs):
    # Sets two variable equal to every other index in the list
    elf_one = new_pairs[index]
    elf_two = new_pairs[index+1]
    # Takes two variables and splits into 4 using the - as the delimiter. Converts to integer type
    elf_one_start = int(elf_one.split('-')[0])
    elf_one_end = int(elf_one.split('-')[1])
    elf_two_start = int(elf_two.split('-')[0])
    elf_two_end = int(elf_two.split('-')[1])
    # If statement to see if the first elf contains the second elf section Adds one to counter if so
    if elf_one_start <= elf_two_start and elf_one_end >= elf_two_end:
        count_fully_contain += 1
    # If statement to see if the second elf contains the first elf section. Adds one to counter if so
    elif elf_two_start <= elf_one_start and elf_two_end >= elf_one_end:
        count_fully_contain += 1
    # Adds two to counter index to get to the next pair of elves the next time through the loop
    index += 2

# Uncomment below lines to test part one working correctly
# print(elf_one_start)
# print(elf_one_end)
# print(elf_two_start)
# print(elf_two_end)
print('The answer to Part 1 of Day 4 is: ' + str(count_fully_contain))

# Begin Part 2

# Sets a counter index to 0
new_index = 0
# Sets a counter index to 0 for all pairs that have one elf which fully contains another elf section
new_count_fully_contain = 0
# A loop to go through and take each elf starting number and ending number and put them into their own start and end
# variable
while new_index < len(new_pairs):
    # Sets two variable equal to every other index in the list
    elf_one = new_pairs[new_index]
    elf_two = new_pairs[new_index+1]
    # Takes two variables and splits into 4 using the - as the delimiter. Converts to integer type
    elf_one_start = int(elf_one.split('-')[0])
    elf_one_end = int(elf_one.split('-')[1])
    elf_two_start = int(elf_two.split('-')[0])
    elf_two_end = int(elf_two.split('-')[1])

    # If statements to check if any of the sections from either elf in each pair overlap with the other. Does not have
    # to be a full overlap
    if elf_one_start <= elf_two_start <= elf_one_end:
        new_count_fully_contain += 1
    elif elf_one_start <= elf_two_end <= elf_one_end:
        new_count_fully_contain += 1
    elif elf_two_start <= elf_one_start <= elf_two_end:
        new_count_fully_contain += 1
    elif elf_two_start <= elf_one_end <= elf_two_end:
        new_count_fully_contain += 1

    # Adds two to counter index to get to the next pair of elves the next time through the loop
    new_index += 2

print('The answer to Part 2 of Day 4 is: ' + str(new_count_fully_contain))