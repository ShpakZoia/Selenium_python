import unittest

def setUpModule():
    print("setup module")

def tearDownModule():
    print("teardown module")

class demo_Keywords(unittest.TestCase):
   
   
    @classmethod
    def setUp(self):
        print("this is the login page")
    
    @classmethod
    def tearDown(self):
        print("this is the logout page")
    
    def test_admin_page(self):
        print("this is the admin page")
    
    def test_about_page(self):
        print("this is the about page")

    def test_faq_page(self):
        print("this is the faq page")
    
    @classmethod
    def setUpClass(cls):
        print("application open")

    @classmethod
    def tearDownClass(cls):
        print("application close")


if __name__ =="__main__":
    unittest.main()