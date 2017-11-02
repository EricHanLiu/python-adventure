import time
import random
import sys
import c

#def red(text): print("\033[91m {}\033[00m" .format(text)),
#def purple(text): print("\033[95m {}\033[00m" .format(text)),
#def yellow(text): print("\033[93m {}\033[00m" .format(text)),

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
            print("\nTHE MOON HAS CRASHED INTO THE EARTH, KILLING EVERYONE")
            self.quit()

    def quit(self):
        print()
        print("Game Over")
        sys.exit(0)

    def info(self):
        c.red("\n_______________________________________________________________________")
        time.sleep(2)
        c.purple("\n\nName: %s" % self.player.name)
        c.purple("\nDay: %s" % self.day)
        if self.day % 5 == 0:
            c.red("                        %s" % self.odd_sky[self.sky])
            self.player.luck += 1
        else:
            print("		             The sky looks", self.sky_event[random.choice(range(6))], "today.")
        c.red("\n_______________________________________________________________________")
        c.purple("\n\nHealth: %d" % self.player.health)
        c.purple("                       		Junk: %d" % self.player.junk)
        time.sleep(1)
        c.yellow("\n\nLuck: %d" % self.player.luck) 
        c.yellow("                    	      		Gold: %d" % self.player.gold)
        c.red("\n_______________________________________________________________________")
        print()
        print()
        time.sleep(1)
        print("1: Explore")
        print("2: Rest")
        print("3: Shop")
        print("4: Quit")
        print("H: Help")
        print()
