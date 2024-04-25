# Keywords
# Loop
# Token sytem 3 time use


token = 3

while token>0:
    num = input("Enter 'Y' to use the service or 'N' to quit: ").upper()
    
    if num=='Y':
        print("Service used.")
        token -= 1
        print("Tokens remaining:", token)
        break
    elif num=='N':
        print("Exiting the program.")
        break
    else:
        print("Invalid input. Please enter 'Y' or 'N'.")

if token == 0:
    print("You've run out of tokens. Please purchase more to continue using the service.")
