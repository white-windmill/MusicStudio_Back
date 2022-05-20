from django.test import TestCase
from common.models import User
from common.models import PlayList
from common.models import Music
from common.models import PlayListCollection
    
import requests
import unittest

class UserTest(TestCase):

    def setUp(self):
        self.user_url = 'http://124.220.169.238:8000/api/sign/'
        self.user_success_id = "1935010205"
        self.user_success_pwd = "12345678"
        self.user_error_id = "1935010205"
        self.user_error_pwd = "475474"

    def test_sign(self):

        #成功实例
        r = requests.get(self.user_url+'?userid='+self.user_success_id+'&password='+
        self.user_success_pwd)
        result = r.json()
        self.assertEqual(result['ret'],0)

        #失败实例
        q = requests.get(self.user_url+'?userid='+self.user_error_id+'&password='+
        self.user_error_pwd)
        result = q.json()
        self.assertEqual(result['ret'],1)

