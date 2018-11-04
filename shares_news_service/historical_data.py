import re
from io import StringIO
from datetime import datetime, timedelta

import csv
import requests


DEFAULT_TIMEOUT_SECONDS = 2
QUOTE_LINK = "https://query1.finance.yahoo.com/v7/finance/download/" \
    "{quote}?period1={dfrom}&period2={dto}"\
    "&interval=1d&events=history&crumb={crumb}"

CRUMBLE_LINK = 'https://finance.yahoo.com/quote/{0}/history?p={0}'
CRUMBLE_REGEX = r'CrumbStore":{"crumb":"(.*?)"}'
# self.session = requests.Session()
# self.dt = timedelta(days=days_back)


def get_historical_data(symbol, days_back):
    session = requests.Session()
    crumb = _get_crumb(session, symbol)
    _get_timeseries(session, crumb, symbol, days_back)


def _get_crumb(session, symbol):
    response = session.get(CRUMBLE_LINK.format(symbol), timeout=DEFAULT_TIMEOUT_SECONDS)
    response.raise_for_status()
    match = re.search(CRUMBLE_REGEX, response.text)
    if not match:
        raise ValueError("Could not get crumb from Yahoo Finance")

    return match.group(1)


def _get_timeseries(session, crumb, symbol, days_back):
    now = datetime.utcnow()
    dateto = int(now.timestamp())
    datefrom = int((now - days_back).timestamp())
    url = QUOTE_LINK.format(quote=symbol, dfrom=datefrom, dto=dateto, crumb=crumb)
    response = session.get(url)
    response.raise_for_status()
    data = csv.reader(StringIO(response.text), parse_dates=['Date'])
    print(data)
