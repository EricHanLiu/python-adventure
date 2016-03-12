import time
import random
import sys
from fight import Fight
from game import Game
from player import Player
from shop import Shop
from help import Help

"""colour text"""
def red(text): print("\033[91m {}\033[00m" .format(text)),
def purple(text): print("\033[95m {}\033[00m" .format(text)),
def yellow(text): print("\033[93m {}\033[00m" .format(text)),

print(chr(27) + "[2J")
player_name = raw_input('What is your name?\n')
player = Player(player_name)
game = Game(player)
fight = Fight(player, game)
help = Help()
shop = Shop(player, game)
print(chr(27) + "[2J")
red("\nWelcome to Polandia, %s" % player_name)

while True:
    game.info()
    choice = raw_input()
    print
    print(chr(27) + "[2J")
    print
    if choice == '1':
        if (player.walk() == 1):
            fight.encounter()
    elif choice == '2':
        player.rest()
    elif choice == '3':
        shop.display()
        continue
    elif choice == '4':
        game.quit()
    elif choice == 'H':
        help.display()
        continue
    else:
        print "Invalid Choice"
        continue    
    game.advance_day()
