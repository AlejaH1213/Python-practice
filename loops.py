python_topics = ["variables", "control flow", "loops", "modules", "classes"]

length = len(python_topics)
index = 0

while index < length:
  print("I am learning about " + python_topics[index])
  index += 1
#==============================================================================================


#==============================================================================================
dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"

for dog_breed in dog_breeds_available_for_adoption:
  print(dog_breed)
  if dog_breed == dog_breed_I_want:
    print("They have the dog I want!")
    break

ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]
# Loop through the ages list. If an entry is less than 21, skip it and move to the next entry. Otherwise, print() the age.
for age in ages:
  if age < 21:
    continue
  print(age)
#==============================================================================================


#==============================================================================================
# Create a list called single_digits that consists of the numbers 0-9 (inclusive).
single_digits = [0 , 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Create a for loop that goes through single_digits and prints out each one.
# Before the loop, create a list called squares. Assign it to be an empty list to begin with.
squares= []
for num in single_digits:
  # Inside the loop that iterates through single_digits, append the squared value of each element of single_digits to the list squares.
  squares.append(num ** 2)
  print(num)
print(squares)
# Create the list cubes using a list comprehension on the single_digits list. Each element of cubes should be an element of single_digits taken to the third power
cubes = [num ** 3 for num in single_digits]
print(cubes)
#==============================================================================================


#==============================================================================================
odds = list(range(1,20,2))
for value in odds:
  print(value)
# creating a list of multiple of 3 from 3 to 30 
threes = [value for value in range(1,31) if value % 3 == 0]
# printing each value on that list
for value in threes:
  print(value)
# creatinh a list with list comprenhension of the first 10 cubes
cubes = [value ** 3 for value in range(1,11)]
# using a for loop to print the values
for value in cubes:
  print(value)
