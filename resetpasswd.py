

old_password = input("Enter Your Old Password: ")

def password(new):

    if new != "":
        for s in range(5):
            new_passwd = input("Enter Your New Password: ")
            confirm_password = input("Enter Confirm Password: ")

            if new_passwd != confirm_password:
                
                if s == 4:
                     print("Try Again! ")
                else:
                    print("Please check your confirm password: ")
        
            else:
                print("Success Your New Password.")
                break
            
password(old_password)
    