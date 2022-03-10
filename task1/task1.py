def palindrom(s):
    if s==s[::-1]:
        print('Palindrom')
    else:
        print("Not palindrom")
s='tenet'
palindrom(s)