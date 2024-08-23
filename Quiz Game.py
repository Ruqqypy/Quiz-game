print("Welcome to my Computer quiz!")
Playing = input("Do you want to play? ")
if Playing != "yes":
    quit()
print("Okay! Let's play ")
Score = 0


Answer = input("What does CPU stand for? ")
if Answer == "Central Processing Unit":
    print("Correct!")
    Score +=1
else: 
    print("Incorrect!")
    

Answer = input("What does GPU stand for? ")
if Answer.lower() == "Graphic Processing Unit":
    print("Correct!")
    #Equivalent to Score = Score + 1
    Score +=1
else: 
    print("Incorrect!")
    

Answer = input("What does RAM stand for? ")
if Answer.upper() == "Random Access Memory":
    print("Correct!")
    Score +=1
else: 
    print("Incorrect!")


Answer = input("What does PSU stand for? ")
if Answer == "Power Supply":
    print("Correct!")
    Score +=1
else: 
    print("Incorrect!")
print("You got " + str(Score) + " questions correct!")
print("You got " + str((Score / 4) * 100) + "%.")
