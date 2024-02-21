class Archive:
    _instance = None
    archive_text = []
    archive_number = []

    def __new__(cls, *args):
        if Archive._instance is None:
            Archive._instance = super().__new__(cls)
            Archive._instance.archive_text.append(args[0])
            Archive._instance.archive_number.append(args[1])
            return Archive._instance
        else:
            Archive._instance.archive_text.append(args[0])
            Archive._instance.archive_number.append(args[1])
            return Archive._instance

    def __init__(self, text, number):
        self.text = text
        self.number = number

    def __str__(self):
        return f'Text is {self.text} and number is {self.number}. Also {Archive.archive_text} and {Archive.archive_number}'

    def __repr__(self):
        return f"Archive('{self.text}', '{self.number}')"


a = Archive('text1', 1)
print(a)
b = Archive('text2', 2)
print(a)
print(b)

# def __new__(cls, text, number):
#     instance = super().__new__(cls)
#     instance.text = text
#     instance.number = number
#     cls.archive_number.append(number)
#     cls.archive_text.append(text)
#     instance.archive_number = cls.archive_number.copy()
#     instance.archive_text = cls.archive_text.copy()
#     return instance
