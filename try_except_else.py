x,y=12/6
try:
    assert x/y
except ZeroDivision as z:
    print(z)
else:
    print(" Division value =",x/y)
