from typing import Optional
from sqlmodel import SQLModel, Field

from datetime import datetime


class Url(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    url: str = Field(index=True, nullable=False)
    shortcode: str = Field(index=True, unique=True, nullable=False)
    access_count: int = Field(default=0)
    createdAt: datetime = Field(default_factory=datetime.utcnow)
    updatedAt: Optional[datetime] = Field(default=None, nullable=True)
