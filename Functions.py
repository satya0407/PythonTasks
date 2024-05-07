#Returns the factorial of n

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

#Returns the 

def fibonacci(n):
    if n < 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(7))

nums = []
def devide(n):
    if n / 10 < 1:
        nums.append(int(n))
        return nums
    else:
        nums.append(int(n%10))
        return devide((n-(n%10))/10)
print(devide(9107638))

lista = []
n = int(input('Adj meg a lista hosszát!'))
for i in range(n):
    x = int(input('Adj meg egy számot!'))
    lista.append(x)

def switch(n, l, r):
    if r-l < 1:
        print(lista)
    else:
        x = lista[l]
        y = lista[r]
        lista[l] = y
        lista[r] = x
        switch(n, l+1, r-1)

switch(n, 0, n-1)