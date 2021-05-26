#   input : 4
#   
#                   * * * * _ _ * 
#
#                   _ _ _ * _ _ * 
#   
#                   * * * * * * * 
#
#                   * _ _ * _ _ _ 
#
#                   * _ _ * * * * 


n = int(input()) # give only odd numbers

for i in range(2*n+1):
    if(i%2 == 1):
        print()
        continue 
    for j in range(2*n -1):
        if(i == n or j == n-1)   :  print("*" , end = " ")
        elif(i == 0 and j < n)   :  print("*" , end = " ")
        elif(i == 2*n and j >= n):  print("*" , end = " ")
        elif(i == 0 and j < n )  :  print("*" , end = " ")
        elif(i < n and j==2*n-2) :  print("*" , end = " ")
        elif(i > n and j==0)     :  print("*" , end = " ")
        else :  print("_" , end = ' ')
    print()