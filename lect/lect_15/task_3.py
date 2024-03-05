from collections import namedtuple
from datetime import date

User = namedtuple('User', 'name surname birthday')
u_1 = User('Egor', 'Menshikov', date(1986, 3, 13))
print(u_1)
print(hash(u_1))
u_2 = User('Egor', 'Menshikov', [1])
print(hash(u_2))
