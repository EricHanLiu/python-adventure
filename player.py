import time
import random
import sys

def red(text): print("\033[91m {}\033[00m" .format(text)),
def purple(text): print("\033[95m {}\033[00m" .format(text)),
def yellow(text): print("\033[93m {}\033[00m" .format(text)),

class Player:
    def __init__(self, player_name):
        self.health = 100
        self.luck = 0
        self.junk = 0
        self.gold = 0
        self.name = player_name

    def find_charm(self):
        red("\n******")
        print
        print "You found a charm!"
        yellow("Luck +1")
        self.luck += 1
	
    def find_junk(self):
        red("\n******")
        print
        print "You found some junk!"
        yellow("Junk +1")
        self.junk += 1
    
    def walk(self):
        num_steps = random.randint(1, 10)
        if num_steps > 5:
            return 1
        elif num_steps < 5:
            self.find_junk()
        else:
            self.find_charm()

    def rest(self):
        print "\nYou are resting."
        #time.sleep(1)
        print "\nYou have", self.junk, "pieces of junk."
        print "You have", self.gold, "gold."
        #time.sleep(1)
        print "\n1: Sleep and heal."
        print "2: Refine junk (requires luck)."
        n = input()
        print(chr(27) + "[2J")
        red("\n******")
        print
        if n == 1:
            if self.health + 20 >= 100:
                yellow("You are max health!")
                self.health = 100
            else:
                self.health += 20
                yellow("+20 health!")
        else:
            if self.junk > 0:
                print "You turned your junk into gold!"
                #either put random value or 5, 5 is less punishing for early stage
                gold_amount = 1 + random.randint(5,10) * self.luck * self.junk 
                yellow("Gold + %d" % gold_amount) 
                self.gold += gold_amount
                self.junk = 0
            else:
                red("Attempt failed!")
