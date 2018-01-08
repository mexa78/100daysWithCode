import random

imie = ["Ala", "Ola", "Katarzyna", "Magdalena", "Anna", "Mirosław", "Wojciech"]
nazwisko = ["Nowak", "Wojtuń", "Kowal", "Gil", "Sikor", "Smith", "Jezioro"]

wybor_imie = random.choice(imie)
wybor_nazwisko = random.choice(nazwisko)

print('The winner is ',wybor_imie,'', wybor_nazwisko)
