from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine, Base
from typing import Any

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Custom exceptions
class CustomExceptionA(Exception):
    def __init__(self, message: str = "Custom A error"):
        self.status_code = 422
        self.message = message

class CustomExceptionB(Exception):
    def __init__(self, message: str = "Custom B error"):
        self.status_code = 404
        self.message = message

@app.exception_handler(CustomExceptionA)
async def handle_custom_a(request: Request, exc: CustomExceptionA):
    body = schemas.ErrorResponse(code=exc.status_code, message=exc.message)
    return JSONResponse(status_code=exc.status_code, content=body.model_dump())

@app.exception_handler(CustomExceptionB)
async def handle_custom_b(request: Request, exc: CustomExceptionB):
    body = schemas.ErrorResponse(code=exc.status_code, message=exc.message)
    return JSONResponse(status_code=exc.status_code, content=body.model_dump())

# Validation error handler
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    body = schemas.ErrorResponse(code=422, message="Validation Error", details={"errors": exc.errors()})
    return JSONResponse(status_code=422, content=body.model_dump())

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/products", response_model=schemas.ProductOut)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product)

@app.get("/products/{product_id}", response_model=schemas.ProductOut)
def read_product(product_id: int, db: Session = Depends(get_db)):
    p = crud.get_product(db, product_id)
    if not p:
        raise CustomExceptionB(message="Product not found")
    return p

@app.get("/raise_a")
def raise_a():
    raise CustomExceptionA(message="Something went wrong A")

@app.get("/raise_b")
def raise_b():
    raise CustomExceptionB(message="Not found B")

@app.post("/validate_user")
def validate_user(user: schemas.User):
    return {"ok": True, "user": user.model_dump()}
