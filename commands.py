from remote import youtube_api, mopidy_api
import logging

logger = logging.getLogger(__name__)

def play_youtube(search_terms):
    search_results = youtube_api.service.search().list(part="snippet", q=search_terms, maxResults=2).execute()
    videoId = search_results['items'][0]['id']['videoId']
    video_title = search_results['items'][0]['snippet']['title']
    logger.info("Youtube VideoId: " + videoId)
    logger.info("Youtube Title: " + video_title)
    tlid = mopidy_api.get_youtube(videoId)
    mopidy_api.play(tlid)
    return video_title

def pause():
    logger.info("Music Pause")
    mopidy_api.pause()

def resume():
    logger.info("Music Resume")
    mopidy_api.resume()

def vol(percent):
    logger.info("Music Volume: " + str(percent) + "%")
    mopidy_api.vol(percent)