# Any sequence ( or iterator ) can be unpacked into variables using assignment operation.

# A tuple can be asssigned
x, y = (5,6)
print(x) # 5
print(y) # 6

# A string can be assigned 
a, b, c = 'Hey'
print(a) # 'H'
print(b) # 'e'
print(c) # 'y'

_, name, price, _ = [ 'blah', 'Cap', 50, (2023,12,1)]
print(name)  # 'Cap'
print(price) # 50