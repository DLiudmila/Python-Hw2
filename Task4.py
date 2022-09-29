# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint

print('Ведите число элементов: ')
N = int(input())
numbers = []
for i in range(N):
    numbers.append(randint(-N, N))
print(numbers)  
multi = None
file = open("file.txt", "r")
lines = file.readlines()

for pos in lines:
    if multi == None:
        multi = numbers[int(pos)]
    else:
        multi = multi * numbers[int(pos)]
print(multi)
file.close
