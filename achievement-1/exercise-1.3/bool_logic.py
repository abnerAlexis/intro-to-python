distance = input("Planet's distance from the sun: ")
axial_tilt = input("Planet's axis: ")

# and operator
print('Planet is habitable by humans:', float(distance) > 0.38 and float(axial_tilt) < 24.5)

# or operator
test1_score = 26
test2_score = 68
print('Student passes:', test1_score >= 50 or test2_score >=50)

# not operator
print('1 not less than 2:', not 1 < 2)

# if else elif
fruit = input("I have an apple, an orange and a banana! " \
     "Which fruit would you like to have? : ")

if fruit == "apple":
    print("Here, have an apple!")

elif fruit == "orange":
    print("Here, have an orange!")

elif fruit == "banana":
    print("Here, have a banana!")

else:
    print("Oops, I don't think I have that.")

# nested statements
number_of_oranges = int(input("How many oranges do you have?: "))

if number_of_oranges > 0:
    print("You have some oranges.")

    if number_of_oranges > 50:
        print("But you've got way too many!")

else:
    print("You have no oranges.")