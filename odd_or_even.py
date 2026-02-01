# Task 7
def odd_or_even():
    num = int(input('Enter number: '))

    result = "even" if (num % 2 == 0) else "odd"
    print(f"The number {num} is {result}.")
    
odd_or_even()