age = int(input("Input your age:\t"))

if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print(f"You admission cost is ${price}.")