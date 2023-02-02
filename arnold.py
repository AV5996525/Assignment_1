din1 = 25.50
din2 = 29.50
disC = 100
disC1 = 500
print("Welcome to Arnold's Amazing Eats II \nHome of the best food in Waterloo! \nThis app will simply help you make an order!")
firName = input("Enter your first name: ").strip()
lasName = input("Enter your last name: ").strip()
city = input("Enter your current city: ").strip()
prov = input("Enter your province: ").strip()
pos = input("Enter your postal code: ").strip()
spcInst = input("Enter any special delivery instructions: ")
phNum = input("Enter your phone number: ").strip()
dinChoice = str(input("Our daily specials are: \n\t1.Prime Rib Dinner - $25.50 \n\t2.Turkey Dinner - $29.50"))

if dinChoice == '1' or dinChoice == '2'  :
        if dinChoice == '1' :
            quanDin1 = float(input("How many of the Prime rib dinners would you like: "))             
            while True:
                conf1 = str(input("Are you sure you would like to order: \n" + str(quanDin1) + "\tX Prime rib Dinners:" + "\n[Yes or No]: "))
                if conf1 == 'y' or conf1 == 'Y' :                              
                    sumT1 = (quanDin1 * din1)
                    
                    if sumT1 >= disC :        
                            print("10% discount granted!")
                    if sumT1 < disC :
                            print("5% discount granted!")
                    if sumT1 > disC1 :
                            print("15 % discount activated!")         
                            
                    break
                                                           
                if conf1 == 'n' or conf1 == 'N' :
                        break    
                elif conf1 != 'y' or 'Y' or 'n' or 'N':
                       print("Invalid entry")         
        elif dinChoice == '2':
            quanDin2 = float(input("How many of the turkey dinners would you like: "))
            while True:
                conf2 = input("Are you sure you would like to order: \n" + str(quanDin2) + "\tX  Turkey Dinners:" + "\n[Yes or No]: ")
                if conf2 == 'y' or conf2 == 'Y' :
                      sumT2 = (quanDin2 * din2)
                      if sumT2 >= disC :        
                            print("10% discount granted!")
                      if sumT2 < disC :
                            print("5% discount granted!")
                      if sumT2 > disC1 :
                            print("15 % discount activated!")   
                      break     
                elif conf2 == 'n' or conf2 == 'N' :
                       break    
                elif conf2 != 'y' or 'Y' or 'n' or 'N':
                       print("Invalid entry")                
            else:
                   print("ok")
elif dinChoice.isalpha() :
        print("Invalid response, please user numbers, not letters.")
else:
            print("Invalid choice, please select choice 1 or 2.")       





