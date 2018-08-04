# shares_news_service

A python package to find potentially interesting news related to shares.
One found, the news can be sent through Telegram using a chat bot.

## Installation
`pip install .`

## How to use it
```
shares_news_service [-h] --chat-id CHAT_ID --telegram-token TELEGRAM_TOKEN url_to_scrape_from
```

The command will find the news at the specified `url` and it will send them to the specified `CHAT_ID` with the bot associated with the specified `TELEGRAM_TOKEN`.

## How are news chosen
The news are chosen if they contain any word form a list of keywords of interest.