SERVICE_CHARGE = 2
TICKET_PRICE = 10

tickets_remaining = 100

def calculate_cost(number_of_tickets): 
  return (num_tickets*TICKET_PRICE) + SERVICE_CHARGE


while tickets_remaining >= 1:
  print("There are {} tickets remaining.".format(tickets_remaining))
  name = input("What is your name? " )
  try: 
    num_tickets = int(input("Hi {}! How many tickets would you like to purchase? ".format(name)))
    if num_tickets > 100:
      raise ValueError("There are only {} tickets remaining. Please try again.".format(tickets_remaining))
  except ValueError as err:
    print("Value entered is not valid. {}".format(err))
  else:
    total_cost = calculate_cost(num_tickets)
    amountdue_message = "Awesome sauce {}! Your total amount due is below: ".format(name)
    amount_due = float(total_cost)
    print(amountdue_message)
    print("${:,.2f}".format(amount_due))
    confirm_purchase = input("Would you like to proceed with the purchase? (Enter Y/N) ")
    if confirm_purchase.lower() == 'y':
      #TODO: Gather credit card info
      tickets_remaining -= num_tickets
      print("SOLD!")
    else: 
      print("Thank you, {}!".format(name) + "There are {} tickets remaining.".format(tickets_reamining))
else:
  print("SOLD OUT! There are {} tickets remaining.".format(tickets_remaining))