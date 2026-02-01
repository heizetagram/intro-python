# Task 8
def search_file():
    
    file_object = open('textfile.txt', 'r')

    search_criteria = input("Input keyword: ").lower()
    print(f"\nSearched word was: {search_criteria}")

    line_num = 1

    for line in file_object:
        if not line.lower().find(search_criteria):
            print(f"Line {line_num}: {line}", end='')
        line_num += 1

    file_object.close()

search_file()