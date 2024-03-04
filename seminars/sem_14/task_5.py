"""
На семинарах по ООП был создан класс прямоугольник
хранящий длину и ширину, а также вычисляющую периметр,
площадь и позволяющий складывать и вычитать
прямоугольники беря за основу периметр.
Напишите 3-7 тестов unittest для данного класса.
"""

import unittest
from rectangle import Rectangle

class TestRec(unittest.TestCase):
    def setUp(self):
        self.rec_a = Rectangle(3, 5)
        self.rec_b = Rectangle(4, 6)

    def test_add(self):
        self.assertEqual(Rectangle(6, 6), self.rec_a + self.rec_b)

    def test_sub(self):
        self.assertEqual(Rectangle(2, 2), self.rec_a - self.rec_b)

    def test_less(self):
        self.assertLess(self.rec_a, self.rec_b)

    def test_four(self):
        self.assertEqual(16, self.rec_a.perimeter)

    def test_five(self):
        self.assertEqual(self.rec_a.area, 15)

    def tearDown(self):
        del self.rec_a
        del self.rec_b


if __name__ == '__main__':
    unittest.main(verbosity=2)

