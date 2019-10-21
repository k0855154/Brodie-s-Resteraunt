import math
speedLimit = int(input("What is the speed limit? "))
demeritPoints = 0
while demeritPoints < 12: 
    currentSpeed = int(input("How fast are you going? "))
    aboveFive = (currentSpeed - speedLimit)/5
    aboveFive = math.ceil(aboveFive)
    if aboveFive > 0:
        demeritPoints = demeritPoints + aboveFive
        if demeritPoints >= 12:
            print("You idiot you got your license suspened")
            break
        else:
            print("Slow Down")  
            pass

    else:
        print("Good boy")


        