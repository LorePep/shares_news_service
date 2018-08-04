from urllib.request import Request, urlopen

from bs4 import BeautifulSoup

KEYWORDS = [
    "result", "results", "report", "reports",
    "exceeding", "expectations", "positive",
    "favourable", "profit", "up",
    "excellent", "transformational", "acquisition",
]

NEWS_HTML_TAG_ATTR = {"class": "m", "colspan": "2"}
SHARES_HTML_TAG_ATTR = {"class": "mb", "align": "right", "valign": "top"}


# scape scrapes a site to gather news about potentially useful shares.
def scrape(url): 
    soup = _get_soup_from_url(url)
    
    news = soup.findAll("td", attrs=NEWS_HTML_TAG_ATTR)
    shares_names = soup.findAll("td", attrs=SHARES_HTML_TAG_ATTR)    

    return _get_interesting_shares_to_news(news, shares_names)



def _get_interesting_shares_to_news(news, names):
    interesting_shares_to_news = {}

    for n, share in zip(news, names):
        text = n.get_text()
        words = _get_words_from_text(text)
        try:
            name = _get_share_name(share.get_text())
        except ValueError as e:
            print("failed to fetch name %s", e)
            continue
        if _is_news_interesting(words):
            interesting_shares_to_news[name] = text
        
    return interesting_shares_to_news


def _get_soup_from_url(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req)
    return BeautifulSoup(page, "html.parser")


def _get_words_from_text(text):
    if not text:
        return []
    split = text.split()
    return [s.replace(",", "").lower() for s in split]


def _is_news_interesting(words):
    if not words:
        return False

    for k in KEYWORDS:
        if k in words:
            return True

    return False


def _get_share_name(text):
    if not text:
        raise ValueError("Share name is None.")

    split = text.split()
    if len(split) != 2:
        raise ValueError("Uknown share naming format.")

    return split[0]