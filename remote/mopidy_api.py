import logging
import json
import requests

logger = logging.getLogger(__name__)

url = "http://10.0.0.123:8888/mopidy/rpc"
headers = {'content-type': 'application/json'}
error = "error"

### Helper functions ###
def handle_error(response, func):
    if error in response:
        logger.error("Error in response to " + func.__name__)

def send_json(payload, func):
    logger.debug("Mopidy Request: " + json.dumps(payload))
    response = requests.post(
        url, data=json.dumps(payload), headers=headers).json()
    handle_error(response, func)
    logger.debug("Mopidy Response: " + str(response))
    return response


### Main Methods ###

def play(tlid):
    # Example echo method
    payload = {
        "method": "core.playback.play",
        "params": {"tlid" : tlid},
        "jsonrpc": "2.0",
        "id": 0
    }
    send_json(payload, play)

    # assert response["result"] == "echome!"
    # assert response["jsonrpc"]
    # assert response["id"] == 0

def pause():
    payload = {
        "method": "core.playback.pause",
        "jsonrpc": "2.0",
        "id": 0
    }
    send_json(payload, pause)

def resume():
    payload = {
        "method": "core.playback.resume",
        "jsonrpc": "2.0",
        "id": 0
    }
    send_json(payload, resume)

def vol(percent):
    payload = {
        "method": "core.mixer.set_volume",
        "params": {"volume": percent},
        "jsonrpc": "2.0",
        "id": 0
    }
    send_json(payload, resume)

def get_youtube(videoId):
    payload = {
        "method": "core.tracklist.add",
        "jsonrpc": "2.0",
        "params": {"uris": ["yt:" + videoId]},
        "id": 0
    }
    response = send_json(payload, get_youtube)
    tlid = response['result'][0]['tlid']
    return tlid


def clear_tracklist():
    payload = {
        "method": "core.tracklist.clear",
        "jsonrpc": "2.0",
        "id": 0
    }
    send_json(payload, clear_tracklist)

# clear_tracklist()
# play(get_youtube("qIF8xvSA0Gw"))