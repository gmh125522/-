import unittest
from testcase import test_login, test_reg

suite = unittest.TestSuite()
#suite.addTests([test_reg('test_login_normal'),test_reg('test_login_password_wrong')])
#suite.addTest(test_reg.TestLogin("test_login_normal"))
#suite.addTest(test_login.TestLogin("test_login_normal"))
loader = unittest.TestLoader()
suite1 = loader.loadTestsFromModule(test_reg)
suite2 = loader.loadTestsFromModule(test_login)
if __name__=="__main__":
    print(suite1)
    print(suite2)
    print(suite1.countTestCases())
    print(suite2.countTestCases())
    #执行suite
    unittest.TextTestRunner(verbosity=1).run(suite1)
    unittest.TextTestRunner(verbosity=1).run(suite2)