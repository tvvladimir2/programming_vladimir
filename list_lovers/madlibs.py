import random

# adjective1 = input("Adjective 1: ")
# adjective2 = input("Adjective 2: ")
# verb1 = input("Verb 1: ")
# verb2 = input("Verb 2: ")
#
# phrase = f"This cat is so {adjective1}. I would like to {verb1} it and {verb2} it. I'm very {adjective2}."
# phrase2 = f"I'm totally in love with this {adjective1} baby. It is so {adjective2}. Don't you want to {verb2}? Or do you want to {verb1} it."
# print (phrase)
# print (phrase2)

male_list = ['Petko',
             'Mike',
             'Grisa',
             'Niki',
             'Kiko',
             'Luigi'
             ]

female_list = ['Sarah',
             'Luiza',
             'Eliza',
             ]

all_list = male_list + female_list

phrase3 = f"{random.choice(all_list)} told me that {random.choice(all_list)} is in love with {random.choice(all_list)}."
phrase4 = f"Another day, I've heard in the corridor that {random.choice(all_list)} really likes {random.choice(all_list)}."
phrase5 = f"I saw {random.choice(all_list)} kiss {random.choice(all_list)}, another day {random.choice(all_list)} kissed {random.choice(all_list)}, and that is why {random.choice(all_list)} slapped {random.choice(all_list)}."
phrase6 = f"{random.choice(male_list)} is in love with {random.choice(female_list)}. I also think, that she is awesome."

print(all_list)

print(phrase3)
print(phrase4)
print(phrase5)
print(phrase6)
