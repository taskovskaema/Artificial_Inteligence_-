from searching_framework import Problem, breadth_first_graph_search, astar_search

class DijagonalniKocki(Problem):

    def __init__(self,initial,cel):
        super().__init__(initial)
        self.goal=cel
        self.matrica=(5,5)

    def goal_test(self, state):
        return state==self.goal

    def check_valid(self,state):
        return all(0<=x<5 and 0<=y< 5 for x,y in state)

    def successor(self, state):
        sleden={}


        for i in range(0,5):
            kvadratcheX,kvadratcheY=state[i]

            dvizhenja=[
                ("Pomesti kvadratche "+str(i+1)+" dolu",(0,-1)),
                ("Pomesti kvadratche "+str(i+1)+" gore",(0,1)),
                ("Pomesti kvadratche "+str(i+1)+" levo",(-1,0)),
                ("Pomesti kvadratche "+str(i+1)+" desno",(1,0)),
            ]

            for action, (dx,dy) in dvizhenja:
                new_kvadratche=(kvadratcheX+dx,kvadratcheY+dy)
                new_state = list(state)
                new_state[i] = new_kvadratche
                if self.check_valid(new_state):
                    sleden[action]=tuple(new_state)

        return sleden

    def h(self,node):
        return sum(abs(x-px)+abs(y-py) for (x,y),(px,py) in zip(node.state,self.goal))

"""   bez zip i sum
def h(self, node):
    total_distance = 0
    for i in range(len(node.state)):
        x, y = node.state[i]
        gx, gy = self.goal[i]
        total_distance += abs(x - gx) + abs(y - gy)
    return total_distance
"""

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]


if __name__ == "__main__":

    kocki=[]
    for i in range(5):
        koord=input()
        kocki.append(tuple(map(int,koord.split(","))))

    cel=((0,4),(1,3),(2,2),(3,1),(4,0))
    problem=DijagonalniKocki(tuple(kocki),cel)
    odgovor=astar_search(problem)

    if odgovor is not None:
        print(odgovor.solution())
    else:
        print("No solution!")


