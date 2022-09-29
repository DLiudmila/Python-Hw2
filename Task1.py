# Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.
# Пример: 6782 -> 23   0,56 -> 11

print('Ведите число: ')
str_n = input()
i = 0
sum = 0
while i<len(str_n):
    digit=str_n[i]
    if digit.isdigit():
        sum = sum + int(digit)
    i=i+1
print(str_n,'->', sum)