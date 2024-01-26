text = input('enter:')


def func(data):
    if data.isdigit():
        data = int(data)
        print(data, type(data))
        return
    if data[0] == '-':
        sign = -1
        data = data[1:]
    else:
        sign = 1
    try:
        data = float(data) * sign
        print(data, type(data))
        return
    except ValueError:
        for item in data.split():
            if item.istitle():
                data = data.lower()
                if sign == -1:
                    data = '-' + data
                print(data, type(data))
                return
            else:
                data = data.lower()
                if sign == -1:
                    data = '-' + data
                print(data, type(data))
                return
func(text)
