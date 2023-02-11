TICKET_PRICE = 10

tickets_remaining = 100

# output  remaining number of available tickets with a variable
print("There are {} tickets still available".format(tickets_remaining))

# get the users name and assign it to a variable
name = input("what is your name?  ")

# Prompt the user by name and ask them how many tickets they want to buy
num_tickets = input("how many tickets do you need to buy, {}?  ".format(name))
num_tickets = int(num_tickets)

# then calculate the total amount ( number of tickets multiplied by price)
amount_due = num_tickets * TICKET_PRICE

# output the total amount to the screen
print("Total amount due is ${}".format(amount_due))
