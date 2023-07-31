# Business Requirement
## Create a band name generator app, the app should have the following functions:
### Create a greeting for your program.
### Ask the user for the city that the grew up in.
### Ask the user for the name of a pet.
### Combine the name of their city and pet and show them their band name.
### Make sure the input cursor shows on a new line.


print("Welcome to Band Name Generator App")

city = input("Enter the name of the city where you grew up:\n ")
pet = input("Enter your favorite pet name:\n ")
print( "Your band name is " + city + " " + pet)
