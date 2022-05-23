from common.models import User
from common.models import PlayList
from common.models import Music
from common.models import PlayListCollection
from django.test import TestCase    
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

        self.playlist_url = 'http://124.220.169.238:8000/api/playlist/'  
        self.ret_url = 'http://124.220.169.238:8000/api/playlist/ret/'
        self.rank_url = 'http://124.220.169.238:8000/api/playlist/rank/'
        self.playlist_test_name = '白色风车'
        self.playlist_test_error_name = '白色1234245'
        self.playlist_test_userid = '1935010205'
        self.playlist_test_error_userid = '1935010333'
        
    #GET查询userid参数
    def test_get(self):

        r = requests.get(self.playlist_url+'?playlistname='+self.playlist_test_name)
        result = r.json()
        self.assertEqual(result['ret'],0)

        q = requests.get(self.playlist_url+'?playlistname='+self.playlist_test_error_name)
        result = q.json()
        self.assertEqual(result['ret'],1)

        rank = requests.get(self.rank_url)
        result = rank.json()
        self.assertEqual(result['ret'],0)

        ret = requests.get(self.ret_url+'?userid='+self.playlist_test_userid+'&playlistname='+
        self.playlist_test_name)
        result = ret.json()
        self.assertEqual(result['ret'],0)

        ret = requests.get(self.ret_url+'?userid='+self.playlist_test_error_userid+'&playlistname='+
        self.playlist_test_error_name)
        result = ret.json()
        self.assertEqual(result['ret'],0)

    def test_post(self):
        
        headers = {"content-type":"application/json"}
        json_data = {'userid':'1935010205','playlistname':'白色风车'}
        r = requests.post(self.playlist_url,json=json_data,headers=headers)
        result = r.json()
        self.assertEqual(result['ret'],0)

    def test_delete(self):

        headers = {"content-type":"application/json"}
        json_data = {'userid':'1935010205','playlistname':'白色风车'}
        r = requests.delete(self.playlist_url,json=json_data,headers=headers)
        result = r.json()
        self.assertEqual(result['ret'],0)
