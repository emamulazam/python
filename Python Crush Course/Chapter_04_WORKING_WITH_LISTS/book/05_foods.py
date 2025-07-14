my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append("cannoli")
friend_foods.append("ice cream")

print(f"My favorite foods are:\n{my_foods}")
print(f"\nMy friend's favorite foods are:\n{friend_foods}")
print("\n\n")

'''Dose not work'''
my_foods1 = ['pizza', 'falafel', 'carrot cake']
friend_foods1 = my_foods1

my_foods1.append("cannoli")
friend_foods1.append("ice cream")

print(f"My favorite foods are:\n{my_foods1}")
print(f"\nMy friend's favorite foods are:\n{friend_foods1}")