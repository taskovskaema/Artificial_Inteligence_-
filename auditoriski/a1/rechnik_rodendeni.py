"""
Задача 3 - Речник со родендени
Во оваа задача се чуваат родендените на пријатели, кои треба да се пронајдат
според имињата на пријателите. Креирајте речник (dictionary) со имиња и
родендени. Потоа, додадете функционалност со која од стандарден влез се
чита име на пријател, и вратете го неговиот роденден (односно испечатете го
на стандарден излез). Интеракцијата на програмата треба да изгледа како:
"""

rodendeni = {
    "Ana": "31/10/2004",
    "Marija": "6/2/2003",
    "Stefan": "7/12/2002",
    "Aleksandar": "20/1/2007"
}

if __name__ == '__main__':
    print("Dobredojdovte do rechnikot za rodendeni. Nie gi znaeme rodendenite na: Ana Marija Stefan Aleksandar ")

    print("Koj rodenden e potrebno da se prebara?")
    
    ime = input()

    print("Rodendenot na " + ime + " e na " + rodendeni.get(ime))
