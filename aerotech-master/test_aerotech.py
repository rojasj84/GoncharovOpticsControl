"""
Unittest the ensemble class
"""
import time

from aerotech import Ensemble
import unittest

class Test(unittest.TestCase):
    def setUp(self):
        ip = '192.168.1.100'
        port = 8000
        self.my_ensemble = Ensemble(ip, port)
        self.my_ensemble.connect()
        self.my_ensemble.move(100, 100, 55)
        time.sleep(2)

    def test_ensemble(self):
        self.assertEqual(self.my_ensemble.get_positions()['X'], 1.0)

    def tearDown(self):
        self.my_ensemble.close()

if __name__ == '__main__':
        ip = '192.168.1.100'
        port = 8000
        my_ensemble = Ensemble(ip, port)
        my_ensemble.connect()
        my_ensemble.reset()
        #my_ensemble.enable()
        #my_ensemble.home()
        #my_ensemble.move(15.0, 1.0, 19.0)
        my_ensemble.move(0.0, 0.0, 0.0)
        print(my_ensemble.get_positions())
        time.sleep(5)
        my_ensemble.close()
