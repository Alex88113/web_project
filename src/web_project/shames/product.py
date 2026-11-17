from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field
from sqlalchemy import DateTime, Numeric, String, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class ProductBase(DeclarativeBase):
    pass

class ProductOrm(ProductBase):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(50), nullable=False)
    price: Mapped[float | int] = mapped_column(Numeric(10, 2), nullable=False)
    quantity: Mapped[int] = mapped_column(nullable=False)

    description: Mapped[str | None]
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    update_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

class ProductCreate(BaseModel):
    title: str = Field(min_length=3, max_length=50, description="The title a product")
    price: float = Field(gt=0, description="the price of the product")
    quantity: int = Field(gt=0)
    description: str | None

class Product(ProductCreate):
    id: int = Field(gt=0)

    config = ConfigDict(from_attributes=True)
