import unittest

class login(unittest.TestCase):
    def test_FbLogin(self):
        print("this is login by Fb")
        self.assertTrue(True)
    
    def test_MailLogin(self):
        print("this is loging by mail")
        self.assertTrue(True)

    def test_TwitterLogin(self):
        print("this is login by twitter")
        self.assertTrue(True)

if __name__=="__main__":
    unittest.main()