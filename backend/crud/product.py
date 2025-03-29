from bson import ObjectId

# === CREATE ===
def add_product(product_data: dict, db):
    result = db.products.insert_one(product_data)
    return str(result.inserted_id) 

# === READ ===
def get_products(db):
    return list(db.products.find({}))

def get_product_by_id(product_id: str, db):
    try:
        product = db.products.find_one({"_id": ObjectId(product_id)})
        if product:
            product["_id"] = str(product["_id"])
            return product
        else:
            raise ValueError(f"Product with id {product_id} does not exist.")
    except Exception as e:
        raise ValueError(f"Invalid product ID format: {product_id}")


# === UPDATE ===
def update_product(product_id: str, update_data: dict, db):
    result = db.products.update_one({"_id": ObjectId(product_id)}, {"$set": update_data})
    if result.matched_count == 0:
        raise ValueError(f"Product with id {product_id} does not exist.")
    return True

# === DELETE ===
def remove_product(product_id: str, db):
    result = db.products.delete_one({"_id": ObjectId(product_id)})
    if result.deleted_count == 0:
        raise ValueError(f"Product with id {product_id} does not exist.")
    return True
