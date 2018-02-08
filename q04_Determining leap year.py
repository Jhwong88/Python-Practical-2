#Python practical 2 qn4 Determining leap year
#Done by Wong Jun Hao










year = int(input("Enter year: "))



if year % 4 == 0:

    print("Leap")

elif year % 400 == 0:

    print("Leap")

elif year % 100 == 0:

    print("Non-Leap")

elif year % 4 == 0:

    print("Leap")

else:

    print("Invalid year")
