def is_year_leap (year):
    return year % 4 ==0
input_year = int(input("Введите год: "))
result = is_year_leap(input_year)
print(f'год {input_year}: {result}')