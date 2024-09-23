# YouTube Channel Statistics Data Ingestion

This project provides a Python-based solution for fetching YouTube channel statistics and video data using the YouTube Data API v3. The script allows you to retrieve information such as the number of subscribers, views, and video statistics for a given channel. It also supports fetching metadata and statistics for individual videos in the channel.

## Features
- Retrieve channel statistics (e.g., subscribers, total views, total videos).
- Fetch metadata and statistics for the most recent videos.
- Store the collected data in a structured JSON file.

## Requirements

- Python 3.x
- `requests` library
- `tqdm` library (for progress bar)

To install the required dependencies, run:

```bash
pip install requests tqdm
```

## Usage
### 1. Initialization

To use the script, initialize the YT_stats class with your YouTube Data API Key and the Channel ID of the channel you want to fetch data for.


### 2. Fetch Channel Statistics

You can fetch channel-level statistics (e.g., subscribers, views, etc.) using:

```python
channel_stats = yt.get_channel_statistics()
print(channel_stats)
```

### 3. Fetch Video Data

To fetch data on recent videos, including their metadata and statistics, use:

```python
video_data = yt.get_channel_video_data()
print(video_data)
```

### 4. Save Data to a JSON File

You can save the collected channel and video data to a JSON file for further analysis by calling the dump() method:

```python

yt.dump()
```

The JSON file will be named based on the channel title or the channel ID.

### File Structure
 - `YT_stats` class: Contains methods to fetch and process channel and video statistics.
 - `get_channel_statistics()`: Retrieves statistics of the specified YouTube channel.
 - `get_channel_video_data()`: Fetches metadata and statistics of recent videos on the channel.
 - `dump()`: Saves the fetched data (channel statistics and video data) to a JSON file.

### Limitations
    The script fetches data for the most recent 50 videos by default.
    The YouTube API has a quota limit, so ensure that you manage the API usage appropriately.

### API Documentation

For more details on the YouTube Data API v3, refer to the official documentation: [YouTube Data API v3
License](https://developers.google.com/youtube/v3)

This project is open-source and available under the MIT License.
