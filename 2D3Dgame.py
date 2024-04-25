# Input , Output , Process ==>> Variables , Data Types, Condition , Statement , Loop ==>> for loop
# Forever loop #while loop


# win_number = [88,99]

# for i in win_number:
#     lottery_num = int(input("Enter Your Lottery Number: "))
    
#     if lottery_num==i:
#         print("Congratulations! You win!")
#         break
#     elif lottery_num!=i:
#         print("Sorry, not a winning number.")
#         break



def lottery():

    win_number = [88,99]

    for i in win_number:
        lottery_num = int(input("Enter Your Lottery Number: "))
    
        if lottery_num==i:
            print("Congratulations! You win!")
            break
        elif lottery_num!=i:
            print("Sorry, not a winning number.")
            break

lottery()