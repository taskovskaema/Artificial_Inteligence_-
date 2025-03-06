"""
Задача 1 - Swap на елементи во листа од торки
Да се напише функција која за дадена листа од торки во облик
[('a', 1), ('b', 2), ('c', 3)] ќе направи swap на елементите
во торките така што елементот на позиција 0 ќе биде елемент
на позиција 1 и обратно. Да се користи list comprehension.

Пример влез: [('a', 1), ('b', 2), ('c', 3)]
Пример излез: [(1, 'a'), (2, 'b'), (3, 'c')]

+ torkite se vnesvat od s.v. posle se praj lista, pa swap
"""
def swapswap(torche):
    return [(y,x) for (x,y) in torche ]

if __name__=='__main__':

    lista=[]
    # torka=()

    while True:
        torka=input()

        if torka == 'done':
            break

        torka=torka.split(",")
        bukva=torka[0].strip()
        broj=int(torka[1].strip())

        lista.append((bukva, broj))

print(lista)

swapLista=[]
swapLista= swapswap(lista);

print(swapLista)





