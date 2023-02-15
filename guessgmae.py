import random
v1= random.randint(1,100)
print ("YOU ARE PLAYING GUESSING CORRECT NUMBER FROM 0 TO 100 ")
print ("YOU HAVE 5 CHANCE TO GUESS THE NUMBER")
i=0
for i in range (5):
    print (i+1," CHANCE")
    num=int(input())
    if v1>num :
        print ("THINK BIG VALUE ")
    elif v1<num:
        print ("THINK SMALL VALUE ")
    elif v1==num:
        print ("YOU GUESS THE VALUE")
        print ("YOU WON THE GAME")
        i=1
        break
print ("YOU LOOSE THE GAME")
print ("ENTERED VALUE IS",V1)
