def is_palindrom(s):
    if s==s[::-1]:
        return True
    else:
        return False
s='tenet'
print(is_palindrom(s))