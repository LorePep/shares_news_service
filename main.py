import argparse

from scraping import scrape_interesting_news
from telegram import send_message


def main(url, chat_id, token):
    shares_to_news = scrape_interesting_news(url)
    for share, news in shares_to_news.items():
        msg = _make_message(share, news)
        send_message(msg, chat_id, token)


def _make_message(share, news):
    """
    >>> _make_message("oneShare", "This is one news")
    'oneShare: This is one news'
    """
    return "{}: {}".format(share, news)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="url of the site to be scraped.")
    parser.add_argument("--chat-id", help="telegram chat id for messaging.", required=True)
    parser.add_argument("--telegram-token", help="telegram api token.", required=True)
    args = parser.parse_args()

    main(args.url, args.chat_id, args.telegram_token)