def show_menu(number):
  print("")
  print("---Choose the menu---")
  print("1. Espresso")
  print("2. Cappucino")
  print("3. Latte")
  print("")
  number_menu = int(input("Select coffee: "))
  return number_menu


def show_type_coffee():
  print("")
  print("---Choose the type of the coffee---")
  print("1. Hot 55 baht")
  print("2. Cold 60 baht")
  print("")
  number_coffee = int(input("Select type: "))
  return number_coffee 



print("---Welcome to Natcha Coffee---")
print("")
number1 = int(input("Please type 1 to show menu: "))
if number1 == 1 :
  menu = show_menu(number1)

  if menu == 1 or menu == 2 or menu == 3:
    coffee_type = show_type_coffee()
    
    if coffee_type == 1 or coffee_type == 2:
      if menu == 1:
        if coffee_type == 1:
          print("---You chose hot Espresso 55 baht---")
        elif coffee_type == 2:
          print("---You chose Cold Espresso 60 baht---")

      elif menu == 2:
        if coffee_type == 1:
          print("---You chose hot Cappucino 55 baht---")
        elif coffee_type == 2 :
          print("---You chose Cold Cappucino 60 baht---")

      elif menu == 3:
        if coffee_type == 1:
          print("---You chose hot Latte 55 baht---")
        elif coffee_type == 2:
          print("---You chose Cold Latte 60 baht---")

      print("")
      pay = int(input("Input your money: "))

      if coffee_type == 1:
        if pay >= 55: 
          sum = pay-55
          print("You recieved a change of %d baht" %sum)
          print("---Thank you---")
        else:
          print("Not enough money")
          print("---Please try again---")

      elif coffee_type == 2:
        if pay >= 60: 
          sum = pay-60
          print("You recieved a change of %d baht" %sum)
          print("---Thank you---")
        else:
          print("Not enough money")
          print("---Please try again---")
          
    else:
      print("Sorry, something went wrong")
      print("---Please try again---")

  
  else:
    print("Sorry, something went wrong")
    print("---Please try again---")
  
else:
  print("Sorry, something went wrong")
