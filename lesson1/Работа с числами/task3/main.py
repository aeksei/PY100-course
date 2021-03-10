DAYS_OF_YEAR = 365

start_year = int(input("Год рождения: "))
current_year = int(input("Такущий год: "))

days = (current_year - start_year) * DAYS_OF_YEAR
print(days)
