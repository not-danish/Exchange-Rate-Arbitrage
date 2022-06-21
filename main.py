domestic_currency = None
foreign_currency = None
domestic_interest = None
current_exchange = None
foreign_interest = None
expected_exchange = None

while True:
  print("1. Calculate if arbitrage opportunity exists")
  print("2. Edit Variables")
  print("-------------------------")
  selection_1 = input("Select an option from the list: ")
  if(str(selection_1) == '1'):
    if(domestic_currency == None or foreign_currency == None or current_exchange == None or domestic_interest == None or foreign_interest == None or expected_exchange == None):
      print("Error: You have not input one or more of your required values")
    else:
      domestic_return = 1 + domestic_interest
      foreign_return = (1+foreign_interest)*(expected_exchange/current_exchange)
      print(f"Domestic Return = {domestic_return}")
      print(f"foreign Return = {foreign_return}")
			
      if(domestic_return > foreign_return):
        print("Invest in Domestic Currency")
      elif(foreign_return > domestic_return):
        print("Invest in Foreign Currency")
      else:
        print("You are indifferent about which currency to invest in")
			
				
  elif(str(selection_1) == '2'):
    print("1. Edit Domestic Currency")
    print("2. Edit Foreign Currency")
    print("3: Edit Current Exchange Rate")
    print("4. Edit Domestic Interest Rate")
    print("5. Edit Foreign Domestic Rate")
    print("6. Edit Future/Expected Foreign Exchange Rate")
    print("-------------------------")
    selection_2 = input("Select an option from the list: ")
  
    if(selection_2 == 1):
      domestic_currency = input("Input new Domestic Currency: ")
      print(f"New domestic currency = {domestic_currency}")
      
    elif(selection_2 == 2):
      foreign_currency = input("Input new Foreign Currency: ")
      print(f"New foreign currency = {foreign_currency}")
      
    elif(selection_2 == 3):
      current_exchange = input("Input current Exchange Rate (DC/FC): ")
      print(f"New exchange rate = {current_exchange}")
      
    elif(selection_2 == 4):
      domestic_interest = input("Input new Domestic Interest Rate: ")
      print(f"New domestic interest rate = {domestic_interest}")
  
    elif(selection_2 == 5):
      foreign_interest = input("Input new Foreign Interest Rate: ")
      print(f"New foreign interest rate = {foreign_interest}")
      
    elif(selection_2 == 6):
      expected_exchange = input("Input new Expected Exchange Rate: ")
      print(f"New expected exchange rate = {expected_exchange}")
  else:
    print("You have typed an incorrect value, try again...")
    