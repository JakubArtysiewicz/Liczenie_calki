#Liczenie całki
def funkcja(x):
    return x*x+1
def liczenie_calki(a,b,przyblizenie):
    wynik = 0
    x = (b-a)/przyblizenie
    for i in range(przyblizenie):
        y = funkcja(a+i*x)
        wynik += y*x
    return wynik

def liczenie_calki_trapezy(a,b,przyblizenie):
    wynik = 0
    x = (b-a)/przyblizenie
    for i in range(przyblizenie):
        y = funkcja(a+i*x)
        y2 = funkcja(a+(i+1)*x)
        wynik += ((y+y2)/2)*x
    return wynik

print(liczenie_calki(0,4,10000000))
print(liczenie_calki_trapezy(0,4,1000))