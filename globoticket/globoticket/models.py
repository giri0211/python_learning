

import decimal
from datetime import date

from globoticket.database import SessionLocal
from sqlalchemy import ForeignKey, select
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    declarative_base,
    mapped_column,
    relationship
)

Base: DeclarativeBase =  declarative_base()

class DBCategory(Base):
    __tablename__ = "category"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] =  mapped_column(unique=True)
    events: Mapped[list["DbEvent"]] = relationship(back_populates="category")
    
class DbEvent(Base):
    __tablename__ = "event"
    
    id: Mapped[int] =  mapped_column(primary_key=True)
    product_code: Mapped[str] =  mapped_column(unique=True)
    date: Mapped[date]
    price: Mapped[decimal.Decimal]
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"))
    category: Mapped["DBCategory"] = relationship(back_populates="events")
    
    def __str__(self):
        return f"{self.id}: {self.product_code:10} {self.date} {self. category.name}"


session = SessionLocal()
results =  session.execute(select(DBCategory)).scalars()
print("\n".join(category.name for category in results))