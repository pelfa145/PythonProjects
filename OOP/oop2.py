class Dog:
    def __init__(self, name, age, breed):
        self.name=name
        self.age=age
        self.breed=breed

    def get_age(self):
        return self.age
    
pack=[]

while True:
    print("\n========DOG CREATOR MENU========")
    print("1. Create a new dog")
    print("2. View all dogs")
    print("3. Exit")

    choice = input("Choose an option 1-3: ")

    if choice=="1":
        namechoice=input("Whats the name of your dog: ")
        breedchoice=input("Whats the breed of your dog: ")
        agechoice=input("How old is your dog: ")
        
        dog=Dog(name=namechoice,age=agechoice,breed=breedchoice)

        pack.append(dog)
        print(dog.age)
        print(pack)
 
        