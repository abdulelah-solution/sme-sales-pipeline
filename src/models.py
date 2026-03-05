from sqlalchemy import String, Numeric, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from decimal import Decimal
from datetime import datetime
from .database import Base


# Products Class (Table)
class Product(Base):
    ''' Representation of the products table in the database '''
    __tablename__ = 'products'

    # Attributes (Columns)
    id: Mapped[int] = mapped_column(primary_key = True)
    name: Mapped[str] = mapped_column(String(100), index = True)
    price: Mapped[Decimal] = mapped_column(Numeric(precision = 10, scale = 2))
    stock_quantity: Mapped[int] = mapped_column(default = 0)

    # One-to-Many Relationship: A single product has multiple sales.
    sales: Mapped[List['Sale']] = relationship(
                                        back_populates = 'product',
                                        cascade = 'all, delete-orphan'
                                    )

    def __repr__(self) -> str:
        return f"<Product(name = '{self.name}', price = {self.price})>"
    

# Sales Class (Table)
class Sale(Base):
    ''' A representation of the sales table and it is linked to the products table. '''
    __tablename__ = 'sales'

    # Attributes (Columns)
    id: Mapped[int] = mapped_column(primary_key = True)
    product_id: Mapped[int] = mapped_column(ForeignKey('products.id'))
    sale_date: Mapped[datetime] = mapped_column(server_default = func.now())
    quantity: Mapped[int] = mapped_column(nullable = False)
    total_price: Mapped[Decimal] = mapped_column(Numeric(precision = 10, scale = 2))

    # (Many-to-one) relationship: A single sale pertains to a single product.
    product: Mapped['Product'] = relationship(back_populates = 'sales')

    def __repr__(self) -> str:
        return f"<Sale(product_id = {self.product_id}, qty = {self.quantity}, total = {self.total_price})>"