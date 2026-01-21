from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List


app = FastAPI()

# Временная база данных
product_list = []
product_id_counter = 1

# BEGIN (write your solution here)
class Product(BaseModel):
    name: str = Field(...)
    price: float = Field(...)
    quantity: int = Field(...)

@app.post("/product")
def add_product(product: Product):
    global product_id_counter, product_list
    if product.price <= 0:
        raise HTTPException(
            status_code=422,
            detail=[{
                "msg": "ensure this value is greater than 0",
            }]
        )
    if product.quantity < 0:
        raise HTTPException(
            status_code=422,
            detail=[{
                "msg": "ensure this value is greater than or equal to 0",
            }]
        )
    product_dict = product.dict()
    product_dict["id"] = product_id_counter
    product_list.append(product_dict)
    response_data = {
        "message": "Product added successfully",
        "product": product_dict
    }
    product_id_counter += 1
    return response_data

@app.get("/products")
def get_products():
    return {"products": product_list}
# END
