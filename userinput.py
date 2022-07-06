import phonenumbers
from phonenumbers import timezone
# This is used to accept the user inputs and will be eventually stored in a database.
# Save name and phone number once. It'll be used for notifications for the user.
# Inputs needed: Name, Phone number, email(optional), food items bought.
# Automatically note the dates for the food items input. 

#Notifood UI 
 

name = input("Enter your full name: ")

# Program to convert input to
# phonenumber format
  
# Parsing String to Phone number
# Phone number format: (+Countrycode)xxxxxxxxxx
phoneNumber = phonenumbers.parse("+919876543210")
# Pass the parsed phone number in below function
timeZone = timezone.time_zones_for_number(phoneNumber)
# This will print the phone number and 
# it's basic details.
print(phoneNumber)
print(timeZone)

#store data for fruits
Fruits = []
print("Enter the name of the fruit: ")
while True:
    Fruit = str(input())
    Fruits.append(Fruit)
    if Fruit == "":
        break
del Fruits[-1]
print(Fruits)

#store data for vegetables
Vegetables = [] 
print("Enter the name of the vegetable: ")
while True:
    Vegetable = str(input())
    Vegetables.append(Vegetable)
    if Vegetable == "":
        break
del Vegetables[-1]
print(Vegetables)

#store data for canned goods
Canned_Goods = []
print("Enter the name of the canned good: ")
while True:
    Canned_Good = str(input())
    Canned_Goods.append(Canned_Good)
    if Canned_Good == "":
        break
del Canned_Goods[-1]
print(Canned_Goods)

#store data for dairy
Dairy = []
print("Enter the name of the Dairy: ")
while True:
    dairy = str(input())
    Dairy.append(dairy)
    if dairy == "":
        break
del Dairy[-1]
print(Dairy)

#store data for meat
Meat = []
print("Enter the name of the meat: ")
while True:
    meat = str(input())
    Meat.append(meat)
    if meat == "":
        break
del Meat[-1]
print(Meat)

#store data for Fish_and_Seafood
Fish_and_Seafood = []
print("Enter the name of the fish and seafood: ")
while True:
    fish_and_seafood = str(input())
    Fish_and_Seafood.append(fish_and_seafood)
    if fish_and_seafood == "":
        break
del Fish_and_Seafood[-1]
print(Fish_and_Seafood)

#store data for deli
Deli = []
print("Enter the name of the deli: ")
while True:
    deli = str(input())
    Deli.append(deli)
    if deli == "":
        break
del Deli[-1]
print(Deli)

#store data for condiments and spices
Condiments_and_Spices = []
print("Enter the name of the condiment or spice: ")
while True:
    condiment = str(input())
    Condiments_and_Spices.append(condiment)
    if condiment == "":
        break
del Condiments_and_Spices[-1]
print(Condiments_and_Spices)

#store data for snacks
Snacks = []
print("Enter the name of the snack: ")
while True:
    snacks = str(input())
    Snacks.append(snacks)
    if snacks == "":
        break
del Snacks[-1]
print(Snacks)

#store data for Bread and Bakery
Bread_and_Bakery = []
print("Enter the name of the bread or baked item: ")
while True:
    bread = str(input())
    Bread_and_Bakery.append(bread)
    if bread == "":
        break
del Bread_and_Bakery[-1]
print(Bread_and_Bakery)

#store data for Beverages
Beverages = []
print("Enter the name of the beverage: ")
while True:
    beverage = str(input())
    Beverages.append(beverage)
    if beverage == "":
        break
del Beverages[-1]
print(Beverages)

#store data for pasta, rice or cereal
Pasta_Rice_Cereal = []
print("Enter the name of the pasta, rice, or cereal: ")
while True:
    pasta = str(input())
    Pasta_Rice_Cereal.append(pasta)
    if pasta == "":
        break
del Pasta_Rice_Cereal[-1]
print(Pasta_Rice_Cereal)

#store data for baking items
Baking = []
print("Enter the name of the baking item: ")
while True:
    baking = str(input())
    Baking.append(baking)
    if baking == "":
        break
del Baking[-1]
print(Baking)

#store data for frozen goods
Frozen_Foods = []
print("Enter the name of the frozen foods: ")
while True:
    frozen_food = str(input())
    Frozen_Foods.append(frozen_food)
    if frozen_food == "":
        break
del Frozen_Foods[-1]
print(Frozen_Foods)