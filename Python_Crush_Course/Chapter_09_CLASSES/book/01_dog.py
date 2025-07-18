class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def sit(self):
        print(f"{self.name.title()} is now sitting.")
        
    def roll_over(self):
        print(f"{self.name.title()} rolled over!")

  
my_dog = Dog('willie', 6)
print(f"My dog's name is {my_dog.name.title()}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print()

your_dog = Dog('lucy', 3)
print(f"Your dog's name is {your_dog.name.title()}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()