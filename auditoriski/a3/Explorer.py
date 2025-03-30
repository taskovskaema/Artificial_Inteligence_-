from searching_framework import breadth_first_graph_search
from searching_framework.utils import Problem


class Explorer(Problem):

    def __init__(self, initial, cel=None):
        super().__init__(initial, cel)
        self.kukja = (5, 4)
        self.flagP1 = 1
        self.tabla = [7, 5]

    def goal_test(self, state):
        coek_poz = state[0]
        return coek_poz == self.kukja

    def check_valid(self, coek_poz, precki):
        # print("state check valid - ", coek_poz)
        x, y = coek_poz
        return (0 <= x <= self.tabla[0] and
                0 <= y <= self.tabla[1] and
                coek_poz not in precki)

    def successor(self, state):

        sleden = {}
        coek_poz = state[0]
        # print("check - ",coek_poz)
        coekX, coekY = coek_poz
        precka1, precka2 = state[1]

        precka1Y = precka1[1]
        precka2Y = precka2[1]

        if self.flagP1 == 1:
            if precka1Y == 0:
                self.flagP1 = 0
                precka1Y += 1
                precka2Y -= 1
            else:
                precka1Y -= 1
                precka2Y += 1

        else:
            if precka1Y == self.tabla[1] - 1:
                self.flagP1 = 1
                precka1Y -= 1
                precka2Y += 1
            else:
                precka1Y += 1
                precka2Y -= 1

        preckite = [(precka1[0], precka1Y), (precka2[0], precka2Y)]


        if coek_poz in preckite:  #BITNO!
            return sleden

        # akci = ["Right", "Left", "Up", "Down"]
        # direkci = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        dvizhenja = [
            ("Right", (1, 0)),
            ("Left", (-1, 0)),
            ("Up", (0, 1)),
            ("Down", (0, -1))
        ]

        for action, (cX, cY) in dvizhenja:
            nov_coek = (coekX + cX, coekY + cY)
            # print(nov_coek)
            if self.check_valid(nov_coek, preckite):
                sleden[action] = (nov_coek, tuple(preckite))

        return sleden

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]


if __name__ == '__main__':

    # coece = tuple(input().split(","))
    # kukja= tuple(map(input().split(",")))
    # precki = tuple(map(input().split(",")))
    coece = (0, 2)
    precki = ((2, 5), (5, 0))

    problem = Explorer((coece, precki), (5, 4))  #plus celta
    odgovor = breadth_first_graph_search(problem)
    #print(breadth_first_graph_search(problem).solve())

    if odgovor is not None:
        print(odgovor.solution())
    else:
        print("No solution")
