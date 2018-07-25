#!/usr/bin/python
#   @creator = Dobinoo
#   @date = 2.12.2017
from termcolor import colored #for colored output
import sys #for sys.exit()
import time #for using sleeping


print "\033c" #to clear the terminal window for the first start

# this is a temporary solution all this choices should be
#stand alone functions , ill update in v2

#main program loop
while True:
    print colored("What is your choice: ","blue")
    choice = raw_input("Choice: ")

#open file
    if(choice == "o"):
        print colored("\nEnter the path for file: ","blue")
        path_to_file = raw_input()
        file = open(path_to_file,"r+")
        time.sleep(3)
        print colored("File opened succesfully\n","green")

#print colored file
    elif(choice == "p"):

        #just a checking flag
        flag = True

        if(file.closed):
            print colored("\nERROR !! \nThere is no file opened\n","red")
            flag = False

        if(flag):
            color = raw_input("Choose color (red,blue,cyan,magenta,yellow): ")
            print colored("\nNow we print selected file in your color :)","blue")
            file.seek(0,0) # always set reading pointer to start
            text = file.read() #no input so from begin to end
            time.sleep(5)

            if(color == ""):
                print("\n+++++++++++++")
                print(text)
                print("+++++++++++++\n")
            else:
                print("\n+++++++++++++")
                print colored(text,color)
                print("+++++++++++++\n")

#i have to delete color variable because if you use same choice
#there is no output
            del color

#close file
    elif(choice == "c"):
        #just a checking flag
        flag = True

        if (file.closed):
            print colored("\nERROR!!!\nThere is no file opened\n","red")
            flag = False

        if(flag):
            print colored("\nClosing opened file","blue")
            file.close()
            time.sleep(3)
            print colored("File " + file.name + "","blue")
            print colored("Closed SUCCESFULLY\n","green")
            del file

#info about file
    elif(choice == "i"):
        flag = True

        if (file.closed):
            print colored("\nERROR!!!\nThere is no file opened\n","red")
            flag = False

        if(flag):
            print colored("\nInfo: ","blue")
            time.sleep(3)
            print "File name: ",file.name
            print "File closed: ",file.closed
            print "Opened in mode: ",file.mode
            print "\n"

#quit program
    elif(choice == "q"):
        time.sleep(2)
        if file.closed == False:
            print colored("\nYou didnt closed your file","red")
            print colored("File name: " + file.name + "","red")
            print colored("File closed: False","red")
            time.sleep(1)
            print colored("WAIT !","yellow")
            time.sleep(1)
            print colored("Ill just do it myself ","yellow")
            file.close()
            time.sleep(5)
            print colored("File " + file.name + " CLOSED SUCCESFULLY\n","green")
            del file

        time.sleep(3)
        print "\n\n\n"
        print colored("USE THIS WISELY YOUNG PADAWAN","yellow")
        print colored("Application closed","red")
        sys.exit(0)


    #just a clearing terminal window
    elif(choice == "clear"):
        print "\033c"

#help
    else:
        time.sleep(2)
        print colored("WRONG CHOICE !\n","red")
        print colored("To enter the MATRIX choose from this choices:\n","blue")
        print colored("To open file:                 \"o\"","blue")
        print colored("To close file:                \"c\"","blue")
        print colored("To get info about file:       \"i\"","blue")
        print colored("To print selected file:       \"p\"","blue")
        print colored("To clear terminal window:     \"clear\"","blue")
        print colored("To close this program:        \"q\" \n","blue")


    #just a escape line
