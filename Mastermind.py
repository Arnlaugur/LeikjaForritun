import random

Limit = 0 #Turn Limit
Condition = 0 #Win condition tracker
CompNumbers = [ random.randint(1,7), random.randint(1,7), random.randint(1,7), random.randint(1,7) ] #4 random numbers for the player to guess

while Condition == 0: #Runs aslong as the player doesn't win or lose

    Pos1 = 0 #Keeps track of the right number in the right place
    Pos2 = 0 #Keeps track of the right number int he wrong place

    print "Take a guess, Example: 3,4,5,6"
    Userguess = input() #Takes in the users guess

    Count = 0 #Keeps a count
    while Count < 4: #Runs four times
        if Userguess[Count] == CompNumbers[Count]: #Checks if the number is in the right position
            Pos1 += 1
        elif Userguess[Count] == CompNumbers[0] and Count != 0: #Next four if sentences check if its the right number in wrong position
            Pos2 += 1
        elif Userguess[Count] == CompNumbers[1] and Count != 1:
            Pos2 += 1
        elif Userguess[Count] == CompNumbers[2] and Count != 2:
            Pos2 += 1
        elif Userguess[Count] == CompNumbers[3] and Count != 3:
            Pos2 += 1
        Count += 1 #Adds to count

    if Pos1 == 4: #If all numbers are correct
        print "You won, CompNum:"
        print CompNumbers #Shows the correct number (For debugging)
        Condition = 1 #Win condition filled

    else:
        print "You had " + str(Pos2) + " numbers right but in the wrong position" #Tells the user how many numbers he got correct but in the wrong spot
        print "You had " + str(Pos1) + " numbers right" #Tells the user how many numbers he got completely right
        Limit += 1

    if  Limit > 8: #If the turn limit is reached
        print "You Lose, Correct answer: " + str(CompNumbers) #User loses
        Condition = 1

