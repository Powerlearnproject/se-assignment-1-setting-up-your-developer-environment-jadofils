# Function to find the maximum of three numbers using ternary operator
def max_of_three(a, b, c):
    max_num = a if (a > b and a > c) else (b if b > c else c)
    return max_num

# Example usage
a = 9
b = 6
c = 15

print("The maximum number is:", max_of_three(a, b, c))
