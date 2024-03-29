"""
Напишите для задачи 1 тесты unittest. Проверьте
следующие варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери
символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов
(кроме п. 1)
"""

import unittest
from task_1 import func


class TestFunc(unittest.TestCase):
    def test_one(self):
        self.assertEqual('hello world', func('hello world'))

    def test_two(self):
        self.assertEqual('hello world', func('HELlO wOrLd'))

    def test_three(self):
        self.assertEqual('hello world', func('hello, wo,r!ld'))

    def test_four(self):
        self.assertEqual('hello world', func('hELlыo, wo,r!ацацld'))


if __name__ == '__main__':
    unittest.main(verbosity=2)
