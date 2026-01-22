#CYBR 304
#Homework 1.1
#Zoey Van Dyke

def main():
    #creating matrix 1 & printing
    matrix1 = get_matrix()
    print("Matrix 1: \n\t" + str(matrix1))

    #creating matrix 2 & printing
    matrix2 = get_matrix()
    print("Matrix 2: \n\t" + str(matrix2))

    #if the matrices are equal, add them and print the result
    if len(matrix1) == len(matrix2):
        matrix3 = add_matrix(matrix1, matrix2)
        print("Added Matrices: \n\t" + str(matrix3))
    #if the matrices aren't equal, they can't be added 
    else:
        print("Matrices must be the same size!")


def get_matrix():
    matrix = []
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
    #for every row, create a list to hold columns
    for r in range(rows):
        row = []
        #for every column, input values
        for c in range(columns):
            ui = int(input("\tEnter values for " + str(r) + " " + str(c) + ": "))
            row.append(ui)
        matrix.append(row)
        #append values to row, then the matrix itself
    return matrix


def add_matrix(matrix1, matrix2):
    #creating a blank matrix to hold added matrix
    new_matrix = []
    for r in range(len(matrix1)):
        #for each row create a list to hold columns
        row = []
        for c in range(len(matrix1[r])):
            #for each column, append added values
            row.append(int(matrix1[r][c]) + int(matrix2[r][c]))
        new_matrix.append(row)
    return new_matrix


if __name__ == '__main__':
    main()