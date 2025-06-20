from sqlalchemy import (create_engine, Column, Integer,
                        String, BigInteger, Boolean, DateTime, func, ForeignKey, Numeric)
from sqlalchemy.dialects.mysql import NUMERIC
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, Session
from config import *
from decimal import Decimal
engine = create_engine(f'postgresql+psycopg2://{PG_USER}:{PG_PASS}@{PG_HOST}:{PG_PORT}/{PG_DB}')
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True , autoincrement=True)
    amount = Column(Numeric(12 , 2) , default=0 , nullable=False)
    chat_id = Column(BigInteger)
    fullname = Column(String)
    phone = Column(String)

    def save(self , session):
        session.add(self)
        session.commit()
    @classmethod
    def check_registered(cls , session):
        obj = session.query(cls).filter(id == cls.chat_id).first()
        if not obj:
            return False
        return True

    def __repr__(self):
        return f'User {self.chat_id} , {self.fullname} , {self.phone}'

    def check_phone(self, chat_id, session):
        if chat_id.isdigit():
            user = session.query(User).filter(User.chat_id == chat_id).first()
            if user:
                return True
            else:
                return False
        else:
                return False
    def check_summa(self , chat_id , summa, session):
        user = session.query(User).filter(User.chat_id == chat_id).first()
        if user.amount > Decimal(summa):
            return True
        else:
            return False

    def transfer(self, qabul_qiluvchi_chat_id, beruvchi_chat_id, summa, session):
        qabul_qiluvchi_chat_id = str(qabul_qiluvchi_chat_id)
        beruvchi_chat_id = str(beruvchi_chat_id)
        summa = Decimal(summa)

        user1 = session.query(User).filter(User.chat_id == qabul_qiluvchi_chat_id).first()
        user2 = session.query(User).filter(User.chat_id == beruvchi_chat_id).first()

        if not user1 or not user2:
            return False

        user1.amount += summa
        user2.amount -= summa

        session.commit()
        return True
    @classmethod
    def check_register(cls, session, id_):
        obj = session.query(cls).filter(id_ == cls.chat_id).first()
        if not obj:
            return False
        return True