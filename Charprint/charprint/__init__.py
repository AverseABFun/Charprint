__version__ = '1.3.1'
from termcolor import colored
import cursor
import sys
import os
from time import sleep
def main():
    def charprint(string, color, cursorused=True):
        if cursorused == True:
            cursor.show()
        for i in string:
            sys.stdout.write(colored(i, color=color))
            sys.stdout.flush()
        sys.stdout.write("\n")
        sys.stdout.flush()
        if cursorused == True:
            cursor.hide()
    def charinput(string, color, cursorused=True):
        charprint(string, color, cursorused=cursorused)
        return input("")
    def blanket():
        os.system("clear")
        for i in range(3):
            for f in range(3):
                sys.stdout.write("#")
                sys.stdout.flush()
            sys.stdout.write("\n")
            sys.stdout.flush()
        sleep(3)
        os.system("clear")