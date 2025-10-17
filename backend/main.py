from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

# --- テーブルを作成 ---
models.Base.metadata.create_all(bind=engine)

# --- FastAPIアプリ生成 ---
app = FastAPI()


# --- DBセッションを取得するための依存関数 ---
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_name_by_password(db, name = user.name, password=user.password)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.get("/users/id/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.get("/users/name/{name}", response_model=schemas.User)
def read_user_by_name(name: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_name(db, name=name)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.post("/sales/", response_model=schemas.Sales)
def create_sales(sales: schemas.SalesCreate, db: Session = Depends(get_db)):
    db_sales = crud.get_sales_by_year(db, year=sales.year)
    if db_sales:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_sales(db=db, sales=sales)

@app.get("/sales/{year}", response_model=schemas.Sales)
def get_sales_by_year(year: int, db: Session = Depends(get_db)):
    db_year = crud.get_sales_by_year(db, year=year)
    if db_year is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_year