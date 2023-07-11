# Main Function Encompassing Chatbot Logic
def coffe_bot():
  print("\nWelcome to the cafe! \n")
  
  size = get_size()
  drink_type = get_drink_type()
  print("\nAlright, that's a {} {}!".format(size, drink_type))

  name = input("\nCan I get your name please? \n\n")
  print("\nThanks, {}! Your drink will be ready shortly.".format(name))

# Funtion to Determine Drink Size Customer is Making
def get_size():
  res = input("What size drink can I get you? \n[a] Small \n[b] Medium \n[c] Large \n\n")

  if res == "a":
    return "Small"
  if res == "b":
    return "Medium"
  if res == "c":
    return "Large"
  else:
    print_message()
    return get_size()

# Funtion to Print Out Message When Invalid Response is Received
def print_message():
  print("\nI'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.\n")

# Function to Obtain Drink Type
def get_drink_type():
  res = input("\nWhat type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n\n")

  if res == "a":
    return "Brewed Coffee"
  if res == "b":
    return "Mocha"
  if res == "c":
    return order_latte()
  else:
    print_message()
    return get_drink_type()

# Funtion to Determine Milk Type if Customer Orders Latte
def order_latte():
  res = input("\nAnd what kind of milk for your latte? \n[a] 2% Milk \n[b] Non-Fat Milk \n[c] Soy Milk \n\n")
    
  if res == "a":
    return "Latte"
  if res == "b":
    return "Non-Fat Latte"
  if res == "c":
    return "Soy Latte"
  else:
    print_message()
    return order_latte

# Calling Coffee Chatbot
coffe_bot()
