def find_duplicates(list_items):
    k = [] 
    result = []
    for i in list_items:
        if i not in k:
            k.append(i)
    for j in k:
        b = list_items.count(j)
        if(b > 1):
            result.append(j)
    return(result)
            
list_items = [1,2,3,4,1,2,5,8,4,7,6,8,7,4]
result = find_duplicates(list_items)
print(result)