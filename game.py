from settings import (
    GAME_SIZE
)
from functools import (
    reduce
)
import random


def render_grid(grid):
    dashcount = 2 * GAME_SIZE + 1
    print('+' + dashcount*'-' + '+')
    print('| |' + ''.join([str(d) + '|' for d in range(GAME_SIZE)]))
    chr_idx = 65
    for row in grid:
        print('|' + chr(chr_idx) + '|' + '|'.join(row) + '|')
        chr_idx+=1
    print('+' + dashcount*'-' + '+')

class Game():
    def __init__(self):
        self.p1 = Player()
        self.p2 = Player()
        # for now randomly pick positions for ships
        self.p1.random_place()
        self.p2.random_place()
        
        self.run()

    def run(self):
        players = [self.p1, self.p2]
        pid = 0
        while True:
            players[pid].render()
            target = input('[p%s] coords to attack (eg. E4)>> ' % str(pid+1))
            target = target.upper()
            y = int(target[1])
            x = ord(target[0]) - 65
            hit = players[(pid+1) % 2].hit_check(x, y)
            if hit:
                players[pid].tracking_grid[x][y] = 'X'
            else:
                players[pid].tracking_grid[x][y] = 'o'
            pid = (pid+1) % 2

        

class Player():
    def __init__(self):
        self.fleet = [
            Ship(5, 'Aircraft Carrier', 'A'),
            Ship(4, 'Battleship', 'B'),
            Ship(3, 'Cruiser', 'C'),
            Ship(2, 'Destroyer', 'D'),
            Ship(2, 'Destroyer', 'D'),
            Ship(1, 'Submarine', 'S'),
            Ship(1, 'Submarine', 'S'),
        ]
        # shows letters of ships on grid (for now)
        self.player_grid = [['-']*GAME_SIZE for i in range(GAME_SIZE)]
        # ' ' - not fired, X miss, o hit
        self.tracking_grid = [[' ']*GAME_SIZE for i in range(GAME_SIZE)]

    def render(self):
        print('Tracking Grid')
        render_grid(self.tracking_grid)
        print('')
        print('')
        print('Fleet Position')
        render_grid(self.player_grid)

    def random_place(self):
        for ship in self.fleet:
            while True:
                ship.random_place()
                if not self.is_collision():
                    # load into grid
                    for x, y in ship.coords:
                        self.player_grid[x][y] = ship.symbol
                    #print('%s Done' % ship.name)
                    break

    def is_collision(self):
        coords = list(reduce(lambda x, y: x + y, [ship.coords for ship in self.fleet]))
        coords = [str(c) for c in coords]
        return sorted(coords) != sorted(list(set(coords)))

    def hit_check(self, x, y):
        for i, ship in enumerate(self.fleet):
            for j, coord in enumerate(ship.coords):
                if coord == [x, y]:
                    self.fleet[i].coords[j] = 1
                    self.player_grid[x][y] = 'X'
                    return True
        self.player_grid[x][y] = 'o'
        return False
        


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


