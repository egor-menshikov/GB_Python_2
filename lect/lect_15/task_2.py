from datetime import time, datetime, date, timedelta

dt = datetime(1986, 3, 13, 13, 10, 6, 45)
td = timedelta(23, 14, 85, 2, 43, 2, 13)
# dt1 = datetime(1986, 3, 13)
# dt2 = datetime(1988, 8, 11)
# print(dt2 - dt1)
# print(dt + td)

# print(dt)
# print(dt.isoformat())
# print(dt.timestamp())
# print(dt.weekday())
# print(dt.strftime('Дата %d %B %Y. День недели %A. Время %H:%M:%S. Это %W неделя и %j день года.'))

text_time = '13 March 1986 года'
tt = datetime.strptime(text_time, '%d %B %Y года')
print(tt)

# dt = datetime.datetime.now()
# td = datetime.timedelta(hours=1)
# for i in range(24 * 7 + 1):
#     if dt.weekday() == 6:
#         break
#     dt = dt + td
#
# print(i)
