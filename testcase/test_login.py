import unittest
import requests
from lib import db
from lib import load_data
from lib.case_log import log_case_info
from conf import config
import  json
# 声明一个测试类,基础 unittest.TestCase
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):#整个测试类的测试方法，只执行一次
       cls.skeet = load_data.get_sheet(config.data_file,"登录")

    @unittest.skipUnless(db.check_user("张三"), "跳过该测试用例")
    def test_user_login_normal(self):
        case_data = load_data.get_case(self.skeet,"test_user_login_normal")
        url = case_data[2]
        data =json.loads(case_data[3])
        #excepted_res = json.loads(case_data[4])
        res = requests.post(url=url, data=data)
        log_case_info("test_user_login_normal",url,case_data[3],case_data[4],res.text)
        self.assertIn("登录成功", res.text)

    def test_user_login_password_wrong(self):
        case_data = load_data.get_case(self.skeet, "test_user_login_password_wrong")
        url = case_data[2]
        data = json.loads(case_data[3])
        res = requests.post(url=url, data=data)
        log_case_info("test_user_login_password_wrong", url, case_data[3], case_data[4], res.text)
        self.assertIn("用户名或密码错误", res.text)


if __name__ == "__main__":
    unittest.main(verbosity=2)