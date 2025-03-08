# bidejki se raboti so random pozici test primerite ne izlegvat tocni
import os
import random

os.environ["OPENBLAS_NUM_THREADS"] = "1"

class Player:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, pozicija):
        self.x, self.y = pozicija
        print(f"[{self.x}, {self.y}]")


class Game:
    def __init__(self, redici, koloni):
        self.redici = redici
        self.koloni = koloni
        self.matrica = [['-' for _ in range(koloni)] for _ in range(redici)]

    def valid_position(self, x, y):
        return 0 <= x < self.redici and 0 <= y < self.koloni

    def count_points(self):
        return sum(red.count('.') for red in self.matrica)


class Pacman:
    def __init__(self, redici, koloni, matrica):
        self.player = Player()
        self.game = Game(redici, koloni)
        self.game.matrica = matrica

    def play_game(self):
        if self.game.count_points() == 0:
            print("Nothing to do here")
            return

        direkcija = [(1, 0), (0, -1), (0, 1), (-1, 0)]

        while self.game.count_points() > 0:
            mozni_potezi = []
            poeni_dvizhenje = []

            for direcX, direcY in direkcija:
                newX, newY = self.player.x + direcX, self.player.y + direcY

                if self.game.valid_position(newX, newY):
                    mozni_potezi.append((newX, newY))
                    if self.game.matrica[newX][newY] == '.':
                        poeni_dvizhenje.append((newX, newY))

            if poeni_dvizhenje:
                sledna_pozicija = random.choice(poeni_dvizhenje)
            else:
                sledna_pozicija = random.choice(mozni_potezi)

            self.player.move(sledna_pozicija)
            self.game.matrica[self.player.x][self.player.y] = '#'


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    matrica = [list(input().strip()) for _ in range(n)]
    
    pacman = Pacman(n, m, matrica)
    pacman.play_game()
