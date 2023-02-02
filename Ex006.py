'''Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
расплачивались за проезд и получали билет с номером. Счастливым
билетом называют такой билет с шестизначным номером, где сумма
первых трех цифр равна сумме последних трех. Т.е. билет с номером
385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
программу, которая проверяет счастливость билета.'''

from random import randint
number = randint(100000, 999999)
print(number)
sum_1, sum_2 = 0, 0
for _ in range(3):
    sum_1 = sum_1 + number % 10
    number = number // 10
for _ in range(3):
    sum_2 = sum_2 + number % 10
    number = number // 10    
if sum_1 == sum_2:
    print('билет счастливый')
else:
    print('билет НЕ счастливый')