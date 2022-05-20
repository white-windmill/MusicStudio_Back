from django.test import TestCase
from common.models import User
from common.models import PlayList
from common.models import Music
from common.models import PlayListCollection
    
import requests
import unittest

class UserTest(TestCase):

    def testcase(self):

        Music.objects.create(musicid="12736812",musicname="test",musicsinger="周杰伦",
        musicalbum="发如雪")
        qs = Music.objects.values()
        qs = qs.filter(musicid="12736812")
        data = list(qs)
        self.assertEqual(data[0]['musicname'],"test")

    def setUp(self):

        self.music_url = 'http://124.220.169.238:8000/api/music/'  
        self.rank_url = 'http://124.220.169.238:8000/api/music/rank/'
        self.playlist_test_name = '白色风车'
        self.playlist_test_error_name = '白色1234245'
        self.playlist_test_userid = '1935010205'
        self.playlist_test_error_userid = '1935010333'
        
    def test_get(self):

        rank = requests.get(self.rank_url)
        result = rank.json()
        self.assertEqual(result['ret'],0)

    def test_post(self):
    
        headers = {"content-type":"application/json"}
        json_data = {'userid':'1935010205','playlistname':'白色风车','musicid':'121244',
        'musicname':'七里香','musicsinger':'周杰伦','musicalbum':"范特西"}
        r = requests.post(self.music_url,json=json_data,headers=headers)
        result = r.json()
        self.assertEqual(result['ret'],0)

    def test_delete(self):

        headers = {"content-type":"application/json"}
        json_data = {'playlistname':'白色风车','musicid':'121244',}        
        r = requests.delete(self.music_url,json=json_data,headers=headers)
        result = r.json()
        self.assertEqual(result['ret'],0)