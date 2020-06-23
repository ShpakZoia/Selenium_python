import unittest

class app_test(unittest.TestCase):
    @unittest.SkipTest
    def test_admin_page(self):
        print("this is the admin page")
    
    @unittest.skip("this is not ready lol")
    def test_about_page(self):
        print("this is the about page")
    @unittest.skipIf(1==1, "because one is equal to one")
    def test_faq_page(self):
        print("this is the faq page")

    def test_home_page(self):
        print("this is home page")

    def test_customer_page(Self):
        print("this is customer page")

if __name__=="__main__":
    unittest.main()