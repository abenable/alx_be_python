# pattern_drawing.py

# Prompt user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Draw the pattern using a while loop for rows and a for loop for columns
while row < size:
    for _ in range(size):
        print("*", end="")
    print()  # Move to the next line
    row += 1
