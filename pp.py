def Login():

    vip_person = ['Kaung Myat','Kaung Min']

    for v in vip_person:
        name = input("Enter Your VIP Name: ")
        if v == name:
            print("You can use system:) ")

            account = input("Enter Your Token Account Email: ")
            password = input("Enter Your Password: ")
            cpassword = input("Enter Your Confirm Password: ")
            if password == cpassword:
                print("Success Your Login:) ")
            token = 3
            lucky_num = [10,15,20,25,30,35,40,45,50]
            while token<0:
                num = input("Enter 'Y' to use the service or 'N' to quit: ")
                if num == 'Y':
                    print("Service used.")
                    token -= 1
                    print("Tokens remaining:", token)
                    for i in lucky_num:
                        lottery_num = int(input("Enter Your Lottery Number: "))
                        if lottery_num == lucky_num:
                            print("Congratulations! You win!")
                            break
                        elif lottery_num != i:
                            print("Sorry, not a winning number.")
                            break
                
                elif num == 'N':
                    print("Exiting the program.")
                    break
                else:
                    print("Invalid input. Please enter 'Y' or 'N'.")
            if token == 0:
                print("You've run out of tokens. Please purchase more to continue using the service.")

        else:
            print("Please Check Your Password! ")
        break

    else:
        print("You can't use system:( ")    

Login()
