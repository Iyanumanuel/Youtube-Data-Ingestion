import requests 
import json
from tqdm import tqdm
# from ssl import CHANNEL_BINDING_TYPES
# from main import API_KEY


class YT_stats:

    def __init__(self, api_key, channel_id):
        self.api_key = api_key
        self.channel_id = channel_id
        self.channel_statistics = None
        self.video_data = None

    def get_channel_statistics(self):
        url = f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={self.channel_id}&key={self.api_key}'
        #print(url)
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        #print(data)
        try:
            data = data["items"][0]["statistics"]
        except KeyError:
            data = None

        self.channel_statistics = data
        return data
    
    def get_channel_video_data(self):
        # 1) get video ids
        channel_videos = self._get_channel_videos(limit=50)
        print(len(channel_videos))

        # 2) get video statistics
        parts = ['snippet', 'statistics', 'contentDetails']
        for video_id in tqdm(channel_videos):
            for part in parts:
                data = self._get_single_video_data(video_id, part)
                channel_videos[video_id].update(data)
        
        self.video_data = channel_videos
        return channel_videos


    def _get_single_video_data(self, video_id, part):
        url = f'https://www.googleapis.com/youtube/v3/videos?part={part}&id={video_id}&key={self.api_key}'
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        try:
            data = data['items'][0][part]
        except:
            print('error')
            data = dict()

        return data



    def _get_channel_videos(self, limit=None):
        url = f'https://www.googleapis.com/youtube/v3/search?key={self.api_key}&channelId={self.channel_id}&part=id&order=date'
        if limit is not None and isinstance(limit , int):
            url += '&maxResults=' + str(limit)
#        print(url)
        video, nextPageToken = self._get_channel_videos_per_page(url)
        idx = 0
        while (nextPageToken is not None and idx < 10):
            nexturl = url + "&pageToken=" + nextPageToken
            next_video, nextPageToken = self._get_channel_videos_per_page(nexturl)
            video.update(next_video)
            idx+= 1

        return video

    def _get_channel_videos_per_page(self, url):
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        channel_videos = dict()
        if 'items' not in data:
            return channel_videos, None
        
        item_data = data['items']
        next_page_token = data.get('nextPageToken', None)
        for item in item_data:
            try:
                kind = item['id']['kind']
                if kind == 'youtube#video':
                    video_id = item['id']['videoId']
                    channel_videos[video_id] = dict()
            except KeyError:
                print('error')
        return channel_videos, next_page_token

    def dump(self):
        if self.channel_statistics is None or self.video_data is None:
            print('data is none')
            return 

        fused_data = {self.channel_id: {'channel_statistics': self.channel_statistics, 'video_data': self.video_data}}
        
        channel_title = self.video_data.popitem()[1].get('channelTitle', self.channel_id)
#        channel_title = channel_title.replace(" ", "_").lower()
        file_name = channel_title + '.json'
        with open(file_name, 'w') as f:
            json.dump(fused_data, f, indent=4)

        print('file dumped')

