class Pet:

    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age


class Dog(Pet):

    def speak(self):
        print(f"Hello Bark I'm a dog, but my name is {self.name}")

    def __str__(self):
        return f"Pet: Dog, Name: {self.name}, Breed:{self.breed}, Age:{self.age}"


class Cat(Pet):

    def speak(self):
        print(
            f"Meow Meow, Hello I'm a Cat OBVIOUSLY MEOW, and this cats name is {self.name}"
        )

    def __str__(self):
        return f"Pet: Cat, Name: {self.name}, Breed:{self.breed}, Age:{self.age}"

pets = []

while True:
    print("\n=======PET LOGGER=======")
    print("1.Add a pet")
    print("2.View pets")
    print("3.Exit")

    choice = input("Pick a choice 1-3: ")
    choice = int(choice)
    if choice == 1:
        petclass = input("Dog(1) or cat(2)?: ")
        petclass = int(petclass)
        if petclass == 1:

            name = input("What's the dog's name?: ")
            breed = input("What's the dog's breed?: ")
            age = input("How old is the dog?: ")
            age = int(age)
            pet = Dog(name, breed, age)
            pets.append(pet)
            
        elif petclass == 2:

            name = input("What's the cat's name?: ")
            breed = input("What's the cat's breed?: ")
            age = input("How old is the cat?: ")
            age = int(age)
            pet = Cat(name, breed, age)
            pets.append(pet)    
        else: 
            print("Choose between 2 numbers")
    elif choice == 2:
        for i in pets:
            print(f"{i}")
        input("Press to continue..")
        
    elif choice == 3:
        break
    else: print("Choose between 1-3")