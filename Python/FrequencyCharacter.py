def dict_string(s,k):
    dict_alpha = {}
    for i in k:
        d = s.count(i)
        dict_alpha[i] = d
    return(dict_alpha)

s = input().lower()
k =""
for i in s:
    if i not in k and i.isalpha()==True:
        k+=i
result = dict_string(s,k)
print(result)