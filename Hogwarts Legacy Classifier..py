print('**Welcome To Hogwarts School of Witchcraft & Wizardry!**\n')

# Initialize house scores
houses = {
    'Gryffindor': 0,
    'Ravenclaw': 0,
    'Hufflepuff': 0,
    'Slytherin': 0
}

# Question 1
ans1 = int(input('Do you like Dawn or Dusk?\n1) Dawn\n2) Dusk\nEnter your answer (1-2): '))
if ans1 == 1:
    houses['Gryffindor'] += 1
    houses['Ravenclaw'] += 1
    print('\nGryffindor and Ravenclaw both get a +1\n')
elif ans1 == 2:
    houses['Hufflepuff'] += 1
    houses['Slytherin'] += 1
    print('\nHufflepuff and Slytherin both get a +1\n')
else:
    print('Wrong Input!\n')

# Question 2
ans2 = int(input('When I am dead, I want people to remember me as:\n1) The Good\n2) The Great\n3) The Wise\n4) The Bold\nEnter your answer (1-4): '))
if ans2 == 1:
    houses['Hufflepuff'] += 2
    print('Hufflepuff gets a +2\n')
elif ans2 == 2:
    houses['Slytherin'] += 2
    print('Slytherin gets a +2\n')
elif ans2 == 3:
    houses['Ravenclaw'] += 2
    print('Ravenclaw gets a +2\n')
elif ans2 == 4:
    houses['Gryffindor'] += 2
    print('Gryffindor gets a +2\n')
else:
    print('Wrong Input!\n')

# Question 3
ans3 = int(input('Which kind of instrument most pleases your ear?:\n1) The Violin\n2) The Trumpet\n3) The Piano\n4) The Drum\nEnter your answer (1-4): '))
if ans3 == 1:
    houses['Slytherin'] += 4
    print('Slytherin gets a +4\n')
elif ans3 == 2:
    houses['Hufflepuff'] += 4
    print('Hufflepuff gets a +4\n')
elif ans3 == 3:
    houses['Ravenclaw'] += 4
    print('Ravenclaw gets a +4\n')
elif ans3 == 4:
    houses['Gryffindor'] += 4
    print('Gryffindor gets a +4\n')
else:
    print('Wrong Input!\n')

print("✨ The Sorting Hat is thinking... ✨\n")
sorted_house = max(houses, key=houses.get)
print(f"🏆 You belong in... **{sorted_house}**! 🧙‍♂️")

