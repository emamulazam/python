def make_pizza(size, *toppings):
    print(f"\nMake a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
        