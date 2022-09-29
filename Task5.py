# Реализуйте алгоритм перемешивания списка.

from random import randint


print('Ведите число элементов: ')
N = int(input())
numbers_one = []
for i in range(N):
    numbers_one.append(randint(1, N))
print(numbers_one)

for i in range(0, len(numbers_one)):
    x = randint(0, N)
    var = numbers_one[x]
    numbers_one[x] = numbers_one[i]
    numbers_one[i] = var
print(numbers_one)