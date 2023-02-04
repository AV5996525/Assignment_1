
from tabulate import tabulate

din1 = 25.50
din2 = 29.50
hst = .13
studIc = .10
disC = 100
disC1 = 500
firHead = ["QTY", "ITEM"]
msg = "Thanks for choosing Arnold's Amazing Eats II"
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
            sumT1 = (quanDin1 * din1)
            flag1 = False
            while True:
                
                conf1 = str(input("Are you sure you would like to order: \n" + str(quanDin1) + "\tX Prime rib Dinners:" + "\n[Yes or No]: "))
                if conf1 == 'y' or conf1 == 'Y' :                              
                    flag1 = True
                    

                    if  sumT1 > disC1 :
                         
                            print("15 % discount activated!")
                            Ribdiscnt15 = (.15*sumT1)
                            Ribgrand15 = (sumT1 - Ribdiscnt15)
                            print(str(Ribgrand15))         
                            print("Your sub total is: " + "$" + str(sumT1) + "\nYour 15% discount savings are: " + "$" + str(Ribdiscnt15))
                            print(str(firHead) + "\n" + str(quanDin1) + " X\t" + "Prime rib dinner\n" + "-----------------------------------\n" + "Your grand total is : " + "$" + str(Ribgrand15) + "\n-----------------------------------\n")
                            flag2 = False
                            while True:
                                   
                                   stud = str(input("Are you a student? "))
                                   if stud == 'y' or stud == 'Y' :
                                          
                                          print("Enjoy a student discount")
                                          RibgrandT15S = (Ribgrand15 * studIc)
                                          RibgrandT15St = (Ribgrand15 - RibgrandT15S)  
                                          Ribtax15 = (hst*RibgrandT15St)
                                          Ribtax15F = Ribtax15 + RibgrandT15St
                                          print(*res, sep = ' ')
                                          print(tabulate([['Prime Rib dinner', quanDin1, din1, sumT1], ["10 % Student savings", '', '', '- $'+ str(RibgrandT15S)],['','','sub total', "$"+str(RibgrandT15St)],['','',"Tax 13%", "$"+str(Ribtax15)],['','',"Total", "$"+str(Ribtax15F)]], headers = ["Order", "Item Amnt", "Item Price","Total"]))
                                          print(msg)
                                          flag2 = False
                                          
                                          
                                          while True:
                                                exit
                                                 
                                           
                                           
                                          
                                   

                            
                                   elif stud == 'n' or stud == 'N' :
                                          flag2 = True
                                          print("No student discount applicable.")
                                          RibgrandT15Stnd = Ribgrand15
                                          RibgrandT15Stndtx = Ribgrand15 * hst
                                          RibgrandT15Stndtxf = RibgrandT15Stnd + RibgrandT15Stndtx
                                          print(*res, sep = ' ')
                                          print(tabulate([['Prime Rib dinner', quanDin1, din1, sumT1], [ "", "", "", ""], ['','','sub total', "$"+str(RibgrandT15Stnd)], ['','',"Tax 13%", "$"+str(RibgrandT15Stndtx)],['','',"Total", "$"+str(RibgrandT15Stndtxf)]], headers = ["Order", "Item Amnt", "Item Price","Total"]))  
                                          print(msg)
                                          while True:
                                                exit
                                           
                                   elif stud != 'y' or 'Y' or 'n' or 'N' :

                                          print("Incorrect response")    
                                          continue       
                           
                                         
                                   
                                           
                                      
                    elif sumT1 >= disC :        
                            print("Current selection: ")
                            Ribdiscnt10 = (.10*sumT1)
                            RibgrandT10 = (sumT1 - Ribdiscnt10)
                            print("Your sub total is: " + "$" + str(sumT1) + "\nYour 10% discount savings are: " + "$" + str(Ribdiscnt10))
                            print(str(firHead) + "\n" + str(quanDin1) + " X\t" + "Prime rib dinner\n" + "-----------------------------------\n" + "Your grand total is : " + "$" + str(RibgrandT10) + "\n-----------------------------------\n")
                            
                            while True:
                                   flag3 = False
                                   stud = str(input("Are you a student? "))
                                   if stud == 'y' or stud == 'Y' :
                                          flag3 = True
                                          print("Enjoy a student discount")
                                          RibgrandT10S = (RibgrandT10 * studIc)
                                          RibgrandT10St = (RibgrandT10 - RibgrandT10S)  
                                          Ribtax10 = (hst*RibgrandT10St)
                                          Ribtax10F = Ribtax10 + RibgrandT10St
                                         
                                          print(*res, sep = ' ')
                                          print(tabulate([['Prime Rib dinner', quanDin1, din1, sumT1], ["10 % Student savings", '', '', '- $'+ str(RibgrandT10S)],['','','sub total', "$"+str(RibgrandT10St)],['','',"Tax 13%", "$"+str(Ribtax10)],['','',"Total", "$"+str(Ribtax10F)]], headers = ["Order", "Item Amnt", "Item Price","Total"]))
                                          continue
                                   if stud == 'n' or stud == 'N' :
                                          flag3 = True
                                          print("No student discount applicable.")
                                          RibgrandT10Stnd = RibgrandT10
                                          RibgrandT10Stndtx = RibgrandT10 * hst
                                          RibgrandT10Stndtxf = RibgrandT10Stndtx + RibgrandT10
                                          print(*res, sep = ' ')
                                          print(tabulate([['Prime Rib dinner', quanDin1, din1, sumT1], [ "", "", "", ""], ['','','sub total', "$"+str(RibgrandT10Stnd)], ['','',"Tax 13%", "$"+str(RibgrandT10Stndtx)],['','',"Total", "$"+str(RibgrandT10Stndtxf)]], headers = ["Order", "Item Amnt", "Item Price","Total"]))  
                                          continue 
                                   if stud != 'y' or 'Y' or 'n' or 'N' :
                                          print("Incorrect response")
                                          continue
                    elif sumT1 < disC :
                     
                            print("5% discount granted!")
                            Ribdiscnt5 = (.05*sumT1)
                            Ribgrand5 = (sumT1 - Ribdiscnt5)
                            
                            print("Your sub total is: " + "$" + str(sumT1) + "\nYour 5% discount savings are: " + "$" + str(Ribdiscnt5))
                            print(str(firHead) + "\n" + str(quanDin1) + " X\t" + "Prime rib dinner\n" + "-----------------------------------\n" + "Your grand total is : " + "$" + str(Ribgrand5) + "\n-----------------------------------\n")
                                 
                            while True:
                                   flag4 = False
                                   stud = str(input("Are you a student? "))
                                   if stud == 'y' or stud == 'Y' :
                                          flag4 = True
                                          print("Enjoy a student discount")
                                          RibgrandT5S = (Ribgrand5 * studIc)
                                          RibgrandT5St = (Ribgrand5 - RibgrandT5S)  
                                          Ribtax5 = (hst*RibgrandT5St)
                                          Ribtax5F = Ribtax5 + RibgrandT5St
                                          
                                          print(*res, sep = ' ')
                                          print(tabulate([['Prime Rib dinner', quanDin1, din1, sumT1], ["10 % Student savings", '', '', '- $'+ str(RibgrandT5S)],['','','sub total', "$"+str(RibgrandT5St)],['','',"Tax 13%", "$"+str(Ribtax5)],['','',"Total", "$"+str(Ribtax5F)]], headers = ["Order", "Item Amnt", "Item Price","Total"]))
                                          break
                                   if stud == 'n' or stud == 'N' :
                                          flag4 = True
                                          print("No student discount applicable.")
                                          RibgrandT5Stnd = Ribgrand5
                                          RibgrandT5Stndtx = RibgrandT5Stnd * hst
                                          RibgrandT5Stndtxf = RibgrandT5Stndtx + RibgrandT5Stnd
                                          print(*res, sep = ' ')
                                          print(tabulate([['Prime Rib dinner', quanDin1, din1, sumT1], [ "", "", "", ""], ['','','sub total', "$"+str(RibgrandT5Stnd)], ['','',"Tax 13%", "$"+str(RibgrandT5Stndtx)],['','',"Total", "$"+str(RibgrandT5Stndtxf)]], headers = ["Order", "Item Amnt", "Item Price","Total"]))  
                                          break
                                   if stud != 'y' or 'Y' or 'n' or 'N' :
                                          print("Incorrect response1")                   

                
                
                   
                                                               
                if conf1 == 'n' or conf1 == 'N' :
                       flag1 = True 
                       continue    
                if conf1 != 'y' or 'Y' or 'n' or 'N':
                       print("Invalid entry") 
                       continue
                       flag1 = True
                       
                
                            
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
            
                
            
elif dinChoice.isalpha() :
        print("Invalid response, please user numbers, not letters.")
else:
            print("Invalid choice, please select choice 1 or 2.")       





