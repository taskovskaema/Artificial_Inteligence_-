from searching_framework import Problem, astar_search

class kajMieKukjata(Problem):

    def __init__(self,initial,dzid):
        super().__init__(initial,dzid)
        self.zeleniosumagolnici=dzid
        self.koordinaten=(5,9)


    def goal_test(self, state):
        c=state[0]
        k=state[1]
        return c[0]==k[0] and c[1]==k[1]

    def check_valid(self,state):
        coek=state[0]
        kukja=state[1]

        return 0<=coek[0]<=self.koordinaten[0] and 0<=coek[1]<=self.koordinaten[1] and coek in self.zeleniosumagolnici
        # coek_x, coek_y = state[0]
        # house_x, house_y = state[1]

        # if coek_x < 0 or coek_x > 4:
        #     return False
        #
        # if coek_y < 0 or coek_y > 8:
        #     return False
        #
        # if coek_y == 7:
        #      return (coek_x, coek_y) == (house_x, house_y)
        #
        # return (coek_x, coek_y) in self.zeleniosumagolnici

    def successor(self, state):
        sleden={}

        coekX,coekY=state[0]
        kukjaX,kukjaY=state[1]

        strana=state[2]

        if strana=="desno":
            newKukjaX=kukjaX + 1
            if newKukjaX==self.koordinaten[0]-1:
                strana="levo"
        elif strana=="levo":
            newKukjaX = kukjaX - 1
            if newKukjaX==0:
                strana="desno"



        direkci={
            ("Stoj",(0,0)),
            ("Gore 1",(0,1)),
            ("Gore 2",(0,2)),
            ("Gore-desno 1",(1,1)),
            ("Gore-desno 2",(2,2)),
            ("Gore-levo 1",(-1,1)),
            ("Gore-levo 2",(-2,2)),
        }

        kukjaKoord=(newKukjaX,kukjaY)

        for akci, (dx,dy) in direkci:
            nov_coek=(coekX+dx,coekY+dy)
            nov_state=(nov_coek,kukjaKoord,strana)
            if self.check_valid(nov_state) or nov_coek==kukjaKoord:
                sleden[akci]=nov_state

        return sleden

    def h(self, node):
        state = node.state
        covek_x, covek_y = state[0]
        house_x, house_y = state[1]

        return (covek_y - house_y) / 2

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]


if __name__ == '__main__':
    coece=tuple(map(int,input().split(',')))
    kukjicka=tuple(map(int,input().split(',')))
    kade=input()
    allowed = [(1, 0), (2, 0), (3, 0), (1, 1), (2, 1), (0, 2), (2, 2), (4, 2), (1, 3), (3, 3), (4, 3), (0, 4), (2, 4),
               (2, 5), (3, 5), (0, 6), (2, 6), (1, 7), (3, 7)]
    problem=kajMieKukjata((coece,kukjicka, kade),allowed)
    odgovor=astar_search(problem)

    # print(coece,kukjicka, kade)

    if odgovor is not None:
        print(odgovor.solution())
    else:
        print("No solution!")
    # your code here
