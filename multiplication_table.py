# Task 5
def multiplication_table():
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for count in range(len(num_list)):
        for num in num_list:
            print(f"{(count + 1) * num} ", end='')
        print()

multiplication_table()