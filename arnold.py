print("Welcome to Arnold's Amazing Eats II \nHome of the best food in Waterloo! \nThis app will simply help you make an order!")
firName = input("Enter your first name: ").strip()
lasName = input("Enter your last name: ").strip()
city = input("Enter your current city: ").strip()
prov = input("Enter your province: ").strip()
pos = input("Enter your postal code: ").strip()
spcInst = input("Enter any special delivery instructions: ")
phNum = input("Enter your phone number: ").strip()
dinChoice = input("Our daily specials are: \n\t1.Prime rib dinner \n\t2.Turkey Dinner").strip()

if dinChoice.isdigit() == True :
    if dinChoice == 1 :
        print("How many of the Prime rib dinners would you like: ")
    elif dinChoice == 2:
        print("How many of the Turkey dinners would you like: ")
    elif dinChoice != 1 or dinChoice != 2 :
        print("Invalid choice, please select choice 1 or 2.")        
if dinChoice.isalpha() :
    print("Invalid response, please user numbers, not letters.")
else:
    pass



