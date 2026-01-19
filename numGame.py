import random
# import os
com_num=random.randint(1,20)
user_num=int(input("Guess a number:"))
if user_num==com_num:
    print("win😂😂😂🦄")
    print(user_num,com_num)
else:
    print("Lose🤦‍♂️🤦‍♂️🤦‍♂️","Because enter number is not same to same of computer number")
    print("Computer_num:",com_num)
    print("Entered number:",user_num)

