number = 123

d_1 = number // 100
d_2 = number % 100 // 10
d_3 = number % 10

print(d_1, d_2, d_3)
list_digit = [d_1, d_2, d_3]

print("Сумма цифр", sum(list_digit))
print("Количество цифр", len(list_digit))
print("Максимальная цифра", max(list_digit))

print(list_digit[0] - list_digit[-1])
print(list_digit.index(min(list_digit)))