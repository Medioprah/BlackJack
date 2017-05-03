import random
import tkinter
top = tkinter.Tk()
# Code to add widgets will go here...
top.mainloop()

gang = 0
opps = 0
 
fin = False
 
while fin == False:

    cardlist = [1,1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]

    card = cardlist[random.randint(0,51)]
    card2 = cardlist[random.randint(0,51)]
    card3 = cardlist[random.randint(0,51)]
    card4 = cardlist[random.randint(0,51)]
   
    gang = card + card2
    opps = card3 + card4
    chips = 100   
    

    firstornah = 1
    while fin == False:
       
        if firstornah == 1:
            print('u got ' + str(chips) + " chips.")

            wager = int(input('how much u tryna bet? '))

            chips = chips - wager

        if firstornah == 1:
            print("u sittin at " + str(gang))
       
        firstornah = firstornah + 1
   
        hitornah = input('u tryna hit? ')
       
        if hitornah != "sure"   and hitornah != "nah":
            print("what was that? i couldn't hear you fam")
       
        if hitornah == "sure":
            newcard = cardlist[random.randint(0,51)]
            gang = gang + newcard
            print("u now sittin at " + str(gang))
           
        if gang > 21:
            firstornah = 1
            bust = input("u bust foo. u lost " + str(wager) + " chips. u tryna play again? " )
            gang = cardlist[random.randint(0,51)] + cardlist[random.randint(0,51)]
            opps = cardlist[random.randint(0,51)] + cardlist[random.randint(0,51)]
            if bust == "nah":
                fin = True
           
        if hitornah == "nah":
           
            fuck = False
           
            firstornah = 1
           
            while opps <= 17:
                newopps = cardlist[random.randint(0,51)]
                opps = opps + newopps
               
            if opps > 21:
                oppsbust = input("yo opps bust at " + str(opps) + ". u brought respek to yo hood. u gained " + str(wager * 2) + ". u tryna play again? " )
                gang = cardlist[random.randint(0,51)] + cardlist[random.randint(0,51)]
                opps = cardlist[random.randint(0,51)] + cardlist[random.randint(0,51)]
                chips = chips + (wager * 2)
                fuck = True
                if oppsbust == "nah":
                    fin = True
                   
            if gang > opps and fuck != True:
                print('yo opps was at ' + str(opps))
                oppslost = input("u beat yo opps. u put respek on yo name. u gained " + str(wager * 2) + ". u tryna play again? " )
                gang = cardlist[random.randint(0,51)] + cardlist[random.randint(0,51)]
                opps = cardlist[random.randint(0,51)] + cardlist[random.randint(0,51)]
                chips = chips + (wager * 2)
                if oppslost == "nah":
                    fin = True
                   
            if opps > gang and opps <= 21:
                print("yo opps was at " + str(opps))
                oppswon = input("yo opps beat u. u lost yo wager of " + str(wager) + ". u tryna play again? " )
                gang = cardlist[random.randint(0,51)] + cardlist[random.randint(0,51)]
                opps = cardlist[random.randint(0,51)] + cardlist[random.randint(0,51)]
                if oppswon == "nah":
                    fin = True
           
            if opps == gang and fuck != True:
                tie = input("u and yo opps tied. u got your wager of " + str(wager) + " back. u tryna play again? " )
                gang = cardlist[random.randint(0,51)] + cardlist[random.randint(0,51)]
                opps = cardlist[random.randint(0,51)] + cardlist[random.randint(0,51)]
                chips = chips + wager
                if tie == "nah":
                    fin = True