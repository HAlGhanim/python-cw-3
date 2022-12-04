# الجزء الاول
favorite_animals = ['dog','cat','monkey','rabbit']  
print(favorite_animals)
print(favorite_animals[1])
favorite_animals.remove('monkey')
print(favorite_animals)

# الجزء الثاني
favorite_animals.append('chimpanzee')
print(favorite_animals)
for fav in favorite_animals:
    print(f"I love {fav}")

# الجزء الثالث
numbers =[5, 4, 3, 2, 1]
numbers_sum = 0
for numbers in numbers:
    numbers_sum += numbers
print(numbers_sum)

