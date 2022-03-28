

from ssl import CHANNEL_BINDING_TYPES
from main import API_KEY


class YT_stats:

    def _init_(self, api_key, channel_id):
        self.api_key = api_key
        self.channel_id = channel_id
        self.channel_statistics = None

    def get_channel_statistics(self):
        url = f''