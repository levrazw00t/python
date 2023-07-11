
# coding: utf-8

# In[1]:

# Считать отдельными операторами целочисленные ширину и высоту прямоугольника. Создать функцию (def), 
# принимающую в качестве параметров ширину и высоту фигуры и название функции, которую необходимо выполнить. 
# Имя вложенной функции передавать явным образом (например: (a,b,name='perim')).
# Внутри функции создать две вложенные функции (def) по подсчету площади и периметра фигуры. 
# Вывести одной строкой через пробел площадь и периметр, разделенные пробелом (например, '20 18').

x=int(input())
y=int(input())

def f(x,y):
    def area(x,y):
        return x*y
    def perimeter(x,y):
        return (x+y)*2
    print (area(x,y), perimeter(x,y))
    
f(x,y)


# In[2]:

#Считать отдельными операторами целочисленные ширину и высоту прямоугольника, создать функцию (def), 
#принимающую в качестве параметров ширину и высоту фигуры.
#Внутри функции создать две вложенные функции (lambda) по подсчету площади и периметра фигуры. 
#Вывести одной строкой через пробел площадь и периметр, разделенные пробелом (например '20 18').

x=int(input())
y=int(input())

def f(x,y):
    area=lambda x,y: x*y
    perimeter=lambda x,y: (x+y)*2
    print (area(x,y), perimeter(x,y)
           
f(x,y)           


#ln[3]:

#Считать отдельными операторами целочисленные ширину и высоту прямоугольника, 
#создать список из лямбда функций подсчета площади и периметра фигуры.
#Вывести первым оператором индекс лямбда функции подсчета площади и ее результат (например:0 20);
#вторым оператором индекс лямбда функции подсчета периметра и ее результат (например:1 18);
#вывести третьим оператором список полученным значений (например: [20, 18]);
#вывести четвертым оператором итоговые значения, сведенные в одну строк через пробел (например: '20 18').

           
x=int(input())
y=int(input())

area = (lambda x, y: x * y)
perimeter = (lambda x, y: (x + y) * 2)

alist = [area, perimeter]

def f(x, y, *args):
    for i, arg in enumerate(args):
        print(i, arg(x, y))

f(x, y, *alist)

def f1(*args):
    return area(x, y), perimeter(x, y)

c = list(f1(alist, x, y))
print(c)

print(alist[0](x, y), alist[1](x, y))





