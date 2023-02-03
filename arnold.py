
from tabulate import tabulate

din1 = 25.50
din2 = 29.50
hst = .13
studIc = .10
disC = 100
disC1 = 500
firHead = ["QTY", "ITEM"]

print("Welcome to Arnold's Amazing Eats II \nHome of the best food in Waterloo! \nThis app will simply help you make an order!")
firName = input("Enter your first name: ").strip()
lasName = input("Enter your last name: ").strip()
city = input("Enter your current city: ").strip()
prov = input("Enter your province: ").strip()
pos = input("Enter your postal code: ").strip()
spcInst = input("Enter any special delivery instructions: ")
phNum = input("Enter your phone number: ").strip()

receipt1 = [firName+" ", city+" ", phNum+" ", spcInst]
receipt2 = [lasName+" ", prov+" ", pos+" ", '']
res = "\n".join("{}{}".format(x,y) for x,y in zip(receipt1, receipt2))



dinChoice = str(input("Our daily specials are: \n\t1.Prime Rib Dinner - $25.50 \n\t2.Turkey Dinner - $29.50\n"))

if dinChoice == '1' or dinChoice == '2'  :
        if dinChoice == '1' :
            quanDin1 = float(input("How many of the Prime rib dinners would you like: "))             
            while True:
                conf1 = str(input("Are you sure you would like to order: \n" + str(quanDin1) + "\tX Prime rib Dinners:" + "\n[Yes or No]: "))
                if conf1 == 'y' or conf1 == 'Y' :                              
                    sumT1 = (quanDin1 * din1)
                    
                    if sumT1 >= disC :        
                            print("Current selection: ")
                            Ribdiscnt10 = (.10*sumT1)
                            RibgrandT10 = (sumT1 - Ribdiscnt10)
                            print("Your sub total is: " + "$" + str(sumT1) + "\nYour 10% discount savings are: " + "$" + str(Ribdiscnt10))
                            print(str(firHead) + "\n" + str(quanDin1) + " X\t" + "Prime rib dinner\n" + "-----------------------------------\n" + "Your grand total is : " + "$" + str(RibgrandT10) + "\n-----------------------------------\n")
                            while True:
                                   stud = str(input("Are you a student? "))
                                   if stud == 'y' or stud == 'Y' :
                                          print("Enjoy a student discount")
                                          RibgrandT10S = (RibgrandT10 * studIc)
                                          RibgrandT10St = (RibgrandT10 - RibgrandT10S)  
                                          Ribtax10 = (hst*RibgrandT10St)
                                          Ribtax10F = Ribtax10 + RibgrandT10St
                                          recRib10a = [ "Order", "Item", "Item","Total"]
                                          recRib10a2 = [ '', "Amount", "Price",'']
                                          genBord = ["--------", "--------","--------","---------"]
                                          recRib10b = ["Prime rib dinner", str(quanDin1), str(din1), str(sumT1)]
                                          print(*res, sep = ' ')
                                          print(' '.join(recRib10a))
                                          print(' '.join(recRib10a2))
                                          print(' '.join(genBord))
                                          print(' '.join(recRib10b))

                                          break
                                   if stud == 'n' or stud == 'N' :
                                          print("No student discount applicable.")

                                          break  
                                   if stud != 'y' or 'Y' or 'n' or 'N' :
                                          print("Incorrect response")
                                              
                    if sumT1 < disC :
                            print("5% discount granted!")
                            Ribdiscnt5 = (.05*sumT1)
                            Ribgrand5 = (sumT1 - Ribdiscnt5)
                            print(str(Ribgrand5))
                    if sumT1 > disC1 :
                            print("15 % discount activated!")
                            Ribdiscnt15 = (.15*sumT1)
                            Ribgrand15 = (sumT1 - Ribdiscnt15)
                            print(str(Ribgrand15))         
                            
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





