import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"

Students={}

if __name__=='__main__':

    while True:

        users=input()

        if users=='end':
            break

        ime, prezime, brIndeks, predmet, poeniT, poeniP, poeniL=users.split(",")

        vkPoeni=(int(poeniL)+int(poeniP)+int(poeniT))
        ocena=0

        if vkPoeni<=50:
            ocena=5
        elif 50 < vkPoeni <= 60:
            ocena=6
        elif 60 < vkPoeni <= 70:
            ocena=7
        elif 70 < vkPoeni <= 80:
            ocena=8
        elif 80 < vkPoeni <= 90:
            ocena=9
        else:
            ocena=10

        if brIndeks in Students:
            Students[brIndeks]['subjects'].append({
                'subject': predmet,
                'grade': ocena
            })
        else:
            Students[brIndeks]={
                'name':ime,
                'surname': prezime,
                'index': brIndeks,
                'subjects':[{
                    'subject': predmet,
                    # 'pointsT': poeniT,
                    # 'pointsP': poeniP,
                    # 'pointsL': poeniL
                    'grade': ocena
                }]
            }


for i in Students.values():
    print(f"Student: {i['name']} {i['surname']}")
    for j in i['subjects']:
        print(f"----{j['subject']}: {j['grade']}")
    print()
  
"""
Дефинирајте речник students во кој ќе се чуваат информации за предметите кои ги полагале студентите. 
Од стандарден влез се читаат информации за име, презиме, број на индекс, предмет, поени од теоретски дел, 
поени од практичен дел и поени од лабораториски вежби. Може да се вчитаат информации за неограничен број студенти. 
Вчитувањето информации завршува кога ќе се прочита клучниот збор end. Пополнете го речникот students со вчитаните информации.

Потоа, за секој од студентите да се испечати името и презимето, и оцената за секој од предметите кои ги има полагано.
Оцената се пресметува на следниот начин:
[0, 50] - 5
(50, 60] - 6
(60, 70] - 7
(70, 80] - 8
(80, 90] - 9
(90, 100] - 10
"""
