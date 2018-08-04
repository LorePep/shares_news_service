import json 

import requests

TELEGRAM_BOT_URL = "https://api.telegram.org/bot{}/"

# send_message sends a text message through a bot to a specified chat_id.
def send_message(text, chat_id, token):
    url = _get_url_for_bot(text, chat_id, token)
    _get_response(url)


def _get_response(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def _get_url_for_bot(text, chat_id, token):
    """
    >>> _get_url_for_bot("some text", "one_id", "one_token")
    'https://api.telegram.org/botone_token/sendMessage?text=some text&chat_id=one_id'
    """
    return TELEGRAM_BOT_URL.format(token) + "sendMessage?text={}&chat_id={}".format(text, chat_id)