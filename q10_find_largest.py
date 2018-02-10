#Python practical finding largest integer n such that n*n*n <12000
#Done by Wong Jun Hao

n = 50
while n*n*n > 12000:
    n= n-1
print(n)
