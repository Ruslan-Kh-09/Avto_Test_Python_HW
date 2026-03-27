def month_to_season(month):

    if 3 <= month <= 5:
        return "Весна"
    if 6 <= month <= 8:
        return "Лето"
    if 9 <= month <= 11:
        return "Осень"
    if month == 12 or month <= 2:
        return "Зима"
    else:
        return "Неверный номер месяца"


month = int(input("Введите номер месяца (1-12): "))
print(month_to_season(month))

