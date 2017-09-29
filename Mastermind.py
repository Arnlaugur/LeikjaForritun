import random
Limit = 0
Condition = 0
CompNumbers = [ random.randint(1,7), random.randint(1,7), random.randint(1,7), random.randint(1,7) ]
while Condition == 0:

    Pos1 = 0
    Pos2 = 0
    print "Take a guess, Example: 3,4,5,6"
    Userguess = input()
    Count = 0
    while Count < 4:
        if Userguess[Count] == CompNumbers[Count]:
            Pos1 += 1
        if Userguess[Count] == CompNumbers[0] and Count != 0:
            Pos2 += 1
        if Userguess[Count] == CompNumbers[1] and Count != 1:
            Pos2 += 1
        if Userguess[Count] == CompNumbers[2] and Count != 2:
            Pos2 += 1
        if Userguess[Count] == CompNumbers[3] and Count != 3:
            Pos2 += 1
        Count += 1
    if Pos1 == 4:
        print "You won, CompNum:"
        print CompNumbers
        Condition = 1
    else:
        print "You had " + str(Pos2) + " numbers right but in the wrong position"
        print "You had " + str(Pos1) + " numbers right"
        Limit += 1
    if  Limit > 8:
        print "You Lose"