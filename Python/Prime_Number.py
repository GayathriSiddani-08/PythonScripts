def is_prime(n):
    if(n == 2):
        print("Given Number is Prime")
    else:
        for i in range(2,n):
            if(n%i == 0):
                print("Given Number is not Prime")
                break 
        else:
            print("Given Number is a Prime")
            
n = int(input())
is_prime(n)