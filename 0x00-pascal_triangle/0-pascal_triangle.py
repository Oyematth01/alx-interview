#!/usr/bin/python3
"""
Generating a Pascal's Triangle.

This is a function `pascal_triangle(n)` that generates
the first `n` rows of Pascal's Triangle and prints each row.
"""

def pascal_triangle(n):
    """
    This generates and prints Pascal's Triangle up to the nth row.

    Pascal's Triangle is a triangular array of binomial coefficients.
    Each number in the triangle is the sum of the two numbers directly above it.
    The formula for Pascal's triangle is: nCm = n-1Cm-1 + n-1Cm

    Args:
        n (int): The number of rows of Pascal's Triangle to generate. This is an integer greater than 0.

    Returns:
        None: This function prints each row of Pascal's Triangle.
    """
    
    if n <= 0:
        return []
    
    if n == 1:
        return [[1]]

    list_cont = []
    for i in range(n):
        temp_list = []
        for j in range(i + 1):
            if j == 0 or j == i:
                temp_list.append(1)
            else:
                temp_list.append(list_cont[i - 1][j - 1] + list_cont[i - 1][j])
        list_cont.append(temp_list)
    
    # Print each row of Pascal's Triangle
    for row in list_cont:
        print(row)


# Running the function to generate and print Pascal's Triangle
if __name__ == "__main__":
    try:
        n = int(input("Enter the number of rows for Pascal's Triangle: "))
        pascal_triangle(n)
