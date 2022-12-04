
with open('day1.in') as file:
    data = [elf for elf in file.read().strip().split("\n")]

# print(data)


def Count_Calories(data):
    elf_calories = 0
    elf_calories_temp = 0
    for instance in data:
        if instance == '':
            elf_calories_temp = 0
        else:
            elf = int(instance)
            elf_calories_temp += elf
            if elf_calories_temp > elf_calories:
                elf_calories = elf_calories_temp

    return elf_calories

print(Count_Calories(data))

def Count_Top_Three_Calories(data):
    max_elf_one = 0
    max_elf_two = 0
    max_elf_three = 0
    elf_calories_temp = 0
    for instance in data:
        if instance == '':
            elf_calories_temp = 0
        else:
            elf = int(instance)
            elf_calories_temp += elf
            if elf_calories_temp > max_elf_one:
                max_elf_three = max_elf_two
                max_elf_two = max_elf_one
                max_elf_one = elf_calories_temp
            elif elf_calories_temp > max_elf_two:
                max_elf_three = max_elf_two
                max_elf_two = elf_calories_temp
            elif elf_calories_temp > max_elf_three:
                max_elf_three = elf_calories_temp

    Top_3_Calories = max_elf_one + max_elf_two + max_elf_three

    return Top_3_Calories

print(Count_Top_Three_Calories(data))


