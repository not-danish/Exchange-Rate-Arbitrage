domestic_currency = None
foreign_currency = None
domestic_interest = None
current_exchange = None
foreign_interest = None
expected_exchange = None

while True:
  print("1. Edit Domestic Currency")
  print("2. Edit Foreign Currency")
  print("3: Edit Current Exchange Rate")
  print("4. Edit Domestic Interest Rate")
  print("5. Edit Foreign Domestic Rate")
  print("6. Edit Future/Expected Foreign Exchange Rate")
  print("7. Calculate if arbitrage opportunity exists")
  print("-------------------------")
  selection = input("Select an option from the list: ")

  if(selection == 1):
    domestic_currency = input("Input new Domestic Currency: ")
    
  elif(selection == 2):
    foreign_currency = input("Input new Foreign Currency: ")
    
  elif(selection == 3):
    current_exchange = input("Input current Exchange Rate (DC/FC): ")
    
  elif(selection == 4):
    domestic_interest = input("Input new Domestic Interest Rate: ")

  elif(selection == 5):
    foreign_interest = input("Input new Foreign Interest Rate: ")
    
  elif(selection == 6):
    expected_exchange = input("Input new Expected Exchange Rate: ")
    
  elif(selection == 7):
    if(domestic_currency == None or foreign_currency == None or current_exchange == None or domestic_interest == None or foreign_interest == None or expected_exchange == None):
      print("Error: You have not input one or more of your  required values")
  