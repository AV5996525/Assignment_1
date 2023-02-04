#Name:          arnold.py
#Author:        AJ Varatharajan
#Date Created:  February 2, 2023
#Date Last Modified: February 4, 2023

#Purpose: 
#
#This program will accept user input to fill out fields regarding their personal information.
#The user will be able to select one of two items. With one item, but as many servings as desired.
#program will ask user to confirm their order and student status. It will prompt for an appropriate entry using y, Y, n, N only.
#If user does not confirm the order, they CAN re enter their selection.
#A receipt will be outputted once the user completes the order.


def resta ():                                                                 #defining this entire program as a function, for restarting the program if a certain condition like the customer wanting to restart their order.
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
                                          Ribdiscnt15 = (.15*sumT1)
                                          Ribgrand15 = (sumT1 - Ribdiscnt15)
                                                               
                                          print("Your sub total is: " + "$" + str(round(sumT1,2)) + "\nYour 15% discount savings are: " + "$" + str(round(Ribdiscnt15,2)))
                                          print(str(firHead) + "\n" + str(quanDin1) + " X\t" + "Prime rib dinner\n" + "-----------------------------------\n" + "Your grand total is : " + "$" + str(round(Ribgrand15,2)) + "\n-----------------------------------\n")
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
                                                        print(tabulate([['Prime Rib dinner', quanDin1, '$' + str(din1), '$' + str(round(sumT1,2))], ["10 % Student savings", '', '', '- $'+ str(round(RibgrandT15S,2))],['','','sub total', "$"+str(round(RibgrandT15St, 2))],['','',"Tax 13%", "$"+str(round(Ribtax15, 2))],['','',"Total", "$"+str(round(Ribtax15F, 2))]], headers = ["Order", "Item Amnt", "Item Price","Total"]))
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
                                                        print(tabulate([['Prime Rib dinner', str(quanDin1), '$' + str(din1), '$' + str(round(sumT1, 2))], [ "", "", "", ""], ['','','sub total', "$"+str(round(RibgrandT15Stnd, 2))], ['','',"Tax 13%", "$"+str(round(RibgrandT15Stndtx, 2))],['','',"Total", "$"+str(round(RibgrandT15Stndtxf, 2))]], headers = ["Order", "Item Amnt", "Item Price","Total"]))  
                                                        print(msg)
                                                        while True:
                                                          exit
                                                                      
                                                 elif stud != 'y' or 'Y' or 'n' or 'N' :

                                                     print("Incorrect response")    
                                                     continue       
                                                 
                                                               
                                                               
                                                                      
                                                               
                                   elif sumT1 >= disC and disC1 > sumT1 :        
                                                        print("Current selection: ")
                                                        Ribdiscnt10 = (.10*sumT1)
                                                        RibgrandT10 = (sumT1 - Ribdiscnt10)
                                                        print("Your sub total is: " + "$" + str(round(sumT1, 2)) + "\nYour 10% discount savings are: " + "$" + str(round(Ribdiscnt10, 2)))
                                                        print(str(firHead) + "\n" + str(quanDin1) + " X\t" + "Prime rib dinner\n" + "-----------------------------------\n" + "Your grand total is : " + "$" + str(round(RibgrandT10, 2)) + "\n-----------------------------------\n")
                                                        
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
                                                                      print(tabulate([['Prime Rib dinner', str(quanDin1), '$' + str(din1), '$' + str(round(sumT1, 2))], ["10 % Student savings", '', '', '- $'+ str(round(RibgrandT10S, 2))],['','','sub total', "$" + str(round(RibgrandT10St, 2))],['','',"Tax 13%", "$" + str(round(Ribtax10, 2))],['','',"Total", "$" + str(round(Ribtax10F, 2))]], headers = ["Order", "Item Amnt", "Item Price","Total"]))
                                                                      while True:
                                                                       exit
                                                               if stud == 'n' or stud == 'N' :
                                                                      flag3 = True
                                                                      print("No student discount applicable.")
                                                                      RibgrandT10Stnd = RibgrandT10
                                                                      RibgrandT10Stndtx = RibgrandT10 * hst
                                                                      RibgrandT10Stndtxf = RibgrandT10Stndtx + RibgrandT10
                                                                      print(*res, sep = ' ')
                                                                      print(tabulate([['Prime Rib dinner', str(quanDin1), '$' + str(din1), '$' + str(round(sumT1, 2))], [ "", "", "", ""], ['','','sub total', "$" + str(round(RibgrandT10Stnd, 2))], ['','',"Tax 13%", "$" + str(round(RibgrandT10Stndtx, 2))],['','',"Total", "$" + str(round(RibgrandT10Stndtxf))]], headers = ["Order", "Item Amnt", "Item Price","Total"]))  
                                                                      while True:
                                                                       exit
                                                               if stud != 'y' or 'Y' or 'n' or 'N' :
                                                                      print("Incorrect response")
                                                                      continue
                                   elif sumT1 < disC :
                                                 
                                                        print("5% discount granted!")
                                                        Ribdiscnt5 = (.05*sumT1)
                                                        Ribgrand5 = (sumT1 - Ribdiscnt5)
                                                        
                                                        print("Your sub total is: " + "$" + str(round(sumT1, 2)) + "\nYour 5% discount savings are: " + "$" + str(round(Ribdiscnt5, 2)))
                                                        print(str(firHead) + "\n" + str(quanDin1) + " X\t" + "Prime rib dinner\n" + "-----------------------------------\n" + "Your grand total is : " + "$" + str(round(Ribgrand5, 2)) + "\n-----------------------------------\n")
                                                        
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
                                                                      print(tabulate([['Prime Rib dinner', str(quanDin1), "$" + str(din1), "$" + str(round(sumT1, 2))], ["10 % Student savings", '', '', '- $'+ str(round(RibgrandT5S, 2))],['','','sub total', "$" + str(round(RibgrandT5St, 2))],['','',"Tax 13%", "$" + str(round(Ribtax5, 2))],['','',"Total", "$" + str(round(Ribtax5F, 2))]], headers = ["Order", "Item Amnt", "Item Price","Total"]))
                                                                      while True:
                                                                       exit
                                                               if stud == 'n' or stud == 'N' :
                                                                      flag4 = True
                                                                      print("No student discount applicable.")
                                                                      RibgrandT5Stnd = Ribgrand5
                                                                      RibgrandT5Stndtx = RibgrandT5Stnd * hst
                                                                      RibgrandT5Stndtxf = RibgrandT5Stndtx + RibgrandT5Stnd
                                                                      print(*res, sep = ' ')
                                                                      print(tabulate([['Prime Rib dinner', quanDin1, "$" + str(din1), "$" + str(round(sumT1, 2))], [ "", "", "", ""], ['','','sub total', "$" + str(round(RibgrandT5Stnd, 2))], ['','',"Tax 13%", "$" + str(round(RibgrandT5Stndtx, 2))],['','',"Total", "$" + str(round(RibgrandT5Stndtxf, 2))]], headers = ["Order", "Item Amnt", "Item Price","Total"]))  
                                                                      while True:
                                                                       exit
                                                               if stud != 'y' or 'Y' or 'n' or 'N' :
                                                                      print("Incorrect response")
                                                                      continue                   

                                   
                                   
                                   
                                                                             
                            if conf1 == 'n' or conf1 == 'N' :                               
                                   resta() #certain condition like the customer wanting to restart their order.
                                   
                                                 
                                          
                            if conf1 != 'y' or 'Y' or 'n' or 'N':
                                   print("Invalid entry") 
                                   
                                   flag1 = True
                                   continue      
                            
                                          
              elif dinChoice == '2':
                     quanDin2 = float(input("How many of the turkey dinners would you like: "))
                     sumT2 = (quanDin2 * din2)
                     flag5 = False
                     while True:
                            conf2 = input("Are you sure you would like to order: \n" + str(quanDin2) + "\tX  Turkey Dinners:" + "\n[Yes or No]: ")
                            if conf2 == 'y' or conf2 == 'Y' :
                                   flag5 = True                     
                                   
                                   if sumT2 >= disC and disC1 > sumT2 :        
                                          print("10% discount granted!")
                                          Tudiscnt10 = (.10*sumT2)
                                          Tugrand10 = (sumT2 - Tudiscnt10)
                                                 
                                          print("Your sub total is: " + "$" + str(round(sumT2, 2)) + "\nYour 10% discount savings are: " + "$" + str(round(Tudiscnt10, 2)))
                                          print(str(firHead) + "\n" + str(quanDin2) + " X\t" + "Turkey dinner\n" + "-----------------------------------\n" + "Your grand total is : " + "$" + str(round(Tugrand10, 2)) + "\n-----------------------------------\n")
                                          flag8 = False
                                          while True:
                                                 
                                                 stud = str(input("Are you a student? "))
                                                 if stud == 'y' or stud == 'Y' :
                                                        flag8 = True
                                                        
                                                        TugrandT10S = (Tugrand10 * studIc)
                                                        TugrandT10St = (Tugrand10 - TugrandT10S)  
                                                        Tutax10 = (hst*TugrandT10St)
                                                        Tutax10F = Tutax10 + TugrandT10St
                                                        print(*res, sep = ' ')
                                                        print(tabulate([['Turkey dinner', str(quanDin2), '$' + str(din2), '$' + str(round(sumT2, 2))], ["10 % Student savings", '', '', '- $'+ str(round(TugrandT10S, 2))],['','','sub total', "$" + str(round(TugrandT10St, 2))],['','',"Tax 13%", "$" + str(round(Tutax10, 2))],['','',"Total", "$" + str(round(Tutax10F, 2))]], headers = ["Order", "Item Amnt", "Item Price","Total"]))
                                                        print(msg)
                                                        
                                                        
                                                        while True:
                                                         exit
                                                               
                                                        
                                                        
                                                        
                                                 

                                          
                                                 elif stud == 'n' or stud == 'N' :
                                                        flag8 = True
                                                        
                                                        TugrandT10Stnd = Tugrand10
                                                        TugrandT10Stndtx = Tugrand10 * hst
                                                        TugrandT10Stndtxf = TugrandT10Stnd + TugrandT10Stndtx
                                                        print(*res, sep = ' ')
                                                        print(tabulate([['Turkey dinner', str(quanDin2), '$' + str(round(din2, 2)), '$' + str(round(sumT2, 2))], [ "", "", "", ""], ['','','sub total', "$" + str(round(TugrandT10Stnd, 2))], ['','',"Tax 13%", "$" + str(round(TugrandT10Stndtx, 2))],['','',"Total", "$" + str(round(TugrandT10Stndtxf, 2))]], headers = ["Order", "Item Amnt", "Item Price","Total"]))  
                                                        print(msg)
                                                        while True:
                                                         exit
                                                        
                                                 elif stud != 'y' or 'Y' or 'n' or 'N' :

                                                        print("Incorrect response")    
                                                        continue   
                                   if sumT2 < disC :
                                          print("5% discount granted!")
                                          Tudiscnt5 = (.5*sumT2)
                                          Tugrand5 = (sumT2 - Tudiscnt5)
                                                 
                                          print("Your sub total is: " + "$" + str(round(sumT2, 2)) + "\nYour 5% discount savings are: " + "$" + str(round(Tudiscnt5, 2)))
                                          print(str(firHead) + "\n" + str(quanDin2) + " X\t" + "Turkey dinner\n" + "-----------------------------------\n" + "Your grand total is : " + "$" + str(round(Tugrand5, 2)) + "\n-----------------------------------\n")
                                          flag7 = False
                                          while True:
                                                 
                                                 stud = str(input("Are you a student? "))
                                                 if stud == 'y' or stud == 'Y' :
                                                        flag7 = True
                                                        
                                                        TugrandT5S = (Tugrand5 * studIc)
                                                        TugrandT5St = (Tugrand5 - TugrandT5S)  
                                                        Tutax5 = (hst*TugrandT5St)
                                                        Tutax5F = Tutax5 + TugrandT5St
                                                        print(*res, sep = ' ')
                                                        print(tabulate([['Turkey dinner', str(quanDin2), '$' + str(din2), '$' + str(round(sumT2, 2))], ["10 % Student savings", '', '', '- $'+ str(round(TugrandT5S, 2))],['','','sub total', "$" + str(round(TugrandT5St, 2))],['','',"Tax 13%", "$" + str(round(Tutax5, 2))],['','',"Total", "$" + str(round(Tutax5F, 2))]], headers = ["Order", "Item Amnt", "Item Price","Total"]))
                                                        print(msg)
                                                        
                                                        
                                                        while True:
                                                         exit
                                                               
                                                        
                                                        
                                                        
                                                 

                                          
                                                 elif stud == 'n' or stud == 'N' :
                                                        flag7 = True
                                                        print("No student discount applicable.")
                                                        TugrandT5Stnd = Tugrand5
                                                        TugrandT5Stndtx = Tugrand5 * hst
                                                        TugrandT5Stndtxf = TugrandT5Stnd + TugrandT5Stndtx
                                                        print(*res, sep = ' ')
                                                        print(tabulate([['Turkey dinner', str(quanDin2), '$' + str(din2), '$' + str(round(sumT2, 2))], [ "", "", "", ""], ['','','sub total', "$" + str(round(TugrandT5Stnd, 2))], ['','',"Tax 13%", "$" + str(round(TugrandT5Stndtx, 2))],['','',"Total", "$" + str(round(TugrandT5Stndtxf, 2))]], headers = ["Order", "Item Amnt", "Item Price","Total"]))  
                                                        print(msg)
                                                        while True:
                                                         exit
                                                        
                                                 elif stud != 'y' or 'Y' or 'n' or 'N' :

                                                        print("Incorrect response")    
                                                        continue       
                                   if sumT2 > disC1 :
                                          
                                          
                                          Tudiscnt15 = (.15*sumT2)
                                          Tugrand15 = (sumT2 - Tudiscnt15)
                                                 
                                          print("Your sub total is: " + "$" + str(round(sumT2, 2)) + "\nYour 15% discount savings are: " + "$" + str(round(Tudiscnt15, 2)))
                                          print(str(firHead) + "\n" + str(quanDin2) + " X\t" + "Turkey dinner\n" + "-----------------------------------\n" + "Your grand total is : " + "$" + str(round(Tugrand15, 2)) + "\n-----------------------------------\n")
                                          flag6 = False
                                          while True:
                                                 
                                                 stud = str(input("Are you a student? "))
                                                 if stud == 'y' or stud == 'Y' :
                                                        flag6 = True
                                                        
                                                        TugrandT15S = (Tugrand15 * studIc)
                                                        TugrandT15St = (Tugrand15 - TugrandT15S)  
                                                        Tutax15 = (hst*TugrandT15St)
                                                        Tutax15F = Tutax15 + TugrandT15St
                                                        print(*res, sep = ' ')
                                                        print(tabulate([['Turkey dinner', str(quanDin2), '$' + str(din2), '$' + str(round(sumT2, 2))], ["10 % Student savings", '', '', '- $' + str(round(TugrandT15S, 2))],['','','sub total', "$" + str(round(TugrandT15St, 2))],['','',"Tax 13%", "$" + str(round(Tutax15, 2))],['','',"Total", "$"+str(round(Tutax15F, 2))]], headers = ["Order", "Item Amnt", "Item Price","Total"]))
                                                        print(msg)
                                                        
                                                        
                                                        while True:
                                                         exit
                                                               
                                                        
                                                        
                                                        
                                                 

                                          
                                                 elif stud == 'n' or stud == 'N' :
                                                        flag6 = True
                                                        
                                                        TugrandT15Stnd = Tugrand15
                                                        TugrandT15Stndtx = Tugrand15 * hst
                                                        TugrandT15Stndtxf = TugrandT15Stnd + TugrandT15Stndtx
                                                        print(*res, sep = ' ')
                                                        print(tabulate([['Turkey dinner', str(quanDin2), '$' + str(din2), '$' + str(round(sumT2, 2))], [ "", "", "", ""], ['','','sub total', "$" + str(round(TugrandT15Stnd, 2))], ['','',"Tax 13%", "$" + str(round(TugrandT15Stndtx, 2))],['','',"Total", "$" + str(round(TugrandT15Stndtxf, 2))]], headers = ["Order", "Item Amnt", "Item Price","Total"]))  
                                                        print(msg)
                                                        while True:
                                                         exit
                                                        
                                                 elif stud != 'y' or 'Y' or 'n' or 'N' :

                                                        print("Incorrect response")    
                                                        continue       
                                          
                                   
                            if conf2 == 'n' or conf2 == 'N' :
                                    
                                   resta()   #certain condition like the customer wanting to restart their order.
                            if conf2 != 'y' or 'Y' or 'n' or 'N':
                                   
                                   print("Invalid entry")
                                   continue                
              
                     
              
       elif dinChoice.isalpha() :
              print("Invalid response, please user numbers, not letters.")
       else:
              print("Invalid choice, please select choice 1 or 2.")       


while True:   #program will continously run
      resta()



