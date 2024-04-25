

username = input("Please Enter Your Name: ")

for  i in range(3):
    studentid = input("Please Enter Your Student ID: ")
    confirmsid = input("Confirm Your Student ID: ")

    if studentid == confirmsid:
        print("Your ID Sucess!")

        
        spassword = input("Enter Your Student Password: ")
        cpassword = input("Enter Your Confirm Password: ")
    
        if spassword == cpassword:
            print("Success Your Login:")
            break
        else:
            print("Fail Your Login: Please Check Your Password")
            

    if i == 2:
        print("Try Again! You can Enter Two Times",i)
    

    



