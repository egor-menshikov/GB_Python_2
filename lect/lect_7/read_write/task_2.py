import pathlib


file = open(pathlib.Path('files/binary.data'), mode='wb', buffering=64)
file.write(b'X' * 1200)
file.close()

file = open(pathlib.Path('files/binary.data'), mode='ab')
file.write('hello'.encode('utf-8'))
file.close()

file = open(pathlib.Path('files/binary.data'), mode='r', encoding='utf-8')
print(*file)
file.close()