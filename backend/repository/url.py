from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from backend.models.url import Url


class UrlRepository:
    @staticmethod
    async def get_by_shortcode(
        session: AsyncSession,
        shortcode: str,
    ):
        query = select(Url).where(Url.shortcode == shortcode)
        result = await session.execute(query)
        return result.scalar_one_or_none()

    @staticmethod
    async def create(session: AsyncSession, url: Url):
        session.add(url)
        await session.commit()
        await session.refresh(url)
        return url

    @staticmethod
    async def delete(session: AsyncSession, url: Url):
        await session.delete(url)
        await session.commit()

    @staticmethod
    async def increment_access_count(session: AsyncSession, url: Url):
        url.access_count += 1
        await session.commit()
        await session.refresh(url)
        return url
