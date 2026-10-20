print("Welcome to the Hogwarts Sorting Hat")

trait = input("What best describes you? ")

if trait.lower() == "brave":
    print("You are sorted into Gryffindor!")
    
elif trait.lower() == "intelligent":
    print("You are sorted into Ravenclaw!")
    
elif trait.lower() == "loyal":
    print("You are sorted into Hufflepuff!")

elif trait.lower() == "ambitious":
    print("You are sorted into Slytherin!")
    
elif trait.lower() == "adventurous":
    print("You deserve the marauders map!")
    
else:
    print("The Sorting Hat is confused.")
