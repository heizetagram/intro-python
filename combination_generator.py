# Task 6
def combination_generator():
    letter_list = ['a', 'b', 'c']

    for x in letter_list:
        for y in letter_list:
            for z in letter_list:
                print(x + y + z, end=' ')
        print()

combination_generator()