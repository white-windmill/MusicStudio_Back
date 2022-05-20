from django.test import TestCase
from common.models import User
from common.models import PlayList
from common.models import Music
from common.models import PlayListCollection
    
import requests
import unittest

class UserTest(TestCase):

    def testcase(self):
        User.objects.create(userid="wuyebf",password="gvrg",username="test")
        qs = User.objects.values()
        qs = qs.filter(userid="wuyebf")
        data = list(qs)
        self.assertEqual(data[0]['username'],"test")

    def setUp(self):
        self.user_url = 'http://124.220.169.238:8000/api/user/'

    #GET查询userid参数
    def test_get_user(self):

        r = requests.get(self.user_url+'?userid='+'123456')
        result = r.json()
        self.assertEqual(result['ret'],1)

        q = requests.get(self.user_url+'?userid='+'1935010205')
        result = q.json()
        self.assertEqual(result['ret'],0)

    def test_add_user(self):
        form_data = {'username':'user0016','userid':'5545','password':'bbfgb',}
        r = requests.post(self.user_url,data=form_data)
        result = r.json()
        self.assertEqual(result, {'ret': 0})
