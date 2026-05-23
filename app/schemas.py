from pydantic import BaseModel, EmailStr, conint, constr
from typing import Optional

class ProductCreate(BaseModel):
    title: str
    price: float
    count: int
    description: str

class ProductOut(ProductCreate):
    id: int
    description: str

class ErrorResponse(BaseModel):
    code: int
    message: str
    details: Optional[dict] = None

class User(BaseModel):
    username: str
    age: conint(gt=18)
    email: EmailStr
    password: constr(min_length=8, max_length=16)
    phone: Optional[str] = 'Unknown'