# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")
# first_name = first_name.capitalize()
# last_name = last_name.capitalize()

# print("Your name is", first_name, last_name)

    # •    The script should ask the user where they want to travel.
    # •    The user’s input should be checked for 3 different travel destinations that you define.
    # •    If the user’s input is one of those 3 destinations, the following statement should be printed: “Enjoy your stay in ______!”
    # •    If the user’s input is something other than the defined destinations, the following statement should be printed: “Oops, that destination is not currently available.”
travel_destination = input('Where do you want to travel?\nA- Japan\nB- Italy\nC- France\n').lower()
if travel_destination == 'a' or travel_destination == 'japan':
    print('Japan is wonderful in spring. Enjoy your stay there.')
elif travel_destination == 'b' or travel_destination == 'italy':
    print('Italy is beautiful in every season!')
elif travel_destination == 'c' or travel_destination == 'france':
    print('France is a timeless tapestry of art, cuisine, and romance.')
else:
    print('Oops, that destination is not currently available.')