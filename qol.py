#!/usr/bin/python
import time
from termcolor import colored

print colored("What is the answer for the ultimate question of Life, the Universe and Everything? ","blue")
answer = raw_input("Answer: ")

time.sleep(5)

if answer == "42" :
    print colored("\nCORRECT!","green")
else:
    print colored("\nWRONG!","red")
