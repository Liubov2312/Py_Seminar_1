'''Задача 8: Требуется определить, можно ли от шоколадки размером 
n x m долек отломить k долек, если разрешается сделать один разлом по
прямой между дольками (то есть разломить шоколадку на два
прямоугольника).'''

'''from random import randint
m = randint(1, 10)
n = randint(1, 10)
k = randint(1, 10)'''

print('введите 3 числa')
m = int(input()) #количество долек по длине шоколадки
n = int(input()) #количество долек по ширине шоколадки
k = int(input()) #количество отломленных долек
if k % m == 0 or k % n == 0:
    print('yes')
else:
    print('no')