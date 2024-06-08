def is_palindrome(string):
    back_string = string[::-1] 
    print(string == back_string)

string = input().lower()
is_palindrome(string)