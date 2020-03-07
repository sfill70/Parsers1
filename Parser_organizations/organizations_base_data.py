# import psycopg2
import sqlalchemy
from sqlalchemy import Column, Integer, String, create_engine, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# print("Версия SQLAlchemy:", sqlalchemy.__version__)
# строка подключения к БД через sqlalchemy
url = 'postgresql://{}:{}@{}:5432/{}'.format('test1', '12341234', '195.133.146.22', 'test')
# устанавливаем соединение
con = sqlalchemy.create_engine(url, echo=True)
Base = declarative_base()




class BaseData(Base):
    __tablename__ = 'organizations'
    id = Column(Integer, primary_key=True)
    key = Column(String)
    volume = Column(String)


    def __init__(self, key, volume):
        self.key = key
        self.volume = volume


    def __repr__(self):
        return "<Partners('%s','%s', )>" % (self.key, self.volume)

    @staticmethod
    def session():
        Session = sessionmaker(bind=con)
        session = Session()
        return session

    @staticmethod
    def creat_table():
        Base.metadata.create_all(con)

