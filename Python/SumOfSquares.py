def sum_of_squares(lst):
    sum = 0 
    for k in lst:
        i = int(k)
        sum += i*i 
    return sum
        
lst = input().split(",")
result = sum_of_squares(lst)
print(result)