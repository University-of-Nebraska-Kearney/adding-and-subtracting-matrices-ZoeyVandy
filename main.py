#CYBR 304
#Homework 1.1
#Zoey Van Dyke

def main():
    matrix1 = get_matrix()
    print("Matrix 1: \n\t" + str(matrix1))

    matrix2 = get_matrix()
    print("Matrix 2: \n\t" + str(matrix2))

    if len(matrix1) == len(matrix2):
        matrix3 = add_matrix(matrix1, matrix2)
        print("Added Matrices: \n\t" + str(matrix3))
    else:
        print("Matrices must be the same size!")


def get_matrix():
    matrix = []
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
    for r in range(rows):
        row = []
        for c in range(columns):
            ui = int(input("\tEnter values for " + str(r) + " " + str(c) + ": "))
            row.append(ui)
        matrix.append(row)
    return matrix


def add_matrix(matrix1, matrix2):
    new_matrix = []
    for r in range(len(matrix1)):
        row = []
        for c in range(len(matrix1[r])):
            row.append(int(matrix1[r][c]) + int(matrix2[r][c]))
        new_matrix.append(row)
    return new_matrix


if __name__ == '__main__':
    main()