def single_line(n):
    if n==0 or n == 2:
        return "*" * (5)
    else :
        return "* R *"

def single_row(n):
    Str = ""
    number = 5 
    for i in range(n//3):
        for j in range(2):
            for k in range(n//3) :
                print(single_line(j) , end= " ")       
            print()

    
    for i in range(n//3) :
        print(single_line(0) , end= " ")       
    print()    

single_row(eval(input()))

"""
Input  : 
5 
Output : 
***** 
* R * 
*****

Input :
9
Output:
***** ***** ***** 
* R * * R * * R * 
***** ***** ***** 
* R * * R * * R * 
***** ***** ***** 
* R * * R * * R * 
***** ***** ***** 
"""
# 5
# 9
