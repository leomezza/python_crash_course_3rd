print("Equality and inequality with strings")
car = 'subaru'
print(car == 'subaru')
print(car != 'subaru')

print("\nTests using the lower() method")
car = 'Subaru'
print(car.lower() == 'subaru')
print(car == 'subaru')

print("\nNumericals tests")
number = 45
print(number == 45)
print(number != 45)
print(number > 40)
print(number < 40)
print(number >= 46)
print(number <= 45)

print("\nTests using AND and OR")
number = 45
print(number == 45 and number != 45)
print(number == 45 or number != 45)

print("\nTest wheter an item is in a list")
list = [1, 3, 5, 7]
print(6 in list)
print(7 in list)

print("\nTest wheter an item is not in a list")
list = [1, 3, 5, 7]
print(6 not in list)
print(7 not in list)
