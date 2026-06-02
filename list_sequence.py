fruits = ["apple", "orange", "mango", "pawpaw"]

list(fruits[1]) # converts a string to list
len(fruits) # finds the length of a list
del fruits[3] # deletes the elements at an index
"mango" in fruits # checks if an element exists"

# Unpacking values from a list
user = ["Incognito", 19, "SEN/25/1497"]
name, age, matric = user
print(name, age, matric)

# Collecting remaining values
name, *rest = user
print(rest) # prints a list of the remainder

# NB: List slicing works the same way as string slicing


numbers = [5, 9, -3, 1, 7, 5]
remaining = [6, -4, 2]; idx = 3
numbers.append(4) # adds an element to the end
numbers.extend(remaining) # joins two lists
numbers.insert(idx, 10) # adds element at an index
numbers.remove(10) # removes a particular element
numbers.pop(-1) # removes element at an index
numbers.sort() # sorts the list in place
new_list = sorted(numbers) # sorts any iterable and returns a new list
# numbers.clear() # empties the list


print(numbers)