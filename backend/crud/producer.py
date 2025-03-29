from sqlalchemy.orm import Session
from models.producer import Producer

#create
#read

def get_producer(db: Session):
    return db.query(Producer).all()

def get_producer_by_id(db: Session, producer_id: int):
    db_product = db.query(Producer).filter(Producer.id == producer_id).first()
    if db_product:
        return db_product
    else:
        raise ValueError(f"Product with id {producer_id} does not exist.")
#update
#delete