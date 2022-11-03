# zad1a
print('zad1')
napis="ala ma kotA"
print(napis+'\n')

# zad1b
x = 1
if x < 100:
    print("pierwszy warunek\nzostał spełniony")
else:
    print("drugi warunek\nzostał spełniony")
# zad1c
print('\n')
x = 1
y = 3
if x < 100:
    print("został spełniony")
    if y % 3 == 0:
        print("pierwszy i drugi warunek")
    else:
        print("tylko pierwszy warunek")
else:
    print("pierwszy warunek\nnie został spełniony")

#zad2

print("\nZad2")
print("Hello World!")

#Zad3
print("\nzad3 ")

print("    Kotek")
print("Miauczy kotek: miau!\n- Coś ty, kotku, miał?\nMiałem ja miseczkę mleczka,\nTeraz pusta jest miseczka,\nA jeszcze bym chciał.\n")
print("Wzdycha kotek: o!\n- Co ci, kotku, co?\n- Śniła mi się wielka rzeka,\nWielka rzeka, pełna mleka\n Aż po samo dno.\n")
print("Pisnął kotek: pii...\n- Pij, koteczku, pij!\nSkulił ogon, zmrużył ślipie,\nŚpi - i we śnie mleczko chlipie,\nBo znów mu się śni.")

#Zad4
print("\nZad4")
x = 5
y = 8
if x == y:
    print("TAK")
else:
    print("NIE")

#Zad5

print("\nZad5")
x = 6
if x % 2 == 0:
    print("Tak")
else:
    print("Nie")
#Zad6
print("\nZad6")

x = 7
y = 7

if x == y:
    print("liczby są równe")
elif x > y :
    print(x)
else:
    print(y)

#Zad7
print("\nZad6")

x = 7
y = 9
z = 7

if x == y == z :
    print(x)
elif x >= y and x >= z :
    print(x)
elif y >= x and y >= z :
    print(y)
elif z >= x and z >= y :
    print(z)

#Zad8
print("\nZad8")

a=1
b=1
c=19

if a != b and a != c and c != b:
    if a < b and a < c :
        if b > c:
            print(a, c, b)
        else:
            print(a,b,c)

    elif b < a and b < c:
        if a > c:
            print(b,c,a)
        else:
            print(b,a,c)

    elif c < a and c < b:
        if a > b:
            print(c, b, a)
        else:
            print(c,a,b)

else:
    if a == b == c:
        print(a,"=",b,"=",c)
    elif a == b:
        if a > c:
            print(c, "<", a,"=",b)
        else:
            print( a, "=" , b , "<",c)
    elif a == c :
        if a > b :
            print(b,"<",c,"=",a)
        else :
            print(c,"=",a,"<",b)
    elif c == b:
        if c > a:
            print(a,"<",c,"=",b)
        else:
            print(c,"=",b,"<",a)

# Zad9
print("\nZad9")

a=7
b=-6
miejsce_zerowe=0

if a == 0 and b != 0 :
    print("Brak miejsc zerowych")
elif a == 0 and b == 0 :
    print("nieskończenie wiele miejsc zerowych")
else:
    miejsce_zerowe = -b/a
    print(miejsce_zerowe)

# Zad10
print("\nZad10")

a=1
b=5
c=6

if a == 0:
    if  b == 0  :
        if c==0 :
            print("Funkcja ma nieskończenie wiele miejsc zerowych")
        else :
            print("Brak rozwiazan")
    else :
        x=-c/b
        print(x)

else :
    delta = b ** 2 - 4 * a * c
    if delta == 0 :
        x1 = -b / 2 * a
        print(x)
    elif delta < 0 :
        print("Brak miejsc zerowych")
    else:
        x1 = ( -b - delta ** (1 / 2) ) /2 * a
        x2 = ( -b + delta ** (1 / 2) ) / 2 * a
        print(x1,x2)

# Zad11

print("\nZad11")
x = 403
print(x % 10)
x = x //10
print(x % 10)
x = x // 10
print(x % 10)














































