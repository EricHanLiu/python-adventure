import time
import random
import sys

def red(text): print("\033[91m {}\033[00m" .format(text)),
def purple(text): print("\033[95m {}\033[00m" .format(text)),
def yellow(text): print("\033[93m {}\033[00m" .format(text)),

MONSTERS = [
    # Monster name: the amount of damage it does: amount of base gold it gives (multiplied with luck): resilience to charm or dmg
    {"name": "a zombie!", "damage": 10, "gold": 5, "res" : 3}, 
    {"name": "a skeleton!", "damage": 15, "gold": 11, "res" : 7},
    {"name": "a witch!", "damage": 40, "gold": 50, "res" : 11}, 
    {"name": "a ghost!", "damage": 25, "gold": 20, "res" : 20},
    {"name": "a giant!", "damage": 30, "gold": 35, "res" : 31}, 
]

class Fight:   
    def __init__(self, player, game):
        self.player = player
        self.game = game

    def encounter(self): 
        self.chance = self.player.luck * random.randint(0,4)
        self.monster = random.choice(MONSTERS)    
        red("\n******")
        print
        print "You encountered", self.monster["name"]
        print "1: Fight"
        print "2: Charm"
        print "3: Run"
        n = input()
        if n == 1:
            self.fight()
        elif n == 2:
            self.charm()
        else:
            print "After a day of running away, you finally escape your pursuer."
        if self.player.health <= 0:
            print
            print "You have died!"
            time.sleep(2)
            self.game.quit()
        
    def fight(self):
        #time.sleep(1)
        print "You attacked!"
        #time.sleep(1)
        if self.chance >= self.monster["res"] - 1:
            #YOU TAKE 1/5 DAMAGE AND DOUBLE GOLD
            print "You gained the upper hand!"
            #time.sleep(1)
            self.player.gold += self.monster["gold"] * 2
            yellow("Gold +%d" % (self.monster["gold"] * 2))
            print
            red("Health -%d" % (self.monster["damage"] / 5))
            self.player.health -= self.monster["damage"] / 5
        else:
            #YOU TAKE NORMAL DAMAGE AND GET NORMAL GOLD
            self.player.gold += self.monster["gold"]
            yellow("Gold +%d" % self.monster["gold"])
            print
            red("Health -%d" % (self.monster["damage"]))
            self.player.health -= self.monster["damage"]

    def charm(self):
        print "Attempting to charm..."
        #time.sleep(1)
        if self.chance > self.monster["res"]:
            print "Attempt successful!"
            self.player.gold += self.monster["gold"] * 4
            print
            yellow("Gold +%d" % (self.monster["gold"] * 4))
        else:          
            print "Attempt failed!"
            print "You have enraged it!"
            red("Health -%d" % (self.monster["damage"] * 2))
            self.player.health -= self.monster["damage"] * 2
