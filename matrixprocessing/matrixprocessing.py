def read_matrix(name=""):
    prompt_size = f"Enter size of {name} matrix: " if name else "Enter matrix size: "
    dimensions = input(prompt_size).split()
    if not dimensions:
        return [], 0, 0
    n, m = int(dimensions[0]), int(dimensions[1])

    prompt_matrix = f"Enter {name} matrix:\n" if name else "Enter matrix:\n"
    print(prompt_matrix, end="")

    matrix = []
    for _ in range(n):
        row = list(map(float, input().split()))
        matrix.append(row)
    return matrix, n, m


def print_result(matrix):
    print("The result is:")
    for row in matrix:
        formatted_row = []
        for x in row:
            # Избавляемся от -0.0
            x = 0 if abs(x) < 1e-10 else x
            if x.is_integer():
                formatted_row.append(str(int(x)))
            else:
                formatted_row.append(str(round(x, 2)))
        print(" ".join(formatted_row))
    print()


def add_matrices():
    matrix_a, n_a, m_a = read_matrix("first")
    matrix_b, n_b, m_b = read_matrix("second")
    if n_a != n_b or m_a != m_b:
        print("The operation cannot be performed.\n")
        return
    result = [[matrix_a[i][j] + matrix_b[i][j] for j in range(m_a)] for i in range(n_a)]
    print_result(result)


def multiply_by_constant():
    matrix_a, n_a, m_a = read_matrix()
    constant = float(input("Enter constant: "))
    result = [[matrix_a[i][j] * constant for j in range(m_a)] for i in range(n_a)]
    print_result(result)


def multiply_matrices():
    matrix_a, n_a, m_a = read_matrix("first")
    matrix_b, n_b, m_b = read_matrix("second")
    if m_a != n_b:
        print("The operation cannot be performed.\n")
        return
    result = [[sum(matrix_a[i][k] * matrix_b[k][j] for k in range(m_a)) for j in range(m_b)] for i in range(n_a)]
    print_result(result)


def transpose_matrix():
    print("\n1. Main diagonal")
    print("2. Side diagonal")
    print("3. Vertical line")
    print("4. Horizontal line")
    trans_choice = input("Your choice: ")
    matrix, n, m = read_matrix()
    result = []
    if trans_choice == '1':
        result = [[matrix[j][i] for j in range(n)] for i in range(m)]
    elif trans_choice == '2':
        result = [[matrix[n - 1 - j][m - 1 - i] for j in range(n)] for i in range(m)]
    elif trans_choice == '3':
        result = [[matrix[i][m - 1 - j] for j in range(m)] for i in range(n)]
    elif trans_choice == '4':
        result = [[matrix[n - 1 - i][j] for j in range(m)] for i in range(n)]
    print_result(result)


def get_minor(matrix, i, j):
    return [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]


def get_determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    for c in range(len(matrix)):
        det += ((-1) ** c) * matrix[0][c] * get_determinant(get_minor(matrix, 0, c))
    return det


def calculate_determinant():
    matrix, n, m = read_matrix()
    if n != m:
        print("The operation cannot be performed.\n")
        return
    det = get_determinant(matrix)
    print("The result is:")
    det = 0 if abs(det) < 1e-10 else det
    print(int(det) if det.is_integer() else round(det, 2))
    print()


def inverse_matrix():
    matrix, n, m = read_matrix()
    if n != m:
        print("The operation cannot be performed.\n")
        return
    det = get_determinant(matrix)
    if det == 0:
        print("This matrix doesn't have an inverse.\n")
        return

    if n == 1:
        print_result([[1 / matrix[0][0]]])
        return

    cofactors = []
    for r in range(n):
        cofactor_row = []
        for c in range(n):
            minor = get_minor(matrix, r, c)
            cofactor = ((-1) ** (r + c)) * get_determinant(minor)
            cofactor_row.append(cofactor)
        cofactors.append(cofactor_row)

    adjugate = [[cofactors[c][r] for c in range(n)] for r in range(n)]
    inverse = [[adjugate[r][c] / det for c in range(n)] for r in range(n)]
    print_result(inverse)


while True:
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("4. Transpose matrix")
    print("5. Calculate a determinant")
    print("6. Inverse matrix")
    print("0. Exit")
    choice = input("Your choice: ")

    if choice == '1':
        add_matrices()
    elif choice == '2':
        multiply_by_constant()
    elif choice == '3':
        multiply_matrices()
    elif choice == '4':
        transpose_matrix()
    elif choice == '5':
        calculate_determinant()
    elif choice == '6':
        inverse_matrix()
    elif choice == '0':
        break

