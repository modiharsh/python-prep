# python 'star expression' can be sed to unpack an iterable with arbitrary length


user_record = ('Harsh', 'adfs@gmail.com', '123-123', '545-434')
Name, email, *phone_no = user_record

print(Name)     # Harsh
print(email)    # adfs@gmail.com
print(phone_no) # ['123-123', '545-434']

# ^^ such variables are always list, even for None


# This is particularly useful when iterating over tuples of varying length

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4)
]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    do_foo(*args) if tag == 'foo' else do_bar(*args)