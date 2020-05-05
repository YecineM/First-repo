# When does unary minus behave differently
# from binary minus ?
# When we have the famous modulo %
# 1- because priority will be in favor of minus
# 2- and modulo's result becomes complicated

print(2%6)   # 2

print(0-2%6)  # -2

# no problem till now,
# % has priority over 'binary' minus,
# unlike (+) for example:
# 5-6+2 is not 5-(6+2)

# so
# 0-2%6 == 0 - 2 == -2

# you could choose any number instead of 0

# Things are different for
# unary minus:

print(0+(-2)%6)  # parentheses prevented
                 # the problem here.
                 
print(-2%6)
# unusual result ! Let's understand it.
# modulo is :
# x%y == x - y*(x//y)

# so, and since [Unary minus] has priority over % !!!
# we get:
# -2%6 == (-2) - 6*((-2)//6) == 4
# -2%6 == (-2) - 6*(-1) == 4

# Note: (-2)//6 = -1 , not 0
# In other words, (-0.333) is the division result,
# so the lower integer (-1) is the floor division result
