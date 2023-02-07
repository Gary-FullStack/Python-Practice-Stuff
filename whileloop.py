import sys

MASTER_PASSWORD = "opensesame"
password = input("enter password:  ")
attempt_count = 1
while password != MASTER_PASSWORD:
    if attempt_count > 3:
        sys.exit("slow down, speedy.  too many attempts")
    password = input(" invalid. try again: ")
    attempt_count += 1

print("welcome Ninjas ...")
