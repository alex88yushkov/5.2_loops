xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]

# Write a loop that prints each of the numbers on a new line.
for new_line in xs:
    print(new_line)

# Write a loop that prints each number and its square on a new line.
for square in xs:
    a = square ** 2
    print(square, "raised to the 2nd power is", a)

# Write a loop that adds all the numbers from the list into a variable called total.
# You should set the total variable to have the value 0 before you start adding them up,
# and print the value in total after the loop has completed.
sum = 0
for total in xs:
    sum += total
print("Sum of the list is", sum)

# Print the product of all the numbers in the list. (product means all multiplied together)
mul = 1
for prod in xs:
    mul *= prod
print("Product of the list is", mul)


