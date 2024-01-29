import functools

f = open('data.bin', 'rb')
for block in iter(functools.partial(f.read, 16), b''):
    print(block)
f.close()
