from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional


app = FastAPI()

# Временная база данных
product_list = []
product_id_counter = 1

# BEGIN (write your solution here)
class ProductSpecifications(BaseModel):
    size: str
    color: str
    material: str


class Product(BaseModel):
    name: str
    price: float = Field(..., gt=0)
    specifications: ProductSpecifications


class ProductResponse(BaseModel):
    id: int
    name: str
    price: float


class ProductDetailResponse(ProductResponse):
    specifications: ProductSpecifications


@app.post("/product", response_model=ProductDetailResponse)
async def create_product(product: Product):
    global product_id_counter, product_list

    product_dict = product.model_dump()
    product_dict['id'] = product_id_counter
    product_id_counter += 1
    product_list.append(product_dict)

    return product_dict


@app.get("/products", response_model=List[ProductResponse])
async def get_products():
    return product_list


@app.get("/product/{product_id}", response_model=ProductDetailResponse)
async def get_product(product_id: int):
    for product in product_list:
        if product['id'] == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")
# END