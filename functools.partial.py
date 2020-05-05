# two ways to simplify
# a function's signature
# when it's possible.

# Here, I'm taking the max(iterable,key) function
# as an example

from functools import partial

# I will call my simple-signatured function
# longest (returns the longest element
# in an iterable)

longest_1=partial(max,key=len)

longest_2=lambda x:max(x,key=len)


# sample lists
ls=[
["hello",
"yeeeeaaaaaa",
'oops',
"!",
3*"oooooooo"],
["eh no",
"oh no",
"ah no"],
[range(3),
range(6),
range(11),
range(2)]
]


for sublist in ls:
    print(longest_1(sublist))
    print(longest_2(sublist))
    print()
    
print(longest_1("str1","string2","ss"))
try:
    print(longest_2("str1","string2","ss"))
except:
    err="Lambda usage is not as powerful as functools.partial (doesn't support multiple syntaxes like the original function)"
    raise TypeError(err)
    
