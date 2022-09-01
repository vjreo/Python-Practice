name = input("Insert your name: ")
greeting = "\nHello " + name + "! Welcome to the Band Name Generator. We will ask a series of questions which will allow us to generate a cool band name for you. Please follow the prompts below."
print(greeting)

city = input("What city did you grow up in? \n")

pet = input("What is the name of a pet you currently own (or have owned)? \n")

band_name = city + " " + pet
print("Your band name could be: " + band_name)