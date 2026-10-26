# CS 111 – In-Class Python Practice: Decisions and Loops

## Sample Solutions

## Problem 1: Movie Ticket Prices (if Statements)

**Python code:**

```python
age = int(input("Enter customer age: "))
price = 0

# Children under 12
if age < 12:
    price = 6

# Customers ages 12 through 64
if age >= 12 and age <= 64:
    price = 12

# Seniors 65 and older
if age >= 65:
    price = 8

print(f"Ticket Price: ${price}")
```

**Sample run:**

```text
Enter customer age: 70
Ticket Price: $8
```

**Explanation:** The program reads the customer's age, checks three non-overlapping age ranges with separate `if` statements, and prints the price. Each `if` is evaluated independently, but only one condition is true for a valid age.

## Problem 2: Counting by Threes (while Count Loop)

**Python code:**

```python
count = 3

while count <= 30:
    print(count)
    count = count + 3
```

**Expected output:**

```text
3
6
9
12
15
18
21
24
27
30
```

**Explanation:** The counter starts at 3. Each iteration prints its value and increases it by 3. The loop stops after printing 30, when the counter becomes 33.

## Problem 3: Counting Customer Orders (Sentinel Loop)

**Python code:**

```python
total_items = 0
order_count = 0

items = int(input("Enter items in order (-1 to quit): "))

while items != -1:
    total_items = total_items + items
    order_count = order_count + 1

    items = int(input("Enter items in order (-1 to quit): "))

print()
print(f"Number of Orders: {order_count}")
print(f"Total Items: {total_items}")
```

**Sample run #1:**

```text
Enter items in order (-1 to quit): 3
Enter items in order (-1 to quit): 5
Enter items in order (-1 to quit): 2
Enter items in order (-1 to quit): -1

Number of Orders: 3
Total Items: 10
```

**Sample run #2:**

```text
Enter items in order (-1 to quit): -1

Number of Orders: 0
Total Items: 0
```

**Explanation:** The program reads an order before entering the loop. Every value other than `-1` contributes to the item total and increments the order count, including an order with zero items. Entering `-1` ends the loop without counting or adding the sentinel.

## Summary of Programming Concepts

| Problem | Programming Structure | Important Concept |
|---|---|---|
| 1. Movie Ticket Prices | Three independent `if` statements | Choose a price based on conditions |
| 2. Counting by Threes | Count-controlled `while` loop | Update a counter until its stopping condition is reached |
| 3. Counting Customer Orders | Sentinel-controlled `while` loop | Stop on a special value without processing it |

## Suggested Test Cases

| Problem | Input | Expected Result |
|---|---|---|
| 1 | Age 8 | $6 |
| 1 | Age 12 | $12 |
| 1 | Age 64 | $12 |
| 1 | Age 65 | $8 |
| 2 | No input | 3, 6, 9, …, 30 on separate lines |
| 3 | 3, 5, 2, -1 | 3 orders, 10 items |
| 3 | 0, 4, -1 | 2 orders, 4 items |
| 3 | -1 | 0 orders, 0 items |

**Reminders:** Indentation identifies the code inside `if` statements and loops. In a `while` loop, make sure some value changes so the loop can eventually stop. Never include the sentinel in the totals.
