from constraint import *

def con_func(marija,simona,petar,sostanok):
    marija_vreme=[14,15,18]
    petar_vreme=[12,13,16,17,18,19]
    simona_vreme=[13,14,16,19]

    if sostanok not in simona_vreme or simona==0:
        return False
    if sostanok not in marija_vreme and marija==1:
        return False
    if sostanok not in petar_vreme and petar==1:
        return False

    return (petar+marija)>=1

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    # ---Dadeni se promenlivite, dodadete gi domenite-----
    problem.addVariable("Marija_prisustvo", [0,1])
    problem.addVariable("Simona_prisustvo", [0,1])
    problem.addVariable("Petar_prisustvo", [0,1])
    problem.addVariable("vreme_sostanok", [12,13,14,15,16,17,18,19])

    # ---Tuka dodadete gi ogranichuvanjata----------------
    problem.addConstraint(con_func, ("Marija_prisustvo","Simona_prisustvo","Petar_prisustvo","vreme_sostanok"))
    # ----------------------------------------------------
    # [print(solution) for solution in problem.getSolutions()]

    solutions=problem.getSolutions()

    for res in solutions:
        pecati={
                "Simona_prisustvo":res["Simona_prisustvo"],
                "Marija_prisustvo":res["Marija_prisustvo"],
                "Petar_prisustvo":res["Petar_prisustvo"],
                "vreme_sostanok":res["vreme_sostanok"]
                }
        print(pecati)

