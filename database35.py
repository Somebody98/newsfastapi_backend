from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from fastapi import FastAPI
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from models import *

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:parkour2013@localhost/news"

engine = create_engine(
   SQLALCHEMY_DATABASE_URL
)

# создаем сессию подключения к бд
DBSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# создаем модель, объекты которой будут храниться в бд
Base = declarative_base()

# Тестовая модель для базы данных
# class Person(Base):
#    __tablename__ = "people"
#
#    id = Column(Integer, primary_key=True, index=True)
#    name = Column(String)
#    age = Column(Integer)

# Модель с категориями
class Categories(Base):
   __tablename__ = "categories"

   id = Column(Integer, primary_key=True, index=True)
   category = Column(String)



# Модель с новостями
class News(Base):
   __tablename__ = "news"

   id = Column(Integer, primary_key=True, index=True)
   category_news = Column(Integer)
   name = Column(String)
   information = Column(String)


# Модель с информацией о сайте
class Information(Base):
   __tablename__ = "info"

   id = Column(Integer, primary_key=True, index=True)
   information = Column(String)


# создаем таблицы
Base.metadata.create_all(bind=engine)

# создаем сессию подключения к бд
SessionLocal = sessionmaker(autoflush=False, bind=engine)
db = SessionLocal()

#  добавление обьектов в бд
# cat1 = Categories(id = 1,category = 'Политика')
# cat2 = Categories(id = 2, category = 'Экономика')
# cat3 = Categories(id = 3, category = 'Спорт')
# cat4 = Categories(id = 4, category = 'Наука')
#
# db.query(Categories)

# db.add_all([cat1,cat2,cat3,cat4])
# db.commit()

#Вывод news-имени и описания
# first_person = db.get(News, 1)
# print(f"{first_person.id} - {first_person.category_news} - {first_person.name} - {first_person.information}")

#Вывод данных по айди категории
# first_person = db.get(Categories, 1)
# print(f"{first_person.id} - {first_person.category}")

# Вывод данных по фильтру айди > 0, выводится всё
# people = db.query(News).filter(News.id > 0).all()
# for p in people:
#    print(f"{p.id}{p.category_news}{p.name}{p.information}")


# print(tom2.category)
# print(tom3.id,tom3.category)
