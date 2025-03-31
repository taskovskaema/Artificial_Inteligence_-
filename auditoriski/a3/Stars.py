NE RABOTI ZA POVEKJE DZVEZDI, SAMO TIE OD AUD.

from searching_framework import breadth_first_graph_search
from searching_framework.utils import Problem


class Stars(Problem):
    def __init__(self, initial, stars, cel=None):
        new_initial = initial + stars
        # print(new_initial)
        super().__init__(new_initial, cel)
        # self.dzvezdi=stars
        self.tabla = (7, 7)

    def goal_test(self, state):
        return len(state[4:]) == 0


    def check_valid(self, koordinati, state):
        x, y = koordinati
        k, l = (state[0], state[1]), (state[2], state[3])
        return (0 <= x <= self.tabla[0] and
                0 <= y <= self.tabla[1] and
                koordinati != k and koordinati != l)

    def successor(self, state):
        sleden = {}
        konj = state[0], state[1]
        lanfer = state[2], state[3]
        svetlecha_topka = state[4:]

        dvizhenjekojnche = {
            ("K1", (-1, 2)),  # gore-levo
            ("K2", (1, 2)),  # gore-desno
            ("K3", (2, 1)),  # desno-gore
            ("K4", (2, -1)),  # desno-dolu
            ("K6", (-1, -2)),  # dolu-levo
            ("K5", (1, -2)),  # dolu-desno
            ("K7", (-2, -1)),  # levo-dolu
            ("K8", (-2, 1))  # levo-gore
        }

        dvizhenjelanferche = {
            ("B1", (-1, 1)),  # gore-levo
            ("B2", (1, 1)),  # gore-desno
            ("B3", (-1, -1)),  # dolu-levo
            ("B4", (1, -1)),  # dolu-desno
        }

        if konj in lanfer:
            return sleden

        for action, (kx, ky) in dvizhenjekojnche:
            novo_kojnche = (konj[0] + kx, konj[1] + ky)
            if self.check_valid(novo_kojnche, state):
                ostanati_dzvezdi = tuple(dz for dz in svetlecha_topka if dz != novo_kojnche)
                sleden[action] = (novo_kojnche[0], novo_kojnche[1], lanfer[0], lanfer[1]) + ostanati_dzvezdi

        for action, (lx, ly) in dvizhenjelanferche:
            # ke ima slucaevi kaj sho lanferot ke mora pokje od 1 kocka da se pomesti
            x, y = lanfer[0], lanfer[1]
            while True:
                x += lx
                y += ly
                novo_lanferche = (x, y)
                
                if novo_lanferche in svetlecha_topka:
                    break
                if not self.check_valid(novo_lanferche,state):
                    break

            ostanati_dzvezdi = tuple(dz for dz in svetlecha_topka if dz != novo_lanferche)
            sleden[action] = (konj[0], konj[1], novo_lanferche[0], novo_lanferche[1]) + ostanati_dzvezdi

        return sleden

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]


if __name__ == '__main__':
    dzvezdi = ((1, 1), (4, 3), (6, 6))
    konjce = (2, 5)
    lanferche = (5, 1)

    problem = Stars((konjce[0], konjce[1], lanferche[0], lanferche[1]), dzvezdi)
    odgovor = breadth_first_graph_search(problem)

    if odgovor is not None:
        print(odgovor.solution())
    else:
        print("No solution")
