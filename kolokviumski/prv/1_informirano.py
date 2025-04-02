from searching_framework import Problem, astar_search

class GhostOnSkates(Problem):
    def __init__(self, initial, precki, matrica, pacman):
        super().__init__(initial)
        self.precki = precki
        self.koordinaten = matrica
        self.pacman = pacman
        # print(initial, precki, matrica, pacman)

    def goal_test(self, state):
        return state == self.pacman

    def check_valid(self, state):
        x, y = state
        return 0 <= x < self.koordinaten[0] and 0 <= y < self.koordinaten[1] and state not in self.precki

    def successor(self, state):
        sleden = {}

        duhX, duhY = state
        # print(duhY)

        direkci = {
            ("Gore 1", (0, 1)),
            ("Gore 2", (0, 2)),
            ("Gore 3", (0, 3)),
            ("Desno 1", (1, 0)),
            ("Desno 2", (2, 0)),
            ("Desno 3", (3, 0))
        }

        for akci, (dx, dy) in direkci:
"""
          AKO NEMOZAT DA SE SKOKAT PRECKITE
            tmpX, tmpY = duhX, duhY
            if akci.startswith("Gore"):
                cekori = int(akci.split(' ')[1])
                flag = True
                for i in range(0, cekori + 1):
                    novG = (tmpX, tmpY + i)
                    if not self.check_valid(novG):
                        flag = False
                        break
                if flag:
                    novG = (tmpX, tmpY + i)
                    sleden[akci] = novG
            
            elif akci.startswith("Desno"):
                cekori = int(akci.split(' ')[1])
                flag = True
                for i in range(0, cekori + 1):
                    novD = (tmpX + i, tmpY)
                    if not self.check_valid(novD):
                        flag = False
                        break
                if flag:
                    novD = (tmpX + i, tmpY)
                    sleden[akci] = (novD)
            else:
"""          
            nov_duh = (duhX + dx, duhY + dy)  
            if self.check_valid(nov_duh):
                sleden[akci] = nov_duh

        return sleden

    def h(self, node):
        dx, dy = node.state
        px, py = self.pacman
        return (abs(dx - px) + abs(dy - py)) / 2

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
        p = input()
        precki.append(tuple(map(int, p.split(','))))

    duh = (0, 0)
    pacman = (n - 1, n - 1)

    problem = GhostOnSkates(duh, tuple(precki), matrica, pacman)
    odgovor = astar_search(problem)

    if odgovor is not None:
        print(odgovor.solution())
    else:
        print("No solution!")
