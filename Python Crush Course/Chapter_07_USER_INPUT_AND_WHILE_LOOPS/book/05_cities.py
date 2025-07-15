prompt = "\nPlease enter the number of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)\t"

while True:
    city = input(prompt)
    
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")