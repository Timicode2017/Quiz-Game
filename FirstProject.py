print("Welcome to my computer quiz! \n")

playing = input("Do you want to play? ")

if playing != "yes" and playing != "Yes":  # we could use upper() case "YES" or lower() case "yes" also can be used.
    quit("Game over the character didn't want to play. \n")

print("Okay then lets play :)")
scroe = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    scroe += 1
    print("Correct!")
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    scroe += 1
    print("Correct!")
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    scroe += 1
    print("Correct!")
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    scroe += 1
    print("Correct!")
else:
    print("Incorrect!")

print("You got " + str(scroe) + " questions correct! ")