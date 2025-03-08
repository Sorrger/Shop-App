from fastapi import APIRouter, Depends
from database.mongo import get_mongo_db
from schemas.product import CreateProduct
from crud.product import get_products  

router = APIRouter()

@router.get("/products", response_model=list[CreateProduct])
async def get_all_products(db=Depends(get_mongo_db)):  
    products = get_products(db)
    for product in products:
        product["_id"] = str(product["_id"])
        if "producer_id" in product:
            product["producer_id"] = str(product["producer_id"])  

    return [CreateProduct(**product) for product in products]
