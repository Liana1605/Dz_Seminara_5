#Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
#Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def sum(a, b):
    if b == 0:
        return(a)
    return sum(a + 1, b - 1) 
num_a = int(input("Введите целое число a: "))
num_b = int(input("Введите целое число b: "))
print(sum(num_a, num_b))
