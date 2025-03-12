# from searching_framework.uninformed_search import *
from searching_framework import breadth_first_graph_search
from searching_framework.utils import Problem


class Footbal(Problem):

    def __init__(self, initial):
        super().__init__(initial)  # neznam sopraj ova proveri
        # to so si se vnesva od minot + SE STATICNO I ZABRANETO
        self.gol = ((7, 2), (7, 3))
        self.protivnici = ((3, 3), (5, 4))
        # okolu coecinjata 8te kocki
        self.zabraneti_pozici = (
        (2, 2), (2, 3), (2, 4), (3, 2), (3, 4), (4, 2), (4, 3), (4, 4), (4, 5), (5, 3), (5, 5), (6, 3), (6, 4), (6, 5))

    def goal_test(self, state):
        """Врати True ако state е целна состојба. Даденава имплементација
        на методот директно ја споредува state со self.goal, како што е
        специфицирана во конструкторот. Имплементирајте го овој метод ако
        проверката со една целна состојба self.goal не е доволна.

        :param state: дадена состојба
        :return: дали дадената состојба е целна состојба
        :rtype: bool
        """
        return state[1] in self.gol  # [1] za koordinatite na topkata od ko ke se postigni celta

    def check_valid(self, state, protivnici):
        # dali koordinatite na coeceto,topkata,protivnicite se na valino mesto- vnatre vo matricata int int...
        coek = state[0]
        topka = state[1]
        return (0 <= coek[0] <= 7 and 0 <= coek[1] <= 7 and 0 <= topka[0] <= 7 and 0 <= topka[1] <= 7 and
                topka not in self.protivnici and topka not in self.zabraneti_pozici and
                coek not in self.protivnici)

    # def successor(self, state):
    #     sleden = {}
    #     coekX, coekY = state[0]  # koordinati na coeko
    #     topkaX, topkaY = state[1]  # koordinati na topkata
    #     topkaKoordinati = (topkaX, topkaY)
    #     akci = ("gore", "dolu", "desno", "goredesno", "doludesno")  # akci kade mozhat da se dvizhat coeceto i topkata
    #     direkci = ((0, 1), (0, -1), (1, 0), (1, 1), (1, -1))
    #
    #     for direkci, akci in zip(direkci, akci):
    #         coekX = coekX + direkci[0]
    #         coekY = coekY + direkci[1]
    #         coek = coekX, coekY
    #         novaTopkaX, novaTopkaY = state[1]
    #
    #         if self.check_valid((coek, topkaKoordinati), self.protivnici):
    #             # provervame dali topkata i coeceto se na pravilno mesto za
    #             # da mozi da se shutni topkata
    #             if (coekX, coekY) == (novaTopkaX, novaTopkaY):
    #                 novaTopkaX = topkaX + direkci[0]
    #                 novaTopkaY = topkaY + direkci[1]
    #                 novaTopkaKoordinati = (novaTopkaX, novaTopkaY)
    #                 if self.check_valid((coek, novaTopkaKoordinati), self.protivnici):
    #                     sleden[f'Turni topka {akci}'] = (coek, novaTopkaKoordinati)
    #                     sleden['Pomesti coece{akci}'] = (coek, novaTopkaKoordinati)
    #
    #     return sleden

    def successor(self, state):
        sleden = {}
        coekX, coekY = state[0]
        topkaX, topkaY = state[1]

        akci = ["gore", "dolu", "desno", "gore-desno", "dolu-desno"]
        direkci = [(0, 1), (0, -1), (1, 0), (1, 1), (1, -1)]

        for (dx, dy), akci in zip(direkci, akci):
            new_coek = (coekX + dx, coekY + dy)

            if self.check_valid((new_coek, (topkaX, topkaY)), self.protivnici):
                sleden[f'Pomesti coece {akci}'] = (new_coek, (topkaX, topkaY))

                if new_coek == (topkaX, topkaY):  # ako coeceto e na pravilni mesto do topkata
                    new_topka = (topkaX + dx, topkaY + dy)
                    if self.check_valid((new_coek, new_topka), self.protivnici):
                        sleden[f'Turni topka {akci}'] = (new_coek, new_topka)

        return sleden

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]


if __name__ == '__main__':

    coek = tuple(map(int, input().split(",")))  # se vnesvat koordinatite za coeceto
    topka = tuple(map(int, input().split(",")))  # koordinatite za topkata
    protivnici = [(3, 3), (5, 4)]  # staticni protivnici gi brojs od slikata koordinatite
    problem = Footbal((coek, topka))
    odgovor = breadth_first_graph_search(problem)
    if odgovor is not None:
        print(odgovor.solution())
    else:
        print("No solution found")

