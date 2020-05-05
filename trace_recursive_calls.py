from functools import wraps


def trace(fun):
	@wraps(fun)
	def fn(*args):
		fn.att+=1
		print("|  "*(fn.att-1)+"|--",end="")
		print(fun.__name__,*args)
		ret=fun(*args)
		print("|  "*fn.att+"|--",end="")
		print("returning",ret)
		fn.att-=1
		return ret
	fn.att=0
	return fn

#       Alternatively,
#       you can use a list defined in the outer scope.
#       (you can also use a global variable then define
#       it locally with glob, but global variable usage
#       is usually discouraged)

#       Using a list:
#def trace(fun):
#       ls=[]
#	@wraps(fun)
#	def fn(*args):
#		print(*ls,"|--",sep="",end="")
#		print(fun.__name__,*args)
#		ls.append("|  ")
#		ret=fun(*args)
#		print(*ls,"|--",sep=""end="")
#		print("returning",ret)
#		ls.pop()
#		return ret
#	return fn

print("""Now define your function,
and then call it with your desired arguments.
I will print its output, don't worry.

Alternatively, you can define other functions
after ending this input,
but you will have to decorate them
yourself using:
"@trace"

Press Ctrl+c to end""")

try:
    codelines=["@trace"]
    while True:
        inp=input()
        if inp:
            codelines.append(inp)

except KeyboardInterrupt:
    call=codelines[-1]
    code="\n".join(codelines[:-1])
    exec(code)
    print(eval(call))
