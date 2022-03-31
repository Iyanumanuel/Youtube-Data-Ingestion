from youtube_stats import YT_stats

API_KEY = "AIzaSyC9yZ1phQzITxSCUPqpM1GQkiowLa7gHOA"
channel_id = "UCV2xi_w10k6ewdPVxDP6uCQ"

yt = YT_stats(API_KEY, channel_id)
#data = yt.get_channel_statistics()
#yt.dump()
# print(data)

yt.get_channel_video_data()