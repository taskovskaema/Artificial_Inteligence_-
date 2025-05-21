from searching_framework import Problem, astar_search


class domaSiEdoma(Problem):
    def __init__(self, initial, kukja, precki, koordinaten):
        super().__init__(initial)
        self.matrica = koordinaten
        self.kukja = kukja
        self.precki = precki

        # print(coek,kukja,precki,matrica)

    def goal_test(self, state):
        return state == self.kukja

    def check_valid(self, state):
        x, y = state
        return 0 <= x < self.matrica[0] and 0 <= y < self.matrica[1] and state not in self.precki

    def successor(self, state):
        sleden = {}

        coekX, coekY = state

        direkci = {
            ("Desno 2", (2, 0)),
            ("Desno 3", (3, 0)),
            ("Gore", (0, 1)),
            ("Dolu", (0, -1)),
            ("Levo", (-1, 0)),
        }

        for akci, (dx, dy) in direkci:
            tmpx, tmpy = coekX, coekY
            # if akci=="Desno 2" or akci=="Desno 3":
            #     desnocoek=(tmpx+1,tmpy)
            #     if not self.check_valid(desnocoek):
            #         break
            #
            # if akci=="Desno 3":
            #     desnocoek=(tmpx+2,tmpy)
            #     if not self.check_valid(desnocoek):
            #         break

            if akci.startswith("Desno"):
                cekori = int(akci.split(' ')[1])
                flag = True

                for i in range(0,cekori+1):
                    if not self.check_valid((tmpx + i, tmpy)):
                        flag = False
                        break
                if flag:
                    desnocoek = (tmpx + i, tmpy)
                    sleden[akci] = desnocoek

            else:
                nov_coek = (coekX + dx, coekY + dy)
                if self.check_valid(nov_coek):
                    sleden[akci] = nov_coek

        return sleden

    def h(self, node):
        px, py = node.state
        hx, hy = self.kukja

        return (abs(px - hx)+ abs(py - hy))/3

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]


if __name__ == '__main__':
    n = int(input())
    matrica = (n, n)

    m = int(input())
    precki = []
    for i in range(m):
        koord = input()
        precki.append(tuple(map(int, koord.split(","))))

    coek = tuple(map(int, input().split(",")))
    kukja = tuple(map(int, input().split(",")))

    problem = domaSiEdoma(coek, kukja, precki, matrica)

    odgovor = astar_search(problem)

    if odgovor is not None:
        print(odgovor.solution())
    else:
        print("No solution!")

    # print(coek, kukja, tuple(precki))
