import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, backref, relation
url = 'postgresql://{}:{}@{}:5432/{}'.format('postgres' ,
                                             '2537300' , 'localhost' , 'postgres')

from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, PickleType
con = sqlalchemy.create_engine(url , echo=False)
Base = declarative_base()
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=con))

class Bot_History(Base):
    __tablename__='bot_history'
    id=Column('id', Integer, primary_key=True)
    dttm=Column(DateTime)
    message=Column(String(400))
    id_chat=Column(Integer)
    username=Column(String(400))
    offset=Column(Integer)

class Bot_Query(Base):
    __tablename__='bot_query'
    id=Column('id', Integer, primary_key=True)
    dttm=Column(DateTime)
    id_chat=Column(Integer)

class LiveJournal_Query(Base):
    __tablename__ = 'livejournal_query'
    id = Column('id', Integer, primary_key=True)
    id_message=Column(Integer)
    state=Column(Integer)




class LiveJournal(Base):
    __tablename__ = 'livejournal'
    id = Column('id', Integer, primary_key=True)
    author = Column(String(400))
    article = Column(String(100000))
    title=Column(String(200))
    dttm = Column(DateTime)

Base.metadata.create_all(con)
Session = sessionmaker(bind=con)
session = Session()

def Add_history(history):
    session.add(history)
    session.commit()

def Add(article):
    journal=LiveJournal(author=article['author'],article=article['article'],
                        dttm=article['dttm'], title=article['title'])
    session.add(journal)

def End():
    session.commit()


def Check(update):
    return session.query(Bot_History).filter(Bot_History.offset==update).count()
