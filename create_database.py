from sqlalchemy import create_engine, Column, Integer, String, Text, Boolean, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Create a base class for declarative model
Base = declarative_base()

# Define the Articles table
class Article(Base):
    __tablename__ = 'articles'
    
    article_id = Column(Integer, primary_key=True, autoincrement=True)
    arxiv_id = Column(String, unique=True, nullable=False)
    title = Column(Text, nullable=False)
    abstract = Column(Text)
    summary = Column(Text)
    published = Column(TIMESTAMP)
    updated = Column(TIMESTAMP)
    doi = Column(String)
    pdf_link = Column(String)
    html_link = Column(String)
    primary_category = Column(String)
    total_results = Column(Integer)
    search_query = Column(Text)
    favorites = Column(Integer)

# Define the Queries table
class Query(Base):
    __tablename__ = 'queries'
    
    query_id = Column(Integer, primary_key=True, autoincrement=True)
    search_query = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP)

# Define the Authors table
class Author(Base):
    __tablename__ = 'authors'
    
    author_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text, nullable=False)
    university_id = Column(Integer, ForeignKey('universities.university_id'), nullable=False)
    
    # Relationship
    university = relationship("University")

# Define the Universities table
class University(Base):
    __tablename__ = 'universities'
    
    university_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text, unique=True, nullable=False)
    location = Column(Text)

# Define the ArticleAuthors table (Many-to-Many relationship)
class ArticleAuthor(Base):
    __tablename__ = 'article_authors'
    
    article_id = Column(Integer, ForeignKey('articles.article_id'), primary_key=True)
    author_id = Column(Integer, ForeignKey('authors.author_id'), primary_key=True)
    contribution = Column(Text, default=None)
    primary_author = Column(Boolean, default=False)

# Define the Keywords table
class Keyword(Base):
    __tablename__ = 'keywords'
    
    keyword_id = Column(Integer, primary_key=True, autoincrement=True)
    keyword = Column(Text, unique=True, nullable=False)

# Define the ArticleKeywords table (Associative table for Many-to-Many relationship)
class ArticleKeyword(Base):
    __tablename__ = 'article_keywords'
    
    article_id = Column(Integer, ForeignKey('articles.article_id'), primary_key=True)
    keyword_id = Column(Integer, ForeignKey('keywords.keyword_id'), primary_key=True)

# Define the Users table
class User(Base):
    __tablename__ = 'users'
    
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    date_created = Column(TIMESTAMP)
    license = Column(Boolean, default=False)
    favorites = Column(Text)  # Comma-separated list of article_ids
    university_id = Column(Integer, ForeignKey('universities.university_id'))
    author_id = Column(Integer, ForeignKey('authors.author_id', ondelete='SET NULL'))

# Define the Comments table
class Comment(Base):
    __tablename__ = 'comments'
    
    comment_id = Column(Integer, primary_key=True, autoincrement=True)
    article_id = Column(Integer, ForeignKey('articles.article_id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP)

# Define the Favorites table
class Favorite(Base):
    __tablename__ = 'favorites'
    
    user_id = Column(Integer, ForeignKey('users.user_id'), primary_key=True)
    article_id = Column(Integer, ForeignKey('articles.article_id'), primary_key=True)
    favorited_at = Column(TIMESTAMP)

# Create the SQLite database
DATABASE_URI = 'sqlite:///_Data/hci_database.sqlite3'
engine = create_engine(DATABASE_URI)

# Create all tables
Base.metadata.create_all(engine)

print("Database 'hci_database.sqlite3' created successfully with all tables.")
