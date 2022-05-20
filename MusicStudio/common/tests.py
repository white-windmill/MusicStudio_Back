from django.test import TestCase
from common.models import User
from common.models import PlayList
from common.models import Music
from common.models import PlayListCollection

# class TestUser(TestCase):

#     # def testcase(self) -> None:
#     #     User.objects.create(userid="wuyebf",password="gvrg",username="test")
        
#     # def testcase(self):
#     #     #User.objects.create(userid="wuyebf",password="gvrg",username="test")
#     #     sq=User.objects.filter(userid="wuyebf")
#     #     # print(sq.username)
#     #     self.assertEqual(sq,1)
    
    
import requests
# import unittest
#class UserTest(unittest.TestCase):
class UserTest(TestCase):
    def setUp(self):
        #self.base_url = 'http://124.220.169.238:8000/api/playlist/rank/'
        self.user_url = 'http://124.220.169.238:8000/api/user/'
        #self.auth = ('user001','pass001')

    #GET查询接口username参数
    # def test_get_user(self):
    #     r = requests.get(self.base_url)
    #     result = r.json()
        # self.assertEqual(result['username'],'user001')
        # self.assertEqual(result['email'],'user001@qq.com')

    def test_add_user(self):
        form_data = {'username':'user0016','userid':'5545','password':'bbfgb',}
        r = requests.post(self.user_url,data=form_data)
        result = r.json()
        self.assertEqual(result, {'ret': 0})
