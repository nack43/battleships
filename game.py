from settings import (
    GAME_SIZE
)


class Game():
    def __init__(self):
        p1 = Player()
        p2 = Player()
        

class Player():
    def __init__(self):
        self.aircraft_carrier = Ship(5, 'Aircraft Carrier', 'A')
        self.battleship = Ship(4, 'Battleship', 'B')
        self.submarine = Ship(3, 'Cruiser', 'C')
        self.cruiser = Ship(3, 'Submarine', 'S')
        self.destroyer = Ship(2, 'Destroyer', 'D')
        # shows letters of ships on grid (for now)
        self.player_grid = [['-']*GAME_SIZE]*GAME_SIZE
        # no - not fired, -1 miss, 1 hit
        self.tracking_grid = [[0]*GAME_SIZE]*GAME_SIZE


class Ship():
    def __init__(self, size, name, symbol):
        self.size = size
        self.name = name
        self.symbol = symbol
        # each part of the ship has an integer
        # 1 = hit, 0 = not hit
        self.parts = [0] * size
        # location data, start 
        self.x = -1
        self.y = -1
        self.heading = -1

    def is_destroyed(self):
        return sum(self.parts) == size


