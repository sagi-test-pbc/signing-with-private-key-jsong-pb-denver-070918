from unittest import TestCase
from ipynb.fs.full.index import *

class PrivateKeyTest(TestCase):

    def test_sign(self):
        pk = PrivateKey(randint(0, 2**256))
        z = randint(0, 2**256)
        sig = pk.sign(z)
        self.assertTrue(pk.point.verify(z, sig))