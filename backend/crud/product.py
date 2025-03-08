from database import mongo_products
from bson import ObjectId

def add_product(product_data: dict):
    result = mongo_products.insert_one(product_data)
    return str(result.inserted_id) 

# === READ ===
def get_products():
    return list(mongo_products.find({}))

def get_product_by_id(product_id: str):
    try:
        product = mongo_products.find_one({"_id": ObjectId(product_id)})
        if product:
            return product
        else:
            raise ValueError(f"Product with id {product_id} does not exist.")
    except Exception as e:
        raise ValueError(f"Invalid product ID format: {product_id}")

# === UPDATE ===
def update_product(product_id: str, update_data: dict):
    result = mongo_products.update_one({"_id": ObjectId(product_id)}, {"$set": update_data})
    if result.matched_count == 0:
        raise ValueError(f"Product with id {product_id} does not exist.")
    return True

# === DELETE ===
def remove_product(product_id: str):
    result = mongo_products.delete_one({"_id": ObjectId(product_id)})
    if result.deleted_count == 0:
        raise ValueError(f"Product with id {product_id} does not exist.")
    return True
