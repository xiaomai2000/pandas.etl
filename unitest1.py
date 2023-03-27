import unittest
from Car import Car

class TestCarMethod(unittest.TestCase):
    """Test"""

    def setUp(self):
        self.myCar = Car("TtCarSample", 2020)
        print("Setup is ran.")

    def test_one(self):
        self.assertTrue(self.myCar.year == 2020)


if __name__ == '__main__':
    unittest.main()
