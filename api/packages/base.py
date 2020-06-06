"""This .py file for alembic migrations
$ alembic revision --autogenerate -m 'init'
$ alembic upgrade head"""

from .database import Base
from .models import links
