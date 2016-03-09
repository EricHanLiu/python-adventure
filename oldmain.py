""" game very loosely based off of majora's mask with the day system 
as time goes on random (lunar?) events happen that affect the game and character (mostly to be implemented)
shop where you can buy time potions to extend the time you have before you die
"""

import time
import random
import sys


"""colour text"""
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
    def encounter(self): 
        self.chance = player.luck * random.randint(0,4)
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
        if player.health <= 0:
            print
            print "You have died!"
            time.sleep(2)
            game.quit()
        
    def fight(self):
        #time.sleep(1)
        print "You attacked!"
        #time.sleep(1)
        if self.chance >= self.monster["res"] - 1:
            #YOU TAKE 1/5 DAMAGE AND DOUBLE GOLD
            print "You gained the upper hand!"
            #time.sleep(1)
            player.gold += self.monster["gold"] * 2
            yellow("Gold +%d" % (self.monster["gold"] * 2))
            print
            red("Health -%d" % (self.monster["damage"] / 5))
            player.health -= self.monster["damage"] / 5
        else:
            #YOU TAKE NORMAL DAMAGE AND GET NORMAL GOLD
            player.gold += self.monster["gold"]
            yellow("Gold +%d" % self.monster["gold"])
            print
            red("Health -%d" % (self.monster["damage"]))
            player.health -= self.monster["damage"]

    def charm(self):
        print "Attempting to charm..."
        #time.sleep(1)
        if self.chance > self.monster["res"]:
            print "Attempt successful!"
            player.gold += self.monster["gold"] * 4
            print
            yellow("Gold +%d" % (self.monster["gold"] * 4))
        else:          
            print "Attempt failed!"
            print "You have enraged it!"
            red("Health -%d" % (self.monster["damage"] * 2))
            player.health -= self.monster["damage"] * 2
            


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
            fight.encounter()
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


class Game: 
    sky_event = ["pleasant", "terrible", "beautiful", "dark", "pretty", "horrid", "scary"]
    odd_sky = ["It's unusually bright today...", "It's unusually dark today...", "There's something odd in the sky...", "The sun looks odd...", "The moon looks red...", "Why is the moon so close..?", "**You hear a faint rumbling...**"]

    def __init__(self):
        self.day = 1
        self.sky = -1
        
    def advance_day(self):
        self.day += 1
        if self.day % 5 == 0:
            self.sky += 1
        if self.day == 36:
            print "\nTHE MOON HAS CRASHED INTO THE EARTH, KILLING EVERYONE"
            self.quit()

    def quit(self):
        print
        print "Game Over"
        sys.exit(0)

    def info(self):
        red("\n_______________________________________________________________________")
        purple("\n\nName: %s" % player.name)
        #time.sleep(2)
        purple("\n\nDay: %s" % self.day)
        if self.day % 5 == 0:
            red("                        %s" % self.odd_sky[self.sky])
            player.luck += 1
        else:
            print "		             The sky looks", self.sky_event[random.choice(range(6))], "today."
        red("\n_______________________________________________________________________")
        purple("\n\nHealth: %d" % player.health)
        purple("                       		Junk: %d" % player.junk)
        #time.sleep(2)
        yellow("\n\nLuck: %d" % player.luck) 
        yellow("                    	      		Gold: %d" % player.gold)
        red("\n_______________________________________________________________________")
        #time.sleep(2)
        print "\n\nWhat would you like to do?\n"
        print "1: Walk\n"
        print "2: Rest\n"
        print "3: Shop\n"
        print "4: Quit\n"
        print "H: Help\n"


class Shop:
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
        yellow("Gold: %s" % player.gold)
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
        if n == 1 and player.gold >= 100:
            print "You have purchased a Heart Piece!"
            player.gold -= 100
            player.health += 50
            print "Health increased by 50! (Can exceed 100)"
        elif n == 2 and player.gold >= 120:
            print "You have purchased a Charm!"
            player.gold -= 120
            player.luck += 1
            print "Luck +1"
        elif n == 3 and player.gold >= 150:
            print "You have purchased a Time Shard!"
            player.gold -= 150
            game.day -= 5
            game.sky -= 1
            print "What's going on?..."
            #time.sleep(5)
            print "You have gone back 5 days in time!"
        elif n == 4 and player.gold >= 300:
            print "You have purchased a Time Piece!"
            player.gold -= 300
            game.day -= 10
            game.sky -= 2
            print "What's going on?......"
            #time.sleep(10)
            print "You have gone back 10 days in time!" 
        elif n == 5 and player.gold >= 5000:
            print "You have purchased a Time Gem!"
            player.gold -= 5000
            #time.sleep(2)
            print "Whoa..."
            #time.sleep(2)
            print "The sky is returning back to normal!"
            print "HOORAY YOU DID IT YOU WON THE GAME WOOHOO"
            #time.sleep(2)
            game.quit()
        else:
            red("Not enough gold!")

class Help:
    def display(self):
        purple("Welcome to the help module.\n")
        print "What would you like information on?\n"
        print "1: How do days work?\n"
        print "2: How do shop items work?\n"
        print "3: How does resting work?\n"
        print "4: How does walking work?\n"
        n = input()
        print
        if n == 1:
            self.day_info()
        elif n == 2:
            self.shop_info()
        elif n == 3:
            self.rest_info()
        elif n == 4:
            self.walk_info()
        else:
            print "Invalid input! Leaving help screen."

    def day_info(self):
        print "The game works on a day system that advances based on player actions. Resting or walking both advance the day, while browsing the shop does not. Every 5 days the player will notice a unique event in the sky, and will be granted 1 luck. After a certain amount of these events the game will end and the player will lose, therefore the player must aim to beat the game before this happens (info on how to do this in the shop items info). "
    def shop_info(self):
        print "The shop allows the user to buy very useful items using the gold earned through refining junk or monster encounters. In order to defeat the game, the player must purchase the 'Time Gem'. The 'Time Shard / Piece' allow the player to reverse time yet keep the player's current statistics, which is crucial to complete the game before the final day."
    def rest_info(self):
        print "Resting provides the player two options. They can either rest and recover 20 health, or can refine junk to receive gold. Refining junk requires both junk and luck, and these two variables act as multipliers to increase the amount of gold received per piece of junk. Attempting to refine junk without luck will provide a very small amount of gold, and is not advised."
    def walk_info(self):
        print "While walking, the player the can have 3 possible encounters. Either they will find a charm (increase luck), find junk, or encounter a monster. On this encounter the player can either fight, charm, or run. Fighting will damage the player and earn them gold, the amount depending on the type of monster and the player's luck compared to the monster's resilience. Charming a monster can either earn the player lots of gold without taking damage, or no gold while taking lots of damage (based on luck). Finally, the player can run from the monster, but the day will advance."

fight = Fight()
game = Game()
help = Help()
shop = Shop()
print(chr(27) + "[2J")
player_name = raw_input('What is your name?\n')
player = Player(player_name)
print(chr(27) + "[2J")
red("\nWelcome to Polandia")


while True:
    game.info()
    choice = raw_input()
    print
    print(chr(27) + "[2J")
    print
    if choice == '1':
        player.walk()
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
