#Compute the prime numbers up to 100

prim = []
for i in range(2, 101):
    c = 0
    for j in range(1, i):
        if i % j == 0:
            c += 1
    if c == 1:
        prim.append(i)
print(prim)
print('\n')

#Counts the number of letters in a text.

s = input('adj meg egy szöveget')
lista = [0] * 26
for i in range(len(s)):
    if s[i] == ' ' or s[i] == '.' or s[i] == '?' or s[i] == '!' or s[i] == ',':
        continue
    lista[ord(s[i])-97] +=1
for i in range(len(lista)):
    print(f'{chr(i+97)}: {lista[i]}')
print('\n')

#Compute the square numbers up to 100

n = []
for i in range (1, 101):
    counter = 0
    for j in range(1, i+1):
        if i % j == 0:
            counter += 1
    if counter % 2 != 0:
        n.append(i)
print(n)
print('\n')