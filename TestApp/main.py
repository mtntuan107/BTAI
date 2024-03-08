# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


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


# def check_rank_matrix(matrix):


# Press the green button in the gutter to run the script.

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

    read_file("Tuan.txt")

    # print(sum_2_num(3,4))