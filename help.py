import time
import random
import sys
import c


class Help:
    def display(self):
        c.purple("Welcome to the help module.\n")
        print("What would you like information on?\n")
        print("1: How do days work?\n")
        print("2: How do shop items work?\n")
        print("3: How does resting work?\n")
        print("4: How does walking work?\n")
        print("5: Leave help screen.")
        n = input()
        print()
        if n == '1':
            self.day_info()
        elif n == '2':
            self.shop_info()
        elif n == '3':
            self.rest_info()
        elif n == '4':
            self.walk_info()
        else:
            print("Leaving help screen.")
        print("Type any key to continue...")
        input()


    def day_info(self):
        print("The game works on a day system that advances based on player actions. Resting or walking both advance the day, while browsing the shop does not. Every 5 days the player will notice a unique event in the sky, and will be granted 1 luck. After a certain amount of these events the game will end and the player will lose, therefore the player must aim to beat the game before this happens (info on how to do this in the shop items info). ")
    def shop_info(self):
        print("The shop allows the user to buy very useful items using the gold earned through refining junk or monster encounters. In order to defeat the game, the player must purchase the 'Time Gem'. The 'Time Shard / Piece' allow the player to reverse time yet keep the player's current statistics, which is crucial to complete the game before the final day.")
    def rest_info(self):
        print("Resting provides the player two options. They can either rest and recover 20 health, or can refine junk to receive gold. Refining junk requires both junk and luck, and these two variables act as multipliers to increase the amount of gold received per piece of junk. Attempting to refine junk without luck will provide a very small amount of gold, and is not advised.")
    def walk_info(self):
        print("While walking, the player the can have 3 possible encounters. Either they will find a charm (increase luck), find junk, or encounter a monster. On this encounter the player can either fight, charm, or run. Fighting will damage the player and earn them gold, the amount depending on the type of monster and the player's luck compared to the monster's resilience. Charming a monster can either earn the player lots of gold without taking damage, or no gold while taking lots of damage (based on luck). Finally, the player can run from the monster, but the day will advance.")
