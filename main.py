# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n=(int(input("n= ")))
list1=[]
for i in range(n):
    num = int(input("num= "))
    list1.append(num)
print(list1)

m=(int(input("m= ")))
list2 = []
for i in range(m):
    num = int(input("num= "))
    list2.append(num)
print(list2)

list3 = list1+list2
list = []
for i in list3:
    if list3.count(i) > 1 and i not in list:
        list.append(i)
        print(i)