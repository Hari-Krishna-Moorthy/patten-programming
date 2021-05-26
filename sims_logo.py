#                ____*____
#                ___*_*___
#                __*___*__
#                _*__*__*_
#                *__*_*__*
#                _*__*__*
#                __*___*_
#                ___*_*__
#                ____*___



n = int(input()) # 5

for i in range(n):
    for j in range(n) :
        if j + i ==  n-1  : print("*" , end = '')
        elif i+j == n+2   : print("*" , end ='')
        else :              print("_" ,end= '')
    for j in range(n-2 , -1 , -1) :
        if j + i ==  n-1  : print("*" , end = '')
        elif i+j == n+2   : print("*" , end ='')
        else :              print("_" ,end= '')
    print()

for i in range(1 ,n):
    for j in range(0 , n-1) :
        if i == j: print("*" , end = '')
        else :     print("_" ,end= '')
    for j in range(1 , n) :
        if i + j == n: print("*" , end = '')
        elif i==1 and j==1  : print("*" , end ='')
        else :              print("_" ,end= '')
    print()
    