import random
Appetizer = ("FrenchFood", "RainbowFood", "FishFood", "DogFood", "SquidFood")
random_num = random.randint(0,4)
Entre = ("Wow", "Yum", "Great", "Gross", "Ew", "Stop", "Fantabulous!")
random_num = random.randint(0,6)
Dessert = ("Cold", "Hot", "Lukewarm", "Soft", "Crunchy", "Sweet", "Salty", "Spicy")
random_num = random.randint(0,6)
print((Appetizer[random_num]) + (Entre[random_num]) + (Dessert[random_num]))
