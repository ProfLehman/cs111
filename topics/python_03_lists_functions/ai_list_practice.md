# AI Generated Practice Questions - Python Lists Practice Problems

## Problem 1: Indexing a List

### Skill Focus

Accessing items in a list using indexes.

### Scenario

You are given a list of cities. Write code to print:

1. The first city
2. The third city
3. The last city using a negative index

### Starter Code

```python
cities = ["Chicago", "Atlanta", "Denver", "Seattle", "Boston"]

# Print the first city


# Print the third city


# Print the last city using a negative index

```

### Expected Output Format

```text
First city: Chicago
Third city: Denver
Last city: Boston
```

---

## Problem 2: Appending to a List

### Skill Focus

Adding items to a list using `.append()`.

### Scenario

You are building a list of class supplies. Start with an empty list, then add three supplies entered by the user.

### Starter Code

```python
supplies = []

supply = input("Enter a school supply: ")
# Add the supply to the list

supply = input("Enter another school supply: ")
# Add the supply to the list

supply = input("Enter one more school supply: ")
# Add the supply to the list

print("Supplies list:")
print(supplies)
```

### Expected Output Format

```text
Enter a school supply: pencil
Enter another school supply: notebook
Enter one more school supply: calculator

Supplies list:
['pencil', 'notebook', 'calculator']
```

---

## Problem 3: Using `len()`, `sum()`, `max()`, and `min()`

### Skill Focus

Using built-in functions to analyze a numeric list.

### Scenario

You are given a list of quiz scores. Write code to display:

1. The number of scores
2. The total points
3. The highest score
4. The lowest score
5. The average score

### Starter Code

```python
quiz_scores = [88, 74, 92, 100, 67, 85]

# Find the number of scores


# Find the total points


# Find the highest score


# Find the lowest score


# Find the average score


# Print all results

```

### Expected Output Format

```text
Number of scores: 6
Total points: 506
Highest score: 100
Lowest score: 67
Average score: 84.33333333333333
```

---

## Problem 4: Processing a List with a `while` Loop

### Skill Focus

Using a `while` loop and an index variable to process every item in a list.

### Scenario

You are given a list of book titles. Write a program that prints each book title with its list number.

The output should start counting at 1 for the reader, even though Python indexes start at 0.

### Starter Code

```python
books = ["Wonder", "Holes", "The Giver", "Hatchet"]

i = 0

while i < len(books):
    # Print the book number and title

    
    # Increase i so the loop moves forward

```

### Expected Output Format

```text
1. Wonder
2. Holes
3. The Giver
4. Hatchet
```

---

## Problem 5: Parallel Lists

### Skill Focus

Using matching indexes in two lists to connect related data.

### Scenario

You have one list of student names and one list of their test scores. Each student’s score is stored at the same index as their name.

Write a program that prints each student and their score.

### Starter Code

```python
students = ["Amy", "Bob", "Carlos", "Dana"]
scores = [100, 72, 89, 95]

i = 0

while i < len(students):
    # Print the student name and matching score

    
    # Increase i so the loop moves forward

```

### Expected Output Format

```text
Amy scored 100
Bob scored 72
Carlos scored 89
Dana scored 95
```

---

## Optional Challenge Problem: Build a Shopping Cart

### Skill Focus

Combining appending, parallel lists, and list processing.

### Scenario

Create two empty lists:

- `items`
- `prices`

Ask the user to enter three item names and three prices. Add each item to the `items` list and each price to the `prices` list.

Then print a receipt showing each item and price.

### Starter Code

```python
items = []
prices = []

item = input("Enter item name: ")
price = float(input("Enter item price: "))

# Append item and price to the correct lists


item = input("Enter another item name: ")
price = float(input("Enter another item price: "))

# Append item and price to the correct lists


item = input("Enter one more item name: ")
price = float(input("Enter one more item price: "))

# Append item and price to the correct lists


print()
print("Receipt")
print("-------")

i = 0

while i < len(items):
    # Print item and matching price

    
    # Increase i


# Print the total cost

```

---

## Quick Student Reminder

When processing lists with a `while` loop, use this pattern:

```python
i = 0

while i < len(my_list):
    # use my_list[i]
    i = i + 1
```

The index variable `i` helps Python move through the list one item at a time.

---

-- end --

