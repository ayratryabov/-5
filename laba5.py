from timeit import Timer
from tabulate import tabulate

def F_rec(w):
    if w == 1:
        return 1
    elif w == 2:
        return 2
    else:
        return 3*F_rec(w-1) - 2*F_rec(w-2)
    
def F_iter(w):
    if w == 1:
        return 1
    elif w == 2:
        return 2
    else:
        f1 = 1
        f2 = 2
        for i in range(3, w+1):
            f = 3*f2 - 2*f1
            f1 = f2
            f2 = f
        return f2

s = int(input('Введите число,до которого будет проведено исследование: '))
n = int(input('Введите число,которое будет периодом в исследовании: '))
c = int(input('Задайте число выполнений в цикле для функции timeit: '))
tabl = []
    
for i in range(1,s+1,n):
    tabl1 = []
    t_rec = Timer(lambda: F_rec(i))
    t_iter = Timer(lambda: F_iter(i))
    tabl1.append(t_rec.timeit(number=c))
    tabl1.append(t_iter.timeit(number=c))
    print()
    tabl.append(tabl1)
    print('Время выполнения рекурсионной функции:',tabl1[0])
    print('Время выполнения итерационной функции:',tabl1[1])
head = ['Время выполнения рекурсионной функции','Время выполнения итерационной функции']
print()
print()
print(tabulate(tabl, headers=head, tablefmt="grid",))
