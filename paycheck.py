import math


def split_check(total, number_of_people):
    if number_of_people <= 1:
        raise ValueError("Number of people must be greater than 1.")
    return math.ceil(total / number_of_people)


try:
    total_due = float(input("what is due?"))
    number_of_people = int(input("how many in group?"))
    amount_due = split_check(total_due, number_of_people)

except ValueError as err:
    print("you dumb ass, enter a number")
    print("{}".format(err))
else:

    print("each dude owes ${}".format(amount_due))
