import time
import random
import sys

def red(text): print("\033[91m {}\033[00m" .format(text)),
def purple(text): print("\033[95m {}\033[00m" .format(text)),
def yellow(text): print("\033[93m {}\033[00m" .format(text)),

class Shop:
    def __init__(self, player, game):
        self.player = player
        self.game = game

    def display(self):
        red("\n_______________________________________________________________________")
        print
        print
        print "Welcome to the shop."
        print "1: Browse Items"
        print "2: Leave"
        if input() == 1:
            self.browse()
        else:
            print(chr(27) + "[2J")
        
    def browse(self):
        #time.sleep(1)
        red("\n_______________________________________________________________________")
        print
        print
        yellow("Gold: %s" % self.player.gold)
        print
        purple("Item                       Price                       Effect")
        red("\n_______________________________________________________________________")
        print
        yellow("1: Heart Piece             100                         +50 Health")
        print
        print
        yellow("2: Charm                   120                         +1 Luck")
        print
        print
        yellow("3: Time Shard              150                         -5 Days")
        print
        print
        yellow("4: Time Piece              300                         -10 Days")
        print
        print
        yellow("5: Time Gem                5000                        Restores Peace")   
        print
        n = input()
        print(chr(27) + "[2J")
        red("\n******")   
        print
        if n == 1 and self.player.gold >= 100:
            print "You have purchased a Heart Piece!"
            self.player.gold -= 100
            self.player.health += 50
            print "Health increased by 50! (Can exceed 100)"
        elif n == 2 and self.player.gold >= 120:
            print "You have purchased a Charm!"
            self.player.gold -= 120
            self.player.luck += 1
            print "Luck +1"
        elif n == 3 and self.player.gold >= 150:
            print "You have purchased a Time Shard!"
            self.player.gold -= 150
            self.game.day -= 5
            self.game.sky -= 1
            print "What's going on?..."
            #time.sleep(5)
            print "You have gone back 5 days in time!"
        elif n == 4 and self.player.gold >= 300:
            print "You have purchased a Time Piece!"
            self.player.gold -= 300
            self.game.day -= 10
            self.game.sky -= 2
            print "What's going on?......"
            #time.sleep(10)
            print "You have gone back 10 days in time!" 
        elif n == 5 and self.player.gold >= 5000:
            print "You have purchased a Time Gem!"
            self.player.gold -= 5000
            #time.sleep(2)
            print "Whoa..."
            #time.sleep(2)
            print "The sky is returning back to normal!"
            print "HOORAY YOU DID IT YOU WON THE GAME WOOHOO"
            #time.sleep(2)
            self.game.quit()
        else:
            red("Not enough gold!")
