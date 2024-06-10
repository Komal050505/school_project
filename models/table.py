from sqlalchemy import Column, String, Integer, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class School_table(Base):
    __tablename__ = "school_data"

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String(50))
    rank = Column("rank", String(100))
    fees = Column("fees", Integer)

