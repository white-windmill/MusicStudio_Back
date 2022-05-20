from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from common.models import User
from common.models import PlayList
from common.models import Music
from common.models import PlayListCollection
from common.models import PlayList
from common.models import History  
import requests
import unittest

class UserTest(TestCase):

    def setUp(self):

        self.music_url = 'http://124.220.169.238:8000/api/music/'  
        self.rank_url = 'http://124.220.169.238:8000/api/music/rank/'
        self.playlist_test_name = '白色风车'
        self.playlist_test_error_name = '白色1234245'
        self.playlist_test_userid = '1935010205'
        self.playlist_test_error_userid = '1935010333' 
        self.history_url = 'http://124.220.169.238:8000/api/history/'  
        
    def test_get(self):

        r = requests.get(self.history_url+'?userid='+'123456')
        result = r.json()
        self.assertEqual(result['ret'],0)

    def test_post(self):
    
        # userId = request.params['userid']
        # listenTime = request.params['listentime']
        # musicId = request.params['musicid']
        # perception = request.params['perception']
        # musicName = request.params['musicname']
        # musicSigner = request.params['musicsinger']
        # musicAlbym = request.params['musicalbum'] 
        headers = {"content-type":"application/json"}
        json_data = {'userid':'1935010205','musicid':'121244',
        'musicname':'七里香','musicsinger':'周杰伦','musicalbum':"范特西",'perception':'心情不好',
        'listentime':'2023-12-3 12:32'}
        r = requests.post(self.history_url,json=json_data,headers=headers)
        result = r.json()
        self.assertEqual(result['ret'],0)

    def test_delete(self):

        headers = {"content-type":"application/json"}
        json_data = {'playlistname':'白色风车','musicid':'121244',}        
        r = requests.delete(self.music_url,json=json_data,headers=headers)
        result = r.json()
        self.assertEqual(result['ret'],0)