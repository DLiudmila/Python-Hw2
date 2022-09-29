# Задайте список из n чисел последовательности (1+ 1/n)^n 
# и выведите на экран их сумму (округляйте до 3 знаков после запятой).
# Пример: Для n = 6: [2, 2.25, 2.37, 2.441, 2.488, 2.522]
# Вывод: 14.031 (2 + 2.25 + 2.37 + 2.441 + 2.448 + 2.522)


from asyncore import write


print('Введите n: ')
n = int(input())
list = [0]*n
for i in range(1, n+1):
    list[i-1] = round(((1 + (1 / i)) ** i), 3)
    i = i + 1
sum = 0
for j in list:
    sum = sum + j
print(sum, '(', end=''),
print(' + '.join(map(str, list)), end='')
print(')')
    