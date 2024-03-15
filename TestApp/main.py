# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np

def print_hi(name):
    for i in name:
        print(f'{i}')


def print_odd_number(x, y):
    for i in range(x, y+1):
        if i % 2 != 0:
            print(i)


def sum_num_range(x, y):
    sum = 0
    for i in range(x, y+1):
        sum += i
    print('Sum all number from '+f'{x} to '+f'{y} = '+ f'{sum}')

def print_dict():
    mydict = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4
    }
    print('All key: ')
    for i in mydict.keys():
        print(i)
    print('All value: ')
    for i in mydict.values():
        print(i)

    for i in mydict.items():
        print(i)


def print_tuples(a, b):
    for i in range(len(a)):
        for j in range(len(b)):
            if i == j:
                print(f'{a[i]} : {b[j]}')

def find_consonants(str):
    vowel = ['u', 'e', 'o', 'a', 'i']
    count = 0
    for i in str:
        for j in vowel:
            if i == j:
                break

    print(count)


def print_result(a, b):
    x = 0
    for i in range(a, b):
        try:
            x = 10 / i
            print(x)
        except ZeroDivisionError:
            print('Can\'t devide by zero.')

def merge(l1, l2):
    return [(l1[i], l2[i]) for i in range(0, len(l1))]


def print_soft_megre(l1, l2):
    ml = merge(l1, l2)
    print(sorted(ml, key=lambda i: (i[1])))




def read_file(str):
    f = open(str, "r")
    for x in f:
        print(x)


def sum_2_num(a, b):
    return a+b


def create_matrix():
    matrix = np.array([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]])
    return matrix
# Press the green button in the gutter to run the script.

def create_vector():
    vector = np.array([1, 2, 3])
    return vector

def check_rank_matrix():
    m = create_matrix()
    m_rank = np.linalg.matrix_rank(m)
    print("Rank of matrix: " + f'{m_rank}')

def check_rank_vector():
    v = create_vector()
    v_rank = np.linalg.matrix_rank(v)
    print("Rank of vector: " + f'{v_rank}')


def check_shape_matrix():
    m = create_matrix()
    print("Shape of matrix: " + f'{m.shape}')

def check_shape_vector():
    v = create_vector()
    print("Shape of vector: " + f'{v.shape}')


def matrix_plus(n):
    m = create_matrix()
    print("New matrix:\n " + f'{m+n}')


def matrix_transpose():
    m = create_matrix()
    return np.transpose(m)

def vector_transpose():
    v = create_vector()
    return np.transpose(v)

def norm_vector():
    v = np.array([2, 7])
    print(v)
    norm = np.linalg.norm(v)
    print("Norm of vector: " + f'{norm}')
    print("Normalized = " + f'{v/norm}')


def plus_minus():
    a = np.array([10,15])
    b = np.array([8,2])
    c = np.array([1,2,3])
    print(f'a = {a}\nb = {b}\nc = {c}')
    print(f'a + b = {a+b}')
    print(f'a - b = {a-b}')
    print(f'a - c: error dimensions of a and c are different. ')

def dot_product():
    a = np.array([10, 15])
    b = np.array([8, 2])
    dot = np.dot(a,b)
    print(f'Dot product: {dot}')


def ex_8():
    # a
    A = np.array([[2, 4, 9],
                  [3, 6, 7]])
    print("a/")
    print(A)
    print("Rank of matrix A:", np.linalg.matrix_rank(A))
    print("Shape of matrix A:", A.shape)

    # b
    value_7 = A[1, 2]
    print("Value 7 in matrix A:", value_7)

    # c
    second_column_A = A[:, 1]
    print("Second column of matrix A:", second_column_A)


def create_rand_matrix():
    return np.random.randint(-10, 10, size=(3, 3))


def create_id_rand_matrix():
    print(f'Id matrix: {np.eye(3)}')


def ex_11():
    # a
    m = np.random.randint(1, 10, size=(3, 3))
    print("W1: ", np.trace(m))
    # b
    m2 = 0
    for i in range(3):
        m2 += m[i, i]
    print("W2: ", m2)


if __name__ == '__main__':
    # print_hi('Mai Trần Nhật Tuấn')
    # print_odd_number(1, 10)
    # sum_num_range(1, 6)
    # print_dict()
    # courses = [131, 141, 142, 212]
    # name = ["Maths", "Physics", "Chem", "Bio"]
    # print_tuples(courses, name)

    # find_consonants('abc')
    # print_result(-2, 3)
    # name = ['Hoa', 'Lam', 'Nam']
    # age = [23, 10, 80]
    # print_soft_megre(name, age)

    # read_file("Tuan.txt")

    # print(sum_2_num(3,4))

    # check_rank_matrix()
    # check_rank_vector()
    # check_shape_matrix()
    # check_shape_vector()
    #
    # matrix_plus(3)
    # print(matrix_transpose())
    # print(vector_transpose())

    # norm_vector()
    # plus_minus()
    # dot_product()
    ex_8()
