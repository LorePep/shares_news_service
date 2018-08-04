import json 

import requests

BASE_URL = "https://api.telegram.org/bot{}/"

# send_message sends a text message through a bot to a specified chat_id.
def send_message(text, chat_id, token):
    url = BASE_URL.format(token) + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    _get_url(url)


def _get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content
