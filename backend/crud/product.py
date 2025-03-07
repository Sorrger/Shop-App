from sqlalchemy.orm import Session
from models import Product
from schemas import CreateProduct

#create
def add_product(db: Session, product: CreateProduct):
    db_product = Product(name=product.name, photo_url=product.photo_url,
                         description=product.description, price=product.price,
                          producer_id= product.producer_id )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

#read
def get_products(db: Session):
    return db.query(Product).all()

def get_product_by_id(db: Session, product_id: int):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product:
        return db_product
    else:
        raise ValueError(f"Product with id {product_id} does not exist.")

#update

#delete
def remove_product(db: Session, product_id: int):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return db_product
    else:
        raise ValueError(f"Product with id {product_id} does not exist.")