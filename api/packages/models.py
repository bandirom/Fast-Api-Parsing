from .database import Base
from sqlalchemy import Column, String, Integer, Boolean


class Links(Base):
    __tablename__ = 'links'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String(350))
    url = Column(String)
    context = Column(String)
    is_main = Column(Boolean, default=False)


links = Links.__table__
