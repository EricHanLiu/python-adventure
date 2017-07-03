import time
import random
import sys
import c


class Shop:
    def __init__(self, player, game):
        self.player = player
        self.game = game

    def display(self):
        c.red("\n_______________________________________________________________________")
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
        time.sleep(1)
        c.red("\n_______________________________________________________________________")
        print
        print
        c.yellow("Gold: %s" % self.player.gold)
        print
        c.purple("Item                       Price                       Effect")
        c.red("\n_______________________________________________________________________")
        print
        c.yellow("1: Heart Piece             100                         +50 Health")
        print
        print
        c.yellow("2: Charm                   120                         +1 Luck")
        print
        print
        c.yellow("3: Time Shard              150                         -5 Days")
        print
        print
        c.yellow("4: Time Piece              300                         -10 Days")
        print
        print
        c.yellow("5: Time Gem                5000                        Restores Peace")   
        print
        n = input()
        print(chr(27) + "[2J")
        c.red("\n******")   
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
            time.sleep(5)
            print "You have gone back 5 days in time!"
        elif n == 4 and self.player.gold >= 300:
            print "You have purchased a Time Piece!"
            self.player.gold -= 300
            self.game.day -= 10
            self.game.sky -= 2
            print "What's going on?......"
            time.sleep(10)
            print "You have gone back 10 days in time!" 
        elif n == 5 and self.player.gold >= 5000:
            print "You have purchased a Time Gem!"
            self.player.gold -= 5000
            time.sleep(2)
            print "Whoa..."
            time.sleep(2)
            print "The sky is returning back to normal!"
            print "HOORAY YOU DID IT YOU WON THE GAME WOOHOO"
            time.sleep(2)
            self.game.quit()
        else:
            c.red("Not enough gold!")
