TICKET_PRICE = 10
SERVICE_CHARGE = 2
tickets_remaining = 100

#  calculate price function with service charge


def calculate_price(number_of_tickets):
    return (number_of_tickets * TICKET_PRICE) + SERVICE_CHARGE


# run code as long as there are tickets available
while tickets_remaining >= 1:

    # output  remaining number of available tickets with a variable
    print("There are {} tickets still available".format(tickets_remaining))

    # get the users name and assign it to a variable
    name = input("what is your name?  ")

    # Prompt the user by name and ask them how many tickets they want to buy
    num_tickets = input(
        "how many tickets do you need to buy, {}?  ".format(name))
    # handle value errors
    try:
        num_tickets = int(num_tickets)
        if num_tickets > tickets_remaining:
            raise ValueError(
                "There are ONLY {} tickets remaining".format(tickets_remaining))
    except ValueError as err:
        print("please enter a correct info {}.".format(err))
    else:
        # then calculate the total amount ( number of tickets multiplied by price)
        amount_due = calculate_price(num_tickets)

        # output the total amount to the screen
        print("Total amount due is ${}".format(amount_due))

        # prompt user if they wan to proceed with purchase
        should_proceed = input(
            "Do you want to proceed with purchase?   Y/N   ")

        # if yes then print out SOLD then decrement the tickets remaining by the  number purchased
        if should_proceed.lower() == "y":
            print("SOLD!")
            tickets_remaining -= num_tickets
        # in no then tell them   to stop wasting your damn time by name
        else:
            print("Thanks for wasting my time {}".format(name))

# notify user that no more tickets are available
print("No more tickets  are available")
