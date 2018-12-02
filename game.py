from settings import (
    GAME_SIZE
)
from functools import (
    reduce
)
import random


class Game():
    def __init__(self):
        self.p1 = Player()
        self.p2 = Player()
        # for now randomly pick positions for ships
        self.p1.random_place()
        self.p2.random_place()
        

class Player():
    def __init__(self):
        self.fleet = [
            Ship(5, 'Aircraft Carrier', 'A'),
            Ship(4, 'Battleship', 'B'),
            Ship(3, 'Cruiser', 'C'),
            Ship(3, 'Submarine', 'S'),
            Ship(2, 'Destroyer', 'D'),
        ]
        # shows letters of ships on grid (for now)
        self.player_grid = [['-']*GAME_SIZE for i in range(GAME_SIZE)]
        # no - not fired, -1 miss, 1 hit
        self.tracking_grid = [[0]*GAME_SIZE for i in range(GAME_SIZE)]

    def render(self):
        print('+' + 19*'-' + '+')
        for row in self.player_grid:
            print('|' + '|'.join(row) + '|')
        print('+' + 19*'-' + '+')

    def random_place(self):
        for ship in self.fleet:
            while True:
                ship.random_place()
                if not self.is_collision():
                    # load into grid
                    for x, y in ship.coords:
                        self.player_grid[x][y] = ship.symbol
                    print('%s Done' % ship.name)
                    break

    def is_collision(self):
        coords = list(reduce(lambda x, y: x + y, [ship.coords for ship in self.fleet]))
        coords = [str(c) for c in coords]
        return sorted(coords) != sorted(list(set(coords)))


class Ship():
    def __init__(self, size, name, symbol):
        self.size = size
        self.name = name
        self.symbol = symbol
        # each part of the ship has an integer
        # 1 = hit, 0 = not hit
        self.parts = [0] * size
        # array of coords the ship uses
        self.coords = []

    def random_place(self):
        self.coords = []
        # defines wether or not the ship is horizontal or vertical
        is_vertical = random.random() > 0.5
        if is_vertical:
            # vertical - fixed x
            x = random.randint(0, GAME_SIZE-1)
            y = random.randint(0, GAME_SIZE-self.size)
        else:
            # horizontal- fixed y
            x = random.randint(0, GAME_SIZE-self.size)
            y = random.randint(0, GAME_SIZE-1)

        self.coords.append([x, y])
        for i in range(self.size-1):
            if is_vertical:
                y+=1
            else:
                x+=1
            self.coords.append([x, y])

    def is_destroyed(self):
        return sum(self.parts) == size


