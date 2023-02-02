print("Welcome to Arnold's Amazing Eats II \nHome of the best food in Waterloo! \nThis app will simply help you make an order!")
firName = input("Enter your first name: ").strip()
lasName = input("Enter your last name: ").strip()
city = input("Enter your current city: ").strip()
prov = input("Enter your province: ").strip()
pos = input("Enter your postal code: ").strip()
spcInst = input("Enter any special delivery instructions: ")
phNum = input("Enter your phone number: ").strip()
dinChoice = str(input("Our daily specials are: \n\t1.Prime rib dinner \n\t2.Turkey Dinner"))

if dinChoice == '1' or dinChoice == '2'  :
        if dinChoice == '1' :
            quanDin1 = float(input("How many of the Prime rib dinners would you like: "))
             
            while True:
            
                conf1 = str(input("Are you sure you would like to order: \n" + str(quanDin1) + "\tX Prime rib Dinners:" + "\n[Yes or No]: "))
                if conf1 == 'y' :
                       break       
                             
            else:
                   print("ok")            
        elif dinChoice == '2':
            quanDin2 = float(input("How many of the turkey dinners would you like: "))
            conf2 = input("Are you sure you would like to order: \n" + str(quanDin2) + "\tX  Turkey Dinners:" + "\n[Yes or No]: ").strip()
             
elif dinChoice.isalpha() :
        print("Invalid response, please user numbers, not letters.")
else:
            print("Invalid choice, please select choice 1 or 2.")       





