class MyException(Exception):
    def __init__(self, text='This is my exception'):
        self.text = text

    def __str__(self):
        return f'Error: {self.text}'


raise MyException
