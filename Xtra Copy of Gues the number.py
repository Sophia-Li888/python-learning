NAME = input("Hi! What is your name?")
print("Hi,",NAME,"! You will be guessing from 1 to 10.")
randomRangeLimit = 10
import random
number = random.randrange(1, randomRangeLimit)
game = "start"
level = 1
attempts = []
attemptsLimit = 5
AGAIN = "yes"

while AGAIN =="yes":

    while game == "start":

        if len(attempts) == attemptsLimit:
            game = "end"
            losePlayAgain = input("""Game Ended :( Sorry...
Do you want to try again?""")  
            losePlayAgain = losePlayAgain.lower()
            if losePlayAgain == "yes":
                randomRangeLimit = 10
                print("It's OK that you lost last time... You can try your hardest this time... :) Now, in level 1 again! :(, you will have to guess numbers from 1 to",randomRangeLimit,"! Beware, and have fun :)")
                import random
                number = random.randrange(1, randomRangeLimit)
                game = "start"
                level = 1
                attempts = []
                attemptsLimit = 5
                break
            else:
                game = "end"
                AGAIN = "no"
                break 

        userAttempt = input("Guess what number I am!")
        userAttempt = int(userAttempt)
    
        if userAttempt == number:
            level = level + 1
            print("Correct! Horray for you! (you are currently on level",level,"!)")
            winPlayAgain = input("Do you want to play again?")
            winPlayAgain = winPlayAgain.lower()
            if winPlayAgain == "yes":
                randomRangeLimit = randomRangeLimit + 10
                attemptsLimit = attemptsLimit + 1
                print("What a brave soul! In the next level, you will have to guess numbers from 1 to",randomRangeLimit, "and you will have",attemptsLimit,"tries! Beware, and have fun :)")
                import random
                number = random.randrange(1, randomRangeLimit)
                game = "start"
                attempts = []
                break
            else:
                game = "end"
                AGAIN = "no"
                break 

        elif userAttempt > number:
                attempts.append(userAttempt)
                print("Too high! These are your attempts:", attempts)

        else:
            attempts.append(userAttempt)
            print("Too low! These are your attempts:", attempts)          

        
print("BYE", NAME, "!")

randomRangeLimit = 10
import random
number = random.randrange(1, randomRangeLimit)
game = "start"
level = 1
attempts = []
attemptsLimit = 5
AGAIN = "yes"     