#Python Practical 2
#Done by Wong Jun Hao


x= int(input(" Enter side 1:"))
y = int(input("Enter side 2:"))
z = int(input("Enter side 3:"))


if x + y <= z and y+ z <= x and z+ x <= y:
    print(" Invalid triangle")

else:
    sum= x + y +z
    print(sum)

