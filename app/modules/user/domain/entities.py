from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from sqlalchemy import String, DateTime, Boolean, ForeignKey
from app.config.db import Base
from app.modules.auth.domain.entities import Role


class Country(Base):
    __tablename__ = "countries"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    code: Mapped[str] = mapped_column(String(5), unique=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)
    created_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __str__(self):
        return self.name


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    country_id: Mapped[int] = mapped_column(ForeignKey("countries.id"), index=True)
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"), index=True)
    city: Mapped[str] = mapped_column(String(20))
    document_type: Mapped[str] = mapped_column(String(3))
    document_number: Mapped[str] = mapped_column(String(20), unique=True)
    email: Mapped[str] = mapped_column(String(256), unique=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    lastname: Mapped[str] = mapped_column(String(50))
    name: Mapped[str] = mapped_column(String(50))
    password: Mapped[str] = mapped_column(String(256))
    created_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    country: Mapped["Country"] = relationship()
    role: Mapped["Role"] = relationship()

    def __str__(self):
        return self.name
