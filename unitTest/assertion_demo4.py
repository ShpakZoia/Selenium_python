import unittest

class app_test(unittest.TestCase):
    def test_app_Name(self):
        t_list = {"python","is","fun"}
        #self.assertIn("python",t_list)
        #self.assertNotIn("python",t_list)
        self.assertNotIn("python1",t_list)

if __name__=="__main__":
    unittest.main()