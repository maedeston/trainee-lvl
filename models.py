from sqlalchemy import Column,Integer,String, Float

from app.database import Base

class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing':True}

    user_id = Column(Integer,primary_key=True,nullable=False)
    email = Column(String,nullable=False,unique=True)
    password = Column(String,nullable=False)

class Account(Base):
    __tablename__ = 'accounts'
    __table_args__ = {'extand_existing': True}

    account_id = Column(Integer, primary_key=True, nullable=False)
    account_balance = Column(Float)

class implage(Base):
    __tablename__ = 'implage'
    __table_args__ = {'extand_existing': True}

    date_rotation = Column(Integer, nullable=False)
    current_salary = Column(Integer, nullable=False)


