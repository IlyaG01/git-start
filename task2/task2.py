a='apple'
b='bed'
c='clever city cat'
d='directory'
lst=[a,b,c,d]
z1=lambda x:( x.find(' ') ==-1)#method returns True if the string has space
z2=lambda x:( not x.startswith('a'))#method returns True if the string starts with 'a'
z3=lambda x:( len(x) >= 5)#method returns True if lenght of string less 5
def func_with_lambda(z,lst):
    newlist = list(filter(z,lst)) # new list
    return newlist
newlist=func_with_lambda(z1,lst)
print(newlist)