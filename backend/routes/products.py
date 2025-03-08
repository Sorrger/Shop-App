from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from backend.crud.product import get_products, get_product_by_id, add_product, remove_product
from schemas import CreateProducer, CreateProduct

router = APIRouter()

@router.get("/products", response_model=list[CreateProduct])
async def get_all_products(db: Session = Depends(get_db)):
    products = get_products(db)
    return products