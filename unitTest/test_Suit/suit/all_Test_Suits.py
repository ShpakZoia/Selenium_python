import unittest
from package1.login_Test import login
from package1.reg import reg_Test

from package2.payment import pay_Test
from package2.payment_Return import payment_Return_Test

#Getting all test methods
tc1 = unittest.TestLoader().loadTestsFromTestCase(login)
tc2 = unittest.TestLoader().loadTestsFromTestCase(reg_Test)
tc3 = unittest.TestLoader().loadTestsFromTestCase(pay_Test)
tc4 = unittest.TestLoader().loadTestsFromTestCase(payment_Return_Test)

#Creating test suits
sanity_test = unittest.TestSuite([tc1,tc2])
func_test = unittest.TestSuite([tc3,tc4])
master_suit = unittest.TestSuite([tc1,tc2,tc3,tc4])

#running the tests
#unittest.TextTestRunner().run(sanity_test)
#unittest.TextTestRunner().run(func_test)
unittest.TextTestRunner(verbosity=2).run(master_suit)