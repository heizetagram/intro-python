# Task 1
def future_age():
    age = int(input("What age will you have reached this year? "))

    age_diff = 100 - age

    current_year = 2026

    future_age, future_year = (age + 100), (current_year + age_diff)

    print(f"In 100 years you will be {future_age}\n...and the year will be {future_year} when you've reached 100")

future_age()