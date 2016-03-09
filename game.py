import time
import random
import sys

def red(text): print("\033[91m {}\033[00m" .format(text)),
def purple(text): print("\033[95m {}\033[00m" .format(text)),
def yellow(text): print("\033[93m {}\033[00m" .format(text)),

class Game(): 
    sky_event = ["pleasant", "terrible", "beautiful", "dark", "pretty", "horrid", "scary"]
    odd_sky = ["It's unusually bright today...", "It's unusually dark today...", "There's something odd in the sky...", "The sun looks odd...", "The moon looks red...", "Why is the moon so close..?", "**You hear a faint rumbling...**"]

    def __init__(self, player):
        self.day = 1
        self.sky = -1
        self.player = player
        
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
        #time.sleep(2)
        red("\n_______________________________________________________________________")
        purple("\n\nName: %s" % self.player.name)
        purple("\nDay: %s" % self.day)
        if self.day % 5 == 0:
            red("                        %s" % self.odd_sky[self.sky])
            self.player.luck += 1
        else:
            print "		             The sky looks", self.sky_event[random.choice(range(6))], "today."
        red("\n_______________________________________________________________________")
        purple("\n\nHealth: %d" % self.player.health)
        purple("                       		Junk: %d" % self.player.junk)
        #time.sleep(2)
        yellow("\n\nLuck: %d" % self.player.luck) 
        yellow("                    	      		Gold: %d" % self.player.gold)
        red("\n_______________________________________________________________________")
        #time.sleep(2)
        print "\n\nWhat would you like to do?\n"
        print "1: Walk\n"
        print "2: Rest\n"
        print "3: Shop\n"
        print "4: Quit\n"
        print "H: Help\n"
