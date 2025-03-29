from .mysql import engine, Base
from models import producer, user

def init_db():
    Base.metadata.create_all(bind=engine)
