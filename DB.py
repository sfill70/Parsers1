import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, backref, relation
url = 'postgresql://{}:{}@{}:5432/{}'.format('postgres' ,
                                             '2537300' , 'localhost' , 'postgres')

from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, PickleType
con = sqlalchemy.create_engine(url , echo=True)
Base = declarative_base()
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=con))


class LiveJournal(Base):
    __tablename__ = 'livejournal'
    id = Column('id', Integer, primary_key=True)
    author = Column(String(400))
    article = Column(String(1000))
    title=Column(String(200))
    dttm = Column(DateTime)

Base.metadata.create_all(con)
Session = sessionmaker(bind=con)
session = Session()
def Add(article):
    journal=LiveJournal(author=article['author'],article=article['article'],
                        dttm=article['dttm'], title=article['title'])
