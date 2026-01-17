from sqlmodel import SQLModel
from datetime import datetime
from typing import Optional


class UrlRead(SQLModel):
    id: int
    url: str
    shortcode: str
    createdAt: datetime
    updatedAt: Optional[datetime] = None


class UrlStatistics(SQLModel):
    id: int
    url: str
    shortcode: str
    createdAt: datetime
    updatedAt: Optional[datetime] = None
    access_count: int


class UrlCreate(SQLModel):
    url: str


class UrlUpdate(SQLModel):
    url: str


class UrlRetrieve(SQLModel):
    shortcode: str
