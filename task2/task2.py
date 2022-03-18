word1='apple'
word2='bed'
word3='clever city cat'
word4='directory'
lst=[word1,word2,word3,word4]
string_with_space=lambda x:( x.find(' ') ==-1)#method returns True if the string has space
string_with_a_in_start=lambda x:( not x.startswith('a'))#method returns True if the string starts with 'a'
lenght_less_five=lambda x:( len(x) >= 5)#method returns True if lenght of string less 5
def func_for_filter_list(rule,lst):
    return list(filter(rule,lst)) # new list
newlist=func_for_filter_list(string_with_space,lst)
print(newlist)