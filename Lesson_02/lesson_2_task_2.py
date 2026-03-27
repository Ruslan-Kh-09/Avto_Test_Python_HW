def is_year_leap(year):

    return "Этот год високосный" if year % 4 == 0 else "Этот год не високосный"


num = int(input("Введите год: "))
result = is_year_leap(num)
print(f"{num} год  - {result}")
