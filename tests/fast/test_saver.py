import unittest

from theseus.saver import saver

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_convert_graph_keys_in_str(self):
        graph_value = {(0, 1, 0, 0): 1.0, (0, 2, 1, 0): -1.0, (0, 2, 3, 3): 1.0, (0, 3, 1, 0): -1.0,
                       (0, 3, 2, 0): 0.9999375693689644, (0, 4, 1, 0): -1.0, (0, 5, 2, 0): -1.0, (1, 2, 1, 1): 1.0,
                       (1, 2, 2, 2): 0.9996518236554393, (1, 3, 2, 0): -1.0, (1, 4, 3, 0): -1.0, (1, 5, 2, 0): 1.0,
                       (1, 5, 3, 0): -1.0, (2, 3, 0, 0): -1.0, (2, 4, 2, 0): -1.0, (2, 5, 0, 0): -1.0,
                       (2, 5, 2, 0): 0.9996513746480182, (3, 4, 0, 0): 1.0, (3, 5, 0, 0): 1.0, (4, 5, 0, 0): 1.0}

        val_instring = {'(0, 1, 0, 0)': 1.0, '(0, 2, 1, 0)': -1.0, '(0, 2, 3, 3)': 1.0, '(0, 3, 1, 0)': -1.0,
                          '(0, 3, 2, 0)': 0.9999375693689644, '(0, 4, 1, 0)': -1.0, '(0, 5, 2, 0)': -1.0,
                          '(1, 2, 1, 1)': 1.0, '(1, 2, 2, 2)': 0.9996518236554393, '(1, 3, 2, 0)': -1.0,
                          '(1, 4, 3, 0)': -1.0, '(1, 5, 2, 0)': 1.0, '(1, 5, 3, 0)': -1.0, '(2, 3, 0, 0)': -1.0,
                          '(2, 4, 2, 0)': -1.0, '(2, 5, 0, 0)': -1.0, '(2, 5, 2, 0)': 0.9996513746480182,
                          '(3, 4, 0, 0)': 1.0, '(3, 5, 0, 0)': 1.0, '(4, 5, 0, 0)': 1.0}

        actual = saver.convert_graph_keys_in_str(self, graph_value)
        self.assertEqual(val_instring,actual)