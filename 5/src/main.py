from fastapi import FastAPI, Body
from typing import Optional

app = FastAPI()

# BEGIN (write your solution here)
from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str
    age: Optional[int] = None

@app.post("/users")
async def create_user(user: UserCreate):
    user_data = user.dict()
    user_data["status"] = "User created"
    return user_data
# END
