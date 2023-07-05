import math

def one():
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a+b+c)/2
    s = (p*(p-a)*(p-b)*(p-c))**(1/2)
    print (s)


def two():
    a = int(input())
    if (a>(-15) and a<=12) or (a>14 and a<17) or (a>=19):
        print(f"True")
    else:
        print(f"False")


def three():
    a = float(input())
    b = float(input())
    c = str(input())
    if c == '+':
        print(a+b)
    elif c == '-':
        print(a-b)
    elif c == '*':
        print(a*b)
    elif c == '/':
        if b == 0:
            print(f"Деление на 0!")
        else:
            print(a/b)
    elif c == 'div':
        if b == 0:
            print(f"Деление на 0!")
        else:
            print(a//b)
    elif c == 'pow':
        print(a**b)
    elif c == 'mod':
        if b == 0:
            print(f"Деление на 0!")
        else:
            print(a%b)


def four():
    d = str(input())
    if d == "треугольник":
        a = int(input())
        b = int(input())
        c = int(input())
        p = (a+b+c)/2
        s = (p*(p-a)*(p-b)*(p-c))**(1/2)
    elif d == 'прямоугольник':
        a = int(input())
        b = int(input())
        s = a*b
    elif d == 'круг':
        r = int(input())
        s = 3.14*r**2
    print(s)


def five():
    a = int(input())
    b = int(input())
    c = int(input())
    if (a>=b and a>=c):
        print(a)
        if(b>=c):
            print(c)
            print(b)
        else:
            print(b)
            print(c)
    elif (b>=a and b>=c):
        print(b)
        if(a>=c):
            print(c)
            print(a)
        else:
            print(a)
            print(c)
    elif (c>=a and c>=b):
        print(c)
        if(a>=b):
            print(b)
            print(a)
        else:
            print(a)
            print(b)


def six():
    n = int(input())
    str_convert = str(n)[-1]
    str_convert2 = str(n)[-2:]
    int_convert = int(str_convert)
    int_convert2 = int(str_convert2)
    if (int_convert == 1) and (int_convert2<10 or int_convert2>14):
        print(f'{n} программист')
    elif (int_convert >= 2 and int_convert <=4) and (int_convert2<10 or int_convert2>14):
        print(f'{n} программиста')
    else:
        print(f"{n} программистов")

def seven():
    a = int(input())
    if (a%10 + a//10%10 + a//100%10 == a//1000%10+a//10000%10+a//100000%10):
        print(f"Счастливый")
    else:
        print(f"Обычный")

def one1():
    n = 0
    s = 0
    a = int(input())
    n = n+a
    s = s+a*a
    while(n!=0):
        a = int(input())
        n = n+a
        s = s+a*a
    print(s)

def two1():
    n = int(input())
    list1 = list()
    for i in range(n):
        j = 0
        while j<i+1:
            list1.append(i+1)
            j+=1
            if len(list1)==n:
                print(*list1)
                break     

def three1():
    ls1 = [int(i) for i in input().split()]
    ls2 = list()
    n = int(input())
    if n not in ls1:
        print('Отсутствует')
    else:
        for i in range(len(ls1)):
            if n == ls1[i]:
                ls2.append(i)
        print(*ls2)

def four1():
    col_len=0
    row_len=1
    md=""
    arr=[]
    a0,b0,an,bn=0,0,0,0
    # формируем матрицу
    while row_len>0: # бесконечный цикл
        md=input().split() # разбиваем строку на элементы для добавления в список
        if "end" in md:
            row_len-=1
            break # если в строке попалось END, закрываем список
        else:
            if row_len==1:
                col_len=len(md)
            row_len+=1 # счетчик
            arr.append(md) # добавляем элементы строки в двухмерный список
    # формируем нулевую матрицу
    arr_sum = [[0 for j in range(col_len)] for i in range(row_len)]

    #определяем в матрице элементы из суммы смежных
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i-1<0: a0=row_len-1
            else: a0=i-1
            if j-1<0: b0=col_len-1
            else: b0=j-1
            if i+1>row_len-1: an=0
            else: an=i+1
            if j+1>col_len-1: bn=0
            else: bn=j+1
            arr_sum[i][j]= int(arr[a0][j])+int(arr[an][j])+int(arr[i][b0])+int(arr[i][bn])
    # выводим новую матрицу на экран
    for row in arr_sum:
        for elem in row:
            print(elem, end=' ')
        print()

def five1():
    a=int(input())
    nul=[[0]*a for i in range(a)]
    x,y=0,0
    for i in range(1,a**2+1):
        nul[x][y]=i
        if x<=y+1 and x+y<a-1: y+=1
        elif x<y: x+=1
        elif x+y>=a : y-=1
        elif x>=y : x-=1
    for i in range(a):
        print(*nul[i])
five1()