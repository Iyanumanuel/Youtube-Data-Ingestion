from yt_stats import YTstats

API_KEY = "AIzaSyC9yZ1phQzITxSCUPqpM1GQkiowLa7gHOA"
channel_id = 'UCV2xi_w10k6ewdPVxDP6uCQ'

yt = YTstats(API_KEY, channel_id)

yt.get_channel_statistics()