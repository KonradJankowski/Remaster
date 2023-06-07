# Zadanie nr 1
# W ciągu 3 godzin biegu biegacz pokonał 38 kilometrów. Wyznacz średnią prędkość korzystając ze zmiennych.

t = 3
distanse = 38
av_speed = int(distanse / t)
print(f"Srednia prędkośc to {av_speed} km\h")
#
#
# Zadanie nr 2
# Zakładając, że na lokatę wpłacono 1000 zł, a oprocentowanie wynosi 4% w skali roku, oblicz jaka będzie wartość lokaty po 5 latach.
#

wartosc_pocz = 1000
procent = 4.0
liczba_lat =5

wartosc = wartosc_pocz * (1 + procent / 100) ** liczba_lat


print(f"Po {liczba_lat} latach na lokacie będzie {wartosc} zł ")
#
# Zadanie nr 3
# Oblicz jaką drogę pokonasz idąc do sklepu po czerwonych liniach i wypisz tyle myślników (-) jaki będzie wynik.

a = 9
b = 12
c = ( a ** 2 + b ** 2) ** 0.5
print(f" długość drogi to {2 * c}" )
print(2*int(c)*"-")
