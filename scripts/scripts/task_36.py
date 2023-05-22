""" 
Write a function print_operation_table(operation, num_rows=6, num_columns=6) 
that takes as an argument a function that calculates an element by row and column number. 
The num_rows and num_columns arguments specify the number of table rows and columns to be printed. 
The numbering of rows and columns starts from one (think why not from zero). 
Note: A binary operation is any operation that has exactly two arguments, such as multiplication.

*Example:*

**Input:** `print_operation_table(lambda x, y: x + y) `
**Conclusion:**

1 2 3 4 5 6
2 4 6 8 10 12
3 6 9 12 15 18
4 8 12 16 20 24
5 10 15 20 25 30
6 12 18 24 30 36
"""

def print_operation_table(f, num_rows=6, num_columns=6):
    out = []
    for i in range(1, num_columns+1):
        col = []
        for j in range(1, num_rows+1):
            col.append(f(j,i))
        out.append(col)
    return out

print(print_operation_table(lambda x,y: x*y))