import unittest

class app_test(unittest.TestCase):
    def test_app_Name(self):
        #self.assertGreater(100,10)
        #self.assertGreater(10,100)
        #self.assertGreaterEqual(100,100)
        #self.assertLess(10,100)
        #self.assertLess(100,10)
        #self.assertLessEqual(10,100)
        self.assertLessEqual(100,100)


if __name__=="__main__":
    unittest.main()