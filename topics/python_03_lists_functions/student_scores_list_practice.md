# List Practice: Student Score Analyzer

## Overview

In this challenge, you will build a Python program that collects student names and scores, stores them in lists, and then processes those lists to display useful class information.

You will practice:

- Creating lists
- Adding data to lists with `.append()`
- Using a sentinel value to stop input
- Processing lists with a `while` loop
- Using `len()`, `sum()`, `max()`, and `min()`
- Working with parallel lists

---

## Program Goal

Write a program that allows the user to enter student names and test scores.

The program should keep asking for student names until the user types:

```text
quit
```

For each student entered, the program should ask for that student’s score.

After the user is finished entering data, the program should print:

1. Each student’s name and score
2. The class average
3. The highest score
4. The lowest score

If no scores were entered, the program should print a message saying that no data was entered.

---

# Part 1: Challenge Version

Use the comments below to guide your program.

Try to complete the program using only these comments before looking at the more helpful starter code.

```python
# Create an empty list for student names


# Create an empty list for student scores


# Ask the user to enter the first student name
# The user should type "quit" when finished


# Create a loop that continues as long as the name is not "quit"


    # Ask the user to enter the student's score


    # Add the student name to the names list


    # Add the student score to the scores list


    # Ask the user to enter the next student name


# Print a blank line


# Print a heading for the results


# Create an index variable and set it to 0


# Use a while loop to process every student in the names list


    # Print the current student name and matching score


    # Increase the index variable by 1


# Check whether any scores were entered


    # Calculate the average score


    # Print the average score


    # Print the highest score


    # Print the lowest score


# If no scores were entered


    # Print a message saying no data was entered

```

---

# Part 2: More Helpful Starter Code

If you need more help, use this version.

Some of the structure has been provided, but you still need to complete the missing parts.

```python
names = []
scores = []

name = input("Enter student name or type quit to stop: ")

while name != "quit":
    score = int(input("Enter score: "))

    # Add the name to the names list


    # Add the score to the scores list


    name = input("Enter student name or type quit to stop: ")

print()
print("Student Scores")
print("--------------")

i = 0

while i < len(names):
    # Print the current student's name and score


    # Move to the next index


if len(scores) > 0:
    # Calculate the average score


    # Print the average score


    # Print the highest score


    # Print the lowest score


else:
    # Print a message saying no scores were entered

```

---

# Part 3: Sample Output

Your program should work similar to this example.

```text
Enter student name or type quit to stop: Amy
Enter score: 100
Enter student name or type quit to stop: Bob
Enter score: 72
Enter student name or type quit to stop: Carlos
Enter score: 89
Enter student name or type quit to stop: quit

Student Scores
--------------
Amy scored 100
Bob scored 72
Carlos scored 89

Class average: 87.0
Highest score: 100
Lowest score: 72
```

---

# Part 4: Full Solution

Only look at this section after you have tried the challenge yourself.

```python
names = []
scores = []

name = input("Enter student name or type quit to stop: ")

while name != "quit":
    score = int(input("Enter score: "))

    names.append(name)
    scores.append(score)

    name = input("Enter student name or type quit to stop: ")

print()
print("Student Scores")
print("--------------")

i = 0

while i < len(names):
    print(f"{names[i]} scored {scores[i]}")
    i = i + 1

if len(scores) > 0:
    average = sum(scores) / len(scores)

    print()
    print(f"Class average: {average}")
    print(f"Highest score: {max(scores)}")
    print(f"Lowest score: {min(scores)}")
else:
    print("No scores were entered.")
```

---

# Part 5: Code Walkthrough

## Creating Empty Lists

```python
names = []
scores = []
```

The program starts with two empty lists.

- `names` stores student names.
- `scores` stores student scores.

These are called **parallel lists** because the data at the same index belongs together.

For example:

```python
names[0]
scores[0]
```

refer to the same student.

---

## Getting the First Name

```python
name = input("Enter student name or type quit to stop: ")
```

The program asks for the first student name before the loop begins.

This is important because the loop needs a value to check.

---

## Using the Sentinel Loop

```python
while name != "quit":
```

This loop continues as long as the user does not type `"quit"`.

The word `"quit"` is called a **sentinel value** because it tells the program when to stop collecting data.

---

## Appending Data to the Lists

```python
names.append(name)
scores.append(score)
```

The `.append()` method adds new data to the end of a list.

Each time through the loop:

- the student name is added to `names`
- the student score is added to `scores`

Because they are added during the same loop, they stay matched by index.

---

## Processing the Lists with a While Loop

```python
i = 0

while i < len(names):
    print(f"{names[i]} scored {scores[i]}")
    i = i + 1
```

The variable `i` is the index.

It starts at `0` because Python lists are zero-indexed.

Each time the loop runs:

1. It prints the student at index `i`.
2. It prints the matching score at index `i`.
3. It increases `i` by `1`.

The loop stops when `i` is no longer less than the length of the list.

---

## Checking for an Empty List

```python
if len(scores) > 0:
```

This check prevents an error.

If the user types `"quit"` immediately, then the `scores` list will be empty.

This would cause a problem:

```python
average = sum(scores) / len(scores)
```

because dividing by zero is not allowed.

---

## Calculating the Average

```python
average = sum(scores) / len(scores)
```

This line uses two built-in functions:

- `sum(scores)` adds all the scores.
- `len(scores)` counts how many scores there are.

The total divided by the number of scores gives the class average.

---

## Finding the Highest and Lowest Scores

```python
max(scores)
min(scores)
```

These built-in functions find the highest and lowest numbers in the list.

---

# Part 6: Extension Challenges

After your program works, try one or more of these upgrades.

## Extension 1: Format the Average

Change the average so it displays only two decimal places.

Example:

```text
Class average: 87.00
```

Hint:

```python
print(f"Class average: {average:.2f}")
```

---

## Extension 2: Add Letter Grades

When printing each student’s score, also print a letter grade.

Example:

```text
Amy scored 100, grade A
Bob scored 72, grade C
Carlos scored 89, grade B
```

---

## Extension 3: Count Passing Scores

Assume a passing score is 70 or higher.

Print how many students passed.

---

## Extension 4: Find the Student with the Highest Score

Print the name of the student who earned the highest score.

Example:

```text
Highest scoring student: Amy
```

Hint:

You will need to find the index of the highest score and use that index with the `names` list.

---

# Checklist

Before submitting, make sure your program:

- [ ] Creates a list for names
- [ ] Creates a list for scores
- [ ] Uses `"quit"` as the sentinel value
- [ ] Adds names using `.append()`
- [ ] Adds scores using `.append()`
- [ ] Uses a `while` loop to print all students and scores
- [ ] Uses `len()` to check whether scores were entered
- [ ] Calculates the class average
- [ ] Prints the highest score
- [ ] Prints the lowest score
- [ ] Handles the case where no scores were entered
```

---

-- end --
