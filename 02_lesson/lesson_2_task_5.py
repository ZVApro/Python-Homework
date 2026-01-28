def month_to_season(m):
    if m in [1,2,12]:
        return "Зима"
    if m in [3,4,5]:
        return "Весна"
    if m in [6,7,8]:
        return "Лето"
    if m in [9,10,11]:
        return "Осень"
    else:
        return "Нет такого месяца в году"
m = int(input("Введите месяц от 1 до 12: "))
season=month_to_season(m)
print (season)






