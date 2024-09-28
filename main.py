from datetime import datetime
from sqlalchemy import create_engine, text

SQLITE_URI = "sqlite:///_Data/hci_database.sqlite3"

engine = create_engine(SQLITE_URI)#
