# can't use optional argument for 'initial'
# (iterable may itself contain the default
# value, even None may be in the list)

# we can't omit 'initial' either,
# and we can't put it as a positional arg
# (user may choose to omit it)
# so..

#             *args


def reduce(*args):
    
    if len(args)==2:
        func,iterable=args
        return reduce(
        func,
        iterable[1:],
        iterable[0]
                     )
    func,iterable,initial=args
    
    # base case:
    if len(iterable)==1:
        return func(initial,iterable[0])
    
    # recursion:
    return reduce(
    func,
    iterable[1:],
    func(initial,iterable[0])
              )


# test:
print(reduce(lambda x,y:x+y,[1,2,3,4,5]))

print(reduce(lambda x,y:x**y,[1,2,3,4,5]))

print(reduce(lambda x,y:x*y,range(1,6),100))
