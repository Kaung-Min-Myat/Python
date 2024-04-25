
# Functions

# def == define

# Functions Signature = ( )

# Every functions need to recall at the end
# Without call the functions , it will not show any output

# def kaung():
#     print("Hello world")

# kaung()

# def minmyat():
#     a = 1
#     b = 2
#     c = a  + b
#     print(c)

# minmyat()



# def calcu():
#     a=1
#     b=2
#     result=a+b
#     result2= b-a
#     result3=a*b
#     result4=a/b
#     result5=a%b
#     result6=a//b
#     print(result, result2, result3, result4, result5, result6)

# calcu()


# def calculator():

#     num=int(input("Enter First Number: "))
#     num2=int(input("Enter Second Number: "))
#     userchoice=input("Enter Operator")

#     if userchoice == "+":
#         print(num+num2)
#     elif userchoice == "-":
#         print(num-num2)
#     elif userchoice == "*":
#         print(num*num2)
#     elif userchoice == "/":
#         print(num/num2)
#     elif userchoice == "%":
#         print(num%num2)
#     elif userchoice == "//":
#         print(num//num2)

# calculator()


num=int(input("Enter First Number: "))
num2=int(input("Enter Second Number: "))
operator=input("Choose Operator: ")

def addition():
    
    print(num+num2)



def subtraction():

    print(num-num2)



def multiplication():

    print(num*num2)



def division():

    print(num/num2)



def floor():

   print(num//num2)



def modulus():
    
    print(num%num2)



def exponent():

    print(num**num2)







def calcu():

    if operator == "+":
        addition()
    elif operator == "-":
        subtraction()
    elif operator == "*":
        multiplication()
    elif operator == "/":
        division()
    elif operator == "//":
        floor()
    elif operator == "%":
        modulus()
    elif operator == "**":
        exponent()

calcu()


    
    

