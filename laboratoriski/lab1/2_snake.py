from searching_framework import Problem, breadth_first_graph_search
class Zmija(Problem):
    def __init__(self, initial, crveni):
        super().__init__(initial)
        self.crveni = crveni

    def dvizenje(self, zmija, nasoka, direction):
        x, y = zmija[0]
        new_nasoka = nasoka
        if direction == 'ProdolzhiPravo':

            if nasoka == "dolu":
                y -= 1

            elif nasoka == "gore":
                y += 1

            elif nasoka == "desno":
                x += 1

            elif nasoka == "levo":
                x -= 1
        elif direction == 'SvrtiLevo':

            if nasoka == "dolu":
                x += 1
                new_nasoka = "desno"

            elif nasoka == "gore":
                x -= 1
                new_nasoka = "levo"

            elif nasoka == "desno":
                y += 1
                new_nasoka = "gore"

            elif nasoka == "levo":
                y -= 1
                new_nasoka = "dolu"
        elif direction == 'SvrtiDesno':

            if nasoka == "dolu":
                x -= 1
                new_nasoka = "levo"

            elif nasoka == "gore":
                x += 1
                new_nasoka = "desno"

            elif nasoka == "desno":
                y -= 1
                new_nasoka = "dolu"

            elif nasoka == "levo":
                y += 1
                new_nasoka = "gore"

        return (x, y), new_nasoka

    def goal_test(self, state):
        return len(state[1]) == 0

    def check_valid(self, pos, zmija):
        return 0 <= pos[0] < 10 and \
            0 <= pos[1] < 10 and \
            pos not in self.crveni and \
            pos not in zmija

    def successor(self, state):
        successors = {}
        zmija = list(state[0])
        zeleni = list(state[1])

        directions = ("ProdolzhiPravo", "SvrtiDesno", "SvrtiLevo")
        for direction in directions:

            zmija_glava, new_nasoka = self.dvizenje(state[0], state[2], direction)

            if self.check_valid(zmija_glava, zmija):
                zmija.insert(0, zmija_glava)
                if zmija_glava in zeleni:
                    zeleni.remove(zmija_glava)
                else:
                    zmija.pop()

                successors[direction] = (tuple(zmija), tuple(zeleni), new_nasoka)
                zmija = list(state[0])
                zeleni = list(state[1])

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]


if __name__ == '__main__':
    n_zeleni = int(input())
    zeleni = list()
    for _ in range(n_zeleni):
        zeleni.append(tuple(map(int, input().split(","))), )

    n_crveni = int(input())
    crveni = list()
    for _ in range(n_crveni):
        crveni.append(tuple(map(int, input().split(","))), )

    zmija = ((0, 7), (0, 8), (0, 9))
    initial = (zmija, tuple(zeleni), "dolu")

    problem = Zmija(initial, tuple(crveni))
    result = breadth_first_graph_search(problem)

    if result is not None:
        print(result.solution())
    else:
        print("No Solution!")
