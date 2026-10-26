# CS 111 – In-Class Python Practice: Decisions and Loops

Instructions: Write a Python program for each problem. Use the programming structures specified. Test your programs with different input values.

## Problem 1: Movie Ticket Prices (if Statements)

A movie theater charges different ticket prices based on a customer's age:

- Children under 12 pay $6.
- Customers ages 12 through 64 pay $12.
- Seniors 65 and older pay $8.

Write a Python program that inputs the customer's age and determines the correct ticket price. Use three individual `if` statements, not `elif` or `else`.

Starting code:

```python
age = int(input("Enter customer age: "))
price = 0

# Write your if statements here


print(f"Ticket Price: ${price}")

```
Sample run:

```
Enter customer age: 70
Ticket Price: $8
```

## Problem 2: Counting by Threes (while Count Loop)

Write a Python program that uses a count-controlled `while` loop to display the numbers from 3 to 30, counting by 3's. 

Do not use a `for` loop. 

Display each number on a separate line.

Starting code:

```python
# Write your while loop here


```

Expected output:

```
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

## Problem 3: Counting Customer Orders (Sentinel Loop)

A small store wants to count how many customer orders were processed during the day.

Write a Python program that repeatedly asks the user to enter the number of items in a customer order. Continue accepting orders until the user enters -1.

Use a sentinel-controlled `while` loop to keep a running total of all items ordered and count how many orders were entered. When the sentinel is entered, display the number of orders and the total number of items. Do not include the sentinel value in either total. Assume all valid orders contain zero or more items.

Starting code:

```python

total_items = 0
order_count = 0

# Write your sentinel loop here






print(f"Number of Orders: {order_count}")
print(f"Total Items: {total_items}")
```

Sample run #1:

```
Enter items in order (-1 to quit): 3
Enter items in order (-1 to quit): 5
Enter items in order (-1 to quit): 2
Enter items in order (-1 to quit): -1

Number of Orders: 3
Total Items: 10
```

Sample run #2:

```
Enter items in order (-1 to quit): -1

Number of Orders: 0
Total Items: 0
```

-- end --

