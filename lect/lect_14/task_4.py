import doctest
import unittest
import task_1


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(task_1))
    tests.addTests(doctest.DocFileSuite('task_1.md'))
    return tests


if __name__ == '__main__':
    unittest.main(verbosity=2)
