motorcycles = ['honda', 'yamaha', 'suzuki', 'vodvodi', 'bike']
print(motorcycles)

#motorcycles[0] = 'ducati'
motorcycles.append('ducati')
print(motorcycles)

motorcycles.insert(0, 'hiro')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

popped_motorcycle = motorcycles.pop(1)
print(motorcycles)
print(popped_motorcycle)

print(f"The first motorcycle i owned was a {popped_motorcycle.title()}.")

motorcycles.remove('bike')
print(motorcycles)