import math

import Player


class Field():
    def __init__(self):
        self.pokemon = []

    def print_state(self):
        print("You look around and see: ")
        for pokemon in self.pokemon:
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


def print_help(p, m):
    print("All Commands: ")
    for command in Commands:
        print(command)


def quit_game(p, m):
    print("You commit suicide and leave this world.")
    exit(0)


def forward(p, m):
    m.forward()


def backwards(p, m):
    m.backwards()


def right(p, m):
    m.right()


def left(p, m):
    m.left()

def print_state(p, m):
    m.print_state()

Commands = {
    "help": print_help,
    "quit": quit_game,
    "forward": forward,
    "backward": backwards,
    "right": right,
    "left": left,
    "state": print_state,
}

height = int(input("Please enter the height of the map: "))
width = int(input("Please enter the width of the map: "))
name = input("Please enter your name: ")

if name != "" and height > 0 and width > 0:
    player = Player.Player(name)
    map = Map(width, height)
    while True:
        command = input(">")
        if command in Commands:
            Commands[command](player, map)
        else:
            print("You run around in circles and don't know what to do.")
