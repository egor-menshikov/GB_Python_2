import sys

text = 'hello world'
res = text.encode('UTF-8')
print(res, type(res), sys.getsizeof(text), sys.getsizeof(res))
text2 = 'руддщ цщкдв'
res2 = text2.encode('UTF-8')
print(res2, type(res2), sys.getsizeof(text2), sys.getsizeof(res2))
