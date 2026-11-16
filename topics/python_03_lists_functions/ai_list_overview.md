# AI - Learning Lists summary of Lehman class notes

## Step-by-Step Plan: Learning to Process Data in Lists

### Step 1: Understand Why Lists Matter

**Goal:** Recognize when a list is better than individual variables.

Start by comparing these two approaches:

```python
score1 = 85
score2 = 92
score3 = 78
```

versus:

```python
scores = [85, 92, 78]
```

Ask yourself:

- Which version is easier to expand?
- Which version is easier to loop through?
- Which version is easier to calculate an average from?

**Practice Task:**

Create three separate lists:

```python
names = ["Amy", "Bob", "Carlos"]
scores = [100, 72, 89]
prices = [19.99, 5.50, 10.00]
```

Then explain in your own words what each list stores.

---

### Step 2: Practice Accessing List Items by Index

**Goal:** Learn how to retrieve specific pieces of data from a list.

Use this list:

```python
fruits = ["Apple", "Banana", "Cherry"]
```

Practice accessing each item:

```python
print(fruits[0])
print(fruits[1])
print(fruits[2])
```

Then practice negative indexing:

```python
print(fruits[-1])
```

**Key Concept:**

Python starts counting at `0`, not `1`.

So:

```python
fruits[0]
```

means the first item.

**Practice Task:**

Create a list of five favorite foods. Print:

- The first food
- The third food
- The last food using a negative index

Example:

```python
foods = ["Pizza", "Tacos", "Pasta", "Sushi", "Burgers"]

print(foods[0])
print(foods[2])
print(foods[-1])
```

---

### Step 3: Learn to Grow a List with `.append()`

**Goal:** Understand how to add data to a list while a program is running.

Start with an empty list:

```python
names = []
```

Then add items:

```python
names.append("Alice")
names.append("Bob")
names.append("Carlos")

print(names)
```

**Practice Task:**

Create an empty list called `scores`. Append three numbers to it.

```python
scores = []

scores.append(85)
scores.append(92)
scores.append(78)

print(scores)
```

Then print:

```python
print(len(scores))
```

This shows how many items are in the list.

---

### Step 4: Use a Sentinel Loop to Collect List Data

**Goal:** Let the user keep entering data until they decide to stop.

A **sentinel value** is a special input that tells the loop to end.

Example:

```python
names = []

name = input("Enter a name or type quit to stop: ")

while name != "quit":
    names.append(name)
    name = input("Enter a name or type quit to stop: ")

print(names)
```

**What this teaches:**

- Start with an empty list.
- Ask the user for data.
- Add each valid entry using `.append()`.
- Stop when the user enters `"quit"`.

**Practice Task:**

Write a program that asks the user to enter test scores. The user should type `-1` to stop.

```python
scores = []

score = int(input("Enter a score or -1 to stop: "))

while score != -1:
    scores.append(score)
    score = int(input("Enter a score or -1 to stop: "))

print(scores)
```

---

### Step 5: Use Built-in List Functions

**Goal:** Use Python’s built-in tools to analyze numeric lists.

Start with this list:

```python
scores = [85, 92, 78, 100, 67]
```

Then practice:

```python
print(len(scores))
print(sum(scores))
print(max(scores))
print(min(scores))
```

These answer useful questions:

| Question | Python Function |
|---|---|
| How many scores are there? | `len(scores)` |
| What is the total? | `sum(scores)` |
| What is the highest score? | `max(scores)` |
| What is the lowest score? | `min(scores)` |

To calculate the average:

```python
average = sum(scores) / len(scores)
print(average)
```

**Practice Task:**

Create a list of prices and print:

- Number of prices
- Total cost
- Highest price
- Lowest price
- Average price

Example:

```python
prices = [19.99, 5.50, 10.00, 25.75]

print(len(prices))
print(sum(prices))
print(max(prices))
print(min(prices))

average = sum(prices) / len(prices)
print(average)
```

---

### Step 6: Process a List with a `while` Loop

**Goal:** Learn how to visit every item in a list one at a time.

Use this list:

```python
items = ["Laptop", "Mouse", "Keyboard"]
```

Process it with a `while` loop:

```python
i = 0

while i < len(items):
    print(items[i])
    i = i + 1
```

**Important Pattern:**

```python
i = 0
while i < len(list_name):
    process list_name[i]
    i = i + 1
```

The variable `i` is the index. It starts at `0` and increases by `1` each time through the loop.

**Practice Task:**

Create a list of student names and print each name using a `while` loop.

```python
students = ["Amy", "Bob", "Carlos"]

i = 0

while i < len(students):
    print(students[i])
    i = i + 1
```

---

### Step 7: Process Parallel Lists

**Goal:** Learn how to connect related data using matching indexes.

Use these two lists:

```python
items = ["Laptop", "Mouse", "Keyboard"]
costs = [1200.00, 25.50, 45.00]
```

The item at index `0` matches the cost at index `0`.

```python
print(items[0], costs[0])
print(items[1], costs[1])
print(items[2], costs[2])
```

Now process both lists with a `while` loop:

```python
i = 0

while i < len(items):
    print(f"Item: {items[i]} | Price: ${costs[i]}")
    i = i + 1
```

**Practice Task:**

Create two parallel lists:

```python
students = ["Amy", "Bob", "Carlos"]
scores = [100, 72, 89]
```

Then print:

```text
Amy scored 100
Bob scored 72
Carlos scored 89
```

Solution pattern:

```python
students = ["Amy", "Bob", "Carlos"]
scores = [100, 72, 89]

i = 0

while i < len(students):
    print(f"{students[i]} scored {scores[i]}")
    i = i + 1
```

---

### Step 8: Watch for Common Mistakes

Here are the most common errors beginners make with lists.

#### Mistake 1: Forgetting that indexes start at 0

Incorrect assumption:

```python
fruits[1]
```

This gives the second item, not the first.

Correct:

```python
fruits[0]
```

---

#### Mistake 2: Going past the end of the list

If a list has 3 items, the valid indexes are:

```python
0, 1, 2
```

This causes an error:

```python
fruits[3]
```

---

#### Mistake 3: Forgetting to increment `i`

This creates an infinite loop:

```python
i = 0

while i < len(items):
    print(items[i])
```

Correct version:

```python
i = 0

while i < len(items):
    print(items[i])
    i = i + 1
```

#### Mistake 4: Parallel lists with different lengths

This can cause problems:

```python
students = ["Amy", "Bob", "Carlos"]
scores = [100, 72]
```

There are three students but only two scores.

Make sure related parallel lists stay the same length.

---


## Final Mastery Checklist

You are ready to move on when you can confidently do these things:

- [ ] Create a list using square brackets.
- [ ] Access an item using an index.
- [ ] Explain why Python starts counting at `0`.
- [ ] Add items using `.append()`.
- [ ] Use `len()`, `sum()`, `max()`, and `min()`.
- [ ] Use a `while` loop to process every item in a list.
- [ ] Use parallel lists to connect related data.
- [ ] Build a program that collects and analyzes user-entered list data. (See Chapel, Movie, and Student Score examples)
- [ ] Avoid common index errors.
- [ ] Explain what a sentinel value does.

---

-- end --
