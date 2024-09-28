from datetime import datetime
from sqlalchemy import create_engine, text
import urllib.request as libreq

SQLITE_URI = "sqlite:///_Data/hci_database.sqlite3"

engine = create_engine(SQLITE_URI)

api_base_url = f'http://export.arxiv.org/api/{method_name}?{parameters}'


with libreq.urlopen('http://export.arxiv.org/api/query?search_query=all:electron&start=0&max_results=1') as url:
    r = url.read()
    print(r)

    