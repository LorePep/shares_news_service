import argparse

from scraping import scrape
from telegram import send_message


def main(url, chat_id, token):
    shares_to_news = scrape(url)
    for share, news in shares_to_news.items():
        msg = _make_message(share, news)
        send_message(msg, chat_id, token)


def _make_message(share, news):
    return "{}: {}\n".format(share, news)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="url of the site to be scraped.")
    parser.add_argument("--chat-id", help="telegram chat id for messaging.", required=True)
    parser.add_argument("--telegram-token", help="telegram api token.", required=True)
    args = parser.parse_args()

    main(args.url, args.chat_id, args.telegram_token)