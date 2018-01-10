import random

#wersja 1

imie = ["Ala", "Ola", "Katarzyna", "Magdalena", "Anna", "Mirosław", "Wojciech"]
nazwisko = ["Nowak", "Wojtuń", "Kowal", "Gil", "Sikor", "Smith", "Jezioro"]

wybor_imie = random.choice(imie)
wybor_nazwisko = random.choice(nazwisko)

print('The winner is:',wybor_imie,'',wybor_nazwisko,'!!')


#wersja 2

imie_Pani = ['Ala', 'Ola', 'Katarzyna', 'Magdalena', 'Anna','Jan', 'Piotr', 'Grzegorz', 'Paweł','Mirosław', 'Wojciech']
imie_Pan = ['Jan', 'Piotr', 'Grzegorz', 'Paweł','Mirosław', 'Wojciech']
nazwisko_Pan = ['Nowak', 'Wojtuń', 'Kowal', 'Gil', 'Sikor', 'Smith', 'Jezioro']
nazwisko_Pani = ['Kwiatkowska', 'Wiśniewska','Kowalska','Jankowska']


wybor_imie_Pani = random.choice(imie_Pani)
wybor_imie_Pan = random.choice(imie_Pan)
wybor_nazwisko_Pan = random.choice(nazwisko_Pan)
wybor_nazwisko_Pani = random.choice(nazwisko_Pani)
