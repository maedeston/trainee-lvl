from sqlalchemy import Column,Integer,String,Boolean,Float,ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base

class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing':True}

    user_id = Column(Integer,primary_key=True,nullable=False)
    email = Column(String,nullable=False,unique=True)
    password = Column(String,nullable=False)

class Bank_Client(Base):
    __tablename__ = 'bank_clients'
    bank_client_id = Column(Integer, primary_key=True, nullable=False)

    tax_id = Column(Integer, unique=True ,nullable=False)

class Bank_product(Base):
    __tablename__ = 'bank_product'

    products = Column(String, nullable=False)
    product_id = Column(Integer, primary_key=True, nullable=False)

class Card(Bank_product):
    __tablename__ = 'cards'

    card_id = Column(Integer, primary_key=True, nullable=False)
    card_valid_until = Column(Integer, nullable=False)
    card_owner = Column(String, nullable=False)
    card_balance = Column(Integer)
    cvv = Column(Integer, unique=True, nullable=False)
    code = Column(Integer, unique=True, nullable=False)
    data = Column(Integer, nullable=False)

class BC_pshysique_litso(Bank_Client):
    __tablename__ = 'bc_pshysique_litso'
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)

class BC_company(Bank_Client):
    __tablename__ = 'bank_company'

    name = Column(String, nullable=False)


class Account(Base):
    __tablename__ = 'accounts'
    __table_args__ = {'extand_existing': True}

    account_id = Column(Integer, primary_key=True, nullable=False)
    account_balance = Column(Float)

class Transaction(Base):
    __tablename__ = 'transactions'

    transaction_id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users', 'accounts.account_id', ondelete="CASCADE"), nullable=False)
    AFrom = Column(Integer, ForeignKey('accounts.account_id', ondelete="CASCADE"),nullable=False)
    Ato = Column(Integer, ForeignKey('accounts.account_id', ondelete="CASCADE"))
    count =  Column(Float, nullable=False)