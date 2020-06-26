import unittest

class pay_Test(unittest.TestCase):
    def test_pay_In_dol(self):
        print("payment by dollars")
        self.assertTrue(True)

    def test_Pay_In_Tk(self):
        print("payment by taka")
        self.assertTrue(True)

if __name__=="__main__":
    unittest.main()