def Login():
    vip_person = ['Alex', 'John']

    name = input("Enter Your VIP Name: ")
    found = False
    
    for v in vip_person:
        if v == name:
            found = True
            break
    
    if found:
        print("You can use the system :)")

        account = input("Enter Your Token Account Email: ")
        password = input("Enter Your Password: ")
        cpassword = input("Enter Your Confirm Password: ")
        
        if password == cpassword:
            print("Success Your Login :) ")
            token = 3
            lucky_num = [10, 15, 20, 25, 30, 35, 40, 45, 50]

            while token > 0:
                num = input("Enter 'Y' to use the service or 'N' to quit: ")
                if num == 'Y':
                    print("Service used.")
                    token -= 1
                    print("Tokens remaining:", token)
                    lottery_num = int(input("Enter Your Lottery Number: "))
                    
                    found_lottery = False
                    for i in lucky_num:
                        if lottery_num == i:
                            print("Congratulations! You win!")
                            found_lottery = True
                            break
                    if not found_lottery:
                        print("Sorry, not a winning number.")
                        
                elif num == 'N':
                    print("Exiting the program.")
                    break
                else:
                    print("Invalid input. Please enter 'Y' or 'N'.")
                    
            if token == 0:
                print("You've run out of tokens. Please purchase more to continue using the service.")
        else:
            print("Password confirmation failed.")
    else:
        print("You can't use the system :( ")

Login()
