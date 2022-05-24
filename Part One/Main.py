import math
from unicodedata import name

import Player

class Field():
    def __init__(self, pokemon):
        self.pokemon = pokemon
        self.loot = []

    def print_state(self):
        print("You look around and see: ")
        for pokemon in pokemon:
            print(str(pokemon.name))

    @staticmethod
    def gen_random():
        return Field()
        

class Map():
    def __init__(self, width, height):
        self.map = []
        self.x = math.floor(width / 2)
        self.y = math.floor(height / 2)
        for i in range(0, width):
            fields = []
            for j in range(0, height):
                fields.append(Field.gen_random())
            self.map.append(fields)

    def print_state(self):
        self.map[self.x][self.y].print_state()

    def forward(self):
        if self.x == len(self.map) - 1:
            print("You see huge mountains, which you can't pass")
        else:
            self.x = self.x + 1

    def backwards(self):
        if self.x == 0:
            print("You see cliffs, but you can't jump safely")
        else:
            self.x = self.x - 1

    def right(self):
        if self.y == len(self.map[self.x]) - 1:
            print("You see huge mountains, which you can't pass")
        else:
            self.y = self.y + 1

    def left(self):
        if self.y == 0:
           print("You see cliffs, but you can't jump safely")
        else:
            self.y = self.y - 1


Commands = {
    "help": print_help(),
    "quit": quit(),
    "forward": forward(),
    "backward": backward(),
    "right": right(),
    "left": left(),
}

height = int(input("Please enter the height of the map: "))
width = int(input("Please enter the width of the map: "))
name = input("Please enter your name: ")