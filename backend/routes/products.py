from fastapi import APIRouter, Depends, HTTPException
from database.mongo import get_mongo_db
from schemas.product import CreateProduct
from crud.product import get_product_by_id, get_products  

router = APIRouter()

@router.get("/products", response_model=list[CreateProduct])
async def get_all_products(db=Depends(get_mongo_db)):  
    products = get_products(db)
    for product in products:
        product["_id"] = str(product["_id"])
        if "producer_id" in product:
            product["producer_id"] = str(product["producer_id"])  

    return [CreateProduct(**product) for product in products]

@router.get("/products/{id}", response_model=CreateProduct)
async def get_product(id: str, db=Depends(get_mongo_db)):  
    product = get_product_by_id(id, db)
    
    if not product:
        raise HTTPException(status_code=404, detail="Produkt nie znaleziony")

    if isinstance(product.get('producer_id'), int):
        product['producer_id'] = str(product['producer_id'])
    
    return CreateProduct(**product)



