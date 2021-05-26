n = 6 

count = 1
for i in range(2*n-1):
    # print(i+1 , end = "\t")
    for j in range(2*n+1):
        if i == 0 or i == 2*n-2 or  j == n:
            print("*" , end ="")
        elif j == count or j+1 == count :
            print("*" , end ="")
        elif (2*n-j+1 == count and i < n)or(2*n-j+2 == count and i < n-1):
            print("*" , end= '')
        elif (2*n-j+1 == count and i >= n) or (2*n-j == count and i >= n):
            print("*" , end= "")
        else :  print(" " , end = "")
    print()
    if i == 0  :
        count+=1 
    elif i == n -2 :
        count += 2
    elif i == n-1:
        count +=3
    elif  i < n//2-1 or (i > n and i-n> n//2-2 ):
        count = count 
    else:
        count+=1  
