# guest_name = input("Enter Your Name: ")
# room_number = int(input("Enter Room Number: "))

# if room_number<30:
#     print("Avaiable for normal guests")
# elif room_number>50:
#     print("full room")
# elif room_number>30:
#     print("Avaiable for VIP")



def hotel():

    guest_name = input("Enter Your Name: ")
    room_number = int(input("Enter Room Number: "))

    if room_number<30:
        print("Avaiable for normal guests")
    elif room_number>50:
        print("full room")
    elif room_number>30:
        print("Avaiable for VIP")

hotel()
