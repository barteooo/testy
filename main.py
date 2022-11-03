#Zaad 1

for i in range(15):
    print(i)

print(12*"-")

for i in range(2, 15):
    print(i)

print(12*"-")

for i in range(2, 15, 4):
    print(i)

print(12*"-")

n = 4
print("rozmiar: ",n)

for i in range (1, n+1):
    print( (n-i) * "-", end = "XD")
    print(i * "+")

# Zad 2

print("Zad 2: ")

n = 5
print("rozmiar: ", n)

for i in range (0, n + 1):
    print( (n - i) * "*" )

# Zad 3

print("Zad 3:")
n = 5
print("rozmiar: ", n)
for i in range (1 , n + 1):
    print( " " * (n - i), end = "")
    print("*" * i )

# Zad 4

print("Zad 4:")
n = 5
print("rozmiar: ", n)

for i in range ( n ) :
    print( "*" * (i+1) )

# Zad 5
print("Zad 5:")
n = 5
print("rozmiar: ", n)

for i in range( n ):
    print(" " * i , end="")
    print("*" * (n - i) )


# Zad 6
print("Zad 6:")
n = 6
print("rozmiar: ", n)

for i in range (1, n + 1 ):
    print("* " * i)

# Zad 7
print("Zad 7a:\n")
n = 6
for i in range (1, n + 1):
    print( ( ( n - i)  ) * " ", end="")
    print( i * "* ")

if n % 2 == 0 :
   print ( ( (n // 2) * 2 - 3) * " ", end="|___|\n")

else:
   print(((n // 2) * 2 - 2) * " ", end="|___|\n")


print("Zad 7b:")
n = 5
print("rozmiar: ", n)

for i in range (n):
    print( (n - i - 1) * " ",end ="")
    print( ( i + 1) * "*", end="")
    print( i * "*")

# Zad 8

print("Zad 8:")

silnia = 1
n = 5
for i in range (1 , n + 1 ):
    silnia *= i

print(silnia)

# Zad 9
print("Zad 9:")

n = 3
suma = 0
for i in range ( 1 , n + 1):
    suma += i

print(suma)

# Zad 10
print("Zad 10:")

for i in range(10):
    print(i,":" ,i + (i-1) )

# Zad 11
print("Zad 11:")
suma = 0
for i in range (1, 11):
    suma += i
    print(suma)

# Zad 12 :
print("Zad 12:")
for i in range ( 5 ):
    liczba = (2 ** i)
    print(liczba)
    print(-liczba)

# Zad 13:
print("Zad 13:")

for i in range (2, 801):
    dzielniki = 0
    for j in range (1 , i + 1):
        if(i % j == 0 ):
            dzielniki += 1

    if dzielniki == 2:
        print(i)

# Zad 14
print("Zad 14:")

a = 282
b = 78

while ( a % b != 0 ):
    reszta = a % b
    a = b
    b = reszta

print(b)

# Zad 15
print("Zad 15:")

wysokosc = 5
szerokosc = 6

print(" ", end=" ")
for i in range(1, szerokosc + 1):
    print( i,end=" ")

print("\n")


for i in range (1, wysokosc + 1):

    for j in range (1, szerokosc + 1):
        if j == 1:
           print(i, end=" ")
        print(i * j, end=" ")

    print ("\n")

# Zad 16

liczba = 6

czy_da_sie = 0

for i in range(n + 1):
    for j in range(n // 2 + 1):
        suma = 0
        suma = i**2 + j**2
        if suma == liczba :
            czy_da_sie = 1
            break;

if czy_da_sie == 1:
    print("TAK")
else:
    print("NIE")

# Zad 17

print("Zad 17:")

for i in range (100, 1000):
    if i % 10  > (i // 10) % 10 and ( (i//10) // 10) % 10 < (i // 10) % 10 :
        print(i)









































