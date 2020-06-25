# Course: CS261 - Data Structures
# Student Name: Joel Chenoweth
# Assignment: 1 Adding Matrices
# Description: A Matrix is values within ordered rows and columns.  This function adds them together.


def matrix_add(x,y) -> [[]]:
    """
    This function takes in two lists as arguments.  It iterates through the rows and columns on the return and
    adds them to output one matrix of combined data.  It assumes the rows and columns are the same length or returns none.
    """
    X = x

    Y = y

    if len(X) == len(Y) and len(X[0]) == len(Y[0]):
        return [[X[a][b] + Y[a][b] for b in range(len(X[0]))]
                  for a in range(len(X))]





# BASIC TESTING
#if __name__ == "__main__":
    # example 1
 #   m1 = [[1, 2, 3], [2, 3, 4]]
  #  m2 = [[5, 6, 7], [8, 9, 10]]
   # m3 = [[1, 2], [3, 4], [5, 6]]

    #print(matrix_add(m1, m2))
    #print(matrix_add(m1, m3))
    #print(matrix_add(m1, m1))
    #print(matrix_add([[]], [[]]))
    #print(matrix_add([[]], m1))