# Task 4
def find_the_highest():
    a, b, c = 1, 2, 3

    max = 0

    if a > b and a > c:
        max = a
    elif b > a and b > c:
        max = b
    elif c > a and c > b:
        max = c

    print(max)

find_the_highest()