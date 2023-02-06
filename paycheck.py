import math


def split_check(total, number_of_people):
    return math.ceil(total / number_of_people)


try:
    total_due = float(input("what is due?"))
    number_of_people = int(input("how many in group?"))
except ValueError:
    print("you dumb ass, enter a number")
else:
    amount_due = split_check(total_due, number_of_people)
    print("each dude owes ${}".format(amount_due))
