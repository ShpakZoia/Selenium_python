import unittest

class reg_Test(unittest.TestCase):
    def test_FbReg(self):
        print("this is regestration by Fb")
        self.assertTrue(True)
    
    def test_MailReg(self):
        print("this is regestration by mail")
        self.assertTrue(True)

    def test_TwitterReg(self):
        print("this is regestration by twitter")
        self.assertTrue(True)

if __name__=="__main__":
    unittest.main()