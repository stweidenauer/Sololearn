def enter_matrix():
    row_counter = 0
    matrix = []
    row = []
    while True:
        element = input("Enter Elements of " + str(row_counter + 1) + ". row")
        if element == "":
            matrix.append(row)
            row_counter += 1
            row = []
            continue
        if element == "exit":
            matrix.append(row)
            break
        row.append(element)
    return matrix


def check_complete(in_matrix):
    cc = True
    for li in in_matrix:
        if len(li) != len(in_matrix[0]):
            return False
            break
    return cc


def check_lines(in_matrix):
    a = 0
    b = len(in_matrix[0]) - 1
    for l in in_matrix:
        if a == b or a > b:
            break
        if l[a] != l[b]:
            return False
    return True


def rotate_matrix(in_matrix):
    help_matrix = []
    for j in range(len(in_matrix[0])):
        helpline = []
        for i in range(len(in_matrix) - 1, -1, -1):
            helpline.append(in_matrix[i][j])
        help_matrix.append(helpline)
    return help_matrix


mat = enter_matrix()
if check_complete(mat):
    if check_lines(mat) and check_lines(rotate_matrix(mat)):
        print('It is a Owl_Matrix')
    else:
        print('It is not a Owl_Matrix')
else:
    print("Not all rows have the same length, so no matrix entered")
