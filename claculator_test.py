import pytest
import unittest2

from operators import *

class Calc_TDD(unittest2.TestCase):

    sharp = Calc_Test()

    def test_modulo(self):
        self.assertEqual(self.sharp.modulo(10, 5), 0)

    def test_cm_in(self):
        self.assertEqual(self.sharp.cm_inch(10,), 25.4)

    def test_in_cm(self):
        self.assertEqual(self.sharp.inch_cm(2.54), 1.00050854 )