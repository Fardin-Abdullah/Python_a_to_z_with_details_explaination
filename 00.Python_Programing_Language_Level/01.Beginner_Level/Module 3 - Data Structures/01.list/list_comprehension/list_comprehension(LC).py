"1.Basic List Comprehension"
# Create a list of squares
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

"Explanation: This creates a list of squares of numbers from 0 to 9. The expression x**2 computes the square of x, and for x in range(10) iterates over each number from 0 to 9"

"2.List Comprehension with Conditionals"
# Create a list of even numbers
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8]

"Explanation: This generates a list of even numbers from 0 to 9. The condition if x % 2 == 0 filters out the odd numbers, including only those x that are divisible by 2."

"3.List Comprehension With if-else"
# Label numbers as 'Even' or 'Odd'
labels = ["Even" if x % 2 == 0 else "Odd" for x in range(10)]
print(labels)  # Output: ['Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd']

"Explanation: This creates a list of strings labeling each number from 0 to 9 as “Even” or “Odd”. The if-else statement is used within the list comprehension to determine the label based on whether x is even or odd"

"4.Nested List Comprehension"
# Create a 2D matrix
matrix = [[j for j in range(5)] for i in range(3)]
print(matrix)  # Output: [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]

"Explanation: This generates a 2D matrix (a list of lists) with 3 rows and 5 columns. The inner list comprehension [j for j in range(5)] creates a row, and the outer list comprehension repeats this for 3 rows."

"5.LC with multiple conditions"
# Find numbers divisible by both 2 and 3
divisible_by_2_and_3 = [x for x in range(30) if x % 2 == 0 if x % 3 == 0]
print(divisible_by_2_and_3)  # Output: [0, 6, 12, 18, 24]

"Explanation: This creates a list of numbers from 0 to 29 that are divisible by both 2 and 3. The conditions if x % 2 == 0 and if x % 3 == 0 ensure that only numbers meeting both criteria are included."

"6.Using function in LC"
# Apply a function to each element
def square(x):
    return x * x

squares = [square(x) for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

"Explanation: This applies the square function to each number from 0 to 9, creating a list of their squares. The function square(x) is defined to return the square of x."


"7.LC with string"
# Convert each character to uppercase
uppercase_chars = [char.upper() for char in "hello"]
print(uppercase_chars)  # Output: ['H', 'E', 'L', 'L', 'O']

"Explanation: This converts each character in the string “hello” to uppercase. The method char.upper() is called on each character char in the string."

"8.Flattening a list of list"

# Flatten a 2D list
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = [item for sublist in nested_list for item in sublist]
print(flat_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

"Explanation: This flattens a 2D list into a 1D list. The inner loop for item in sublist iterates over each item in each sublist, and the outer loop for sublist in nested_list iterates over each sublist in the nested list."
