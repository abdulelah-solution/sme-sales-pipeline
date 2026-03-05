from sqlalchemy.orm import Session
from sqlalchemy import select
from src.models import Product, Sale
from config import logging

logger = logging.getLogger(__name__)

def create_product(name: str, price: float, stock: int, db: Session):
    ''' Adding a new product to the database '''
    try:
        new_product = Product(
                        name = name,
                        price = price,
                        stock_quantity = stock
                    )
        db.add(new_product)
        db.commit()
        db.refresh(new_product)
        logger.info(f"➕ Product added: {name} (ID: {new_product.id})")
        return new_product
    
    except Exception as e:
        db.rollback()
        logger.error(f"❌ Error adding product {name}: {e}")
        return None


def create_sale(product_id: int, quantity: int, total_price: float, db: Session):
    ''' Recording a sale transaction and updating product inventory '''
    try:
        # 1. Search for the product to ensure its availability and stock availability.
        product = db.scalars(select(Product).filter(Product.id == product_id)).first()

        if not product:
            logger.warning(f"⚠️ Sale skipped: Product ID {product_id} not found.")
            return None

        # 2. Sales Recording
        new_sale = Sale(
                    product_id = product_id,
                    quantity = quantity,
                    total_price = total_price
                    )
        
        # 3. Inventory update (sold quantity less than available)
        product.stock_quantity -= quantity

        db.add(new_sale)
        db.commit()
        db.refresh(new_sale)

        logger.info(f"💰 Sale recorded: ID {new_sale.id} for Product {product.name}")
        return new_sale

    except Exception as e:
        db.rollback()
        logger.error(f"❌ Error recording sale for Product ID {product_id}: {e}")
        return None