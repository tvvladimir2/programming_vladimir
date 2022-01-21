import random

male_list = ['Risko',
            'Ondrej',
            'Adam',
            'Boris',
            'Jakub',
            'Lukas',
            'Alex',
            'Leo',
            'Leonard']

female_list = ['Aliska',
            'Elizabet',
            'Sarika',
            'Barborka',
            'Saska']

food_list = ['moss',
            'rats',
            'pee',
            'milk duds',
            'shit']

all_list = male_list + female_list

print(f"{random.choice(all_list)} likes {random.choice(all_list)} by {random.randint(0, 100)}% love!?")
print(f"{random.choice(all_list)} likes to eat {random.choice(food_list)}!?REALLY???")
