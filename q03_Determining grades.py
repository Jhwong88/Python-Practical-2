#q02_triangle
# Done by Wong Jun Hao


mark = int(input(" Enter your marks: "))
if mark in range(70,100):
    grade= "A"
elif mark in range(60,69):
    grade="B"
elif mark in range(55,59):
    grade="C"
elif mark in range(50,54):
    grade="D"
elif mark in range (45,49):
    grade="E"
elif mark in range(35,44):
    grade="S"
elif mark in range(0,35):
    grade="U"

if mark <= 0:
    print("Invalid! Marks must be between 0 and 100")
if mark >=100:
    print("Invalid! Marks must be between 0 and 100")
else:
    print(grade)
    
