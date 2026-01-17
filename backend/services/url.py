from backend.utils.shortcode import generate_shortcode
from backend.schemas.url import UrlCreate, UrlUpdate
from backend.repository.url import UrlRepository
from backend.models.url import Url

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from datetime import datetime

from fastapi.exceptions import HTTPException
from fastapi import status


class UrlService:
    @staticmethod
    async def create_url(data: UrlCreate, session: AsyncSession):
        
        while True:
            try:
                shortcode = generate_shortcode()

                url = Url(
                    url=data.url,
                    shortcode=shortcode,
                    createdAt=datetime.utcnow()
                )
                return await UrlRepository.create(session, url)

            except IntegrityError:
                await session.rollback()
                continue


    @staticmethod
    async def get_url(
        shortcode: str,
        session: AsyncSession
    ):
        url = await UrlRepository.get_by_shortcode(session, shortcode)

        if not url:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Not found")
        return url

    @staticmethod
    async def redirect_url(
        shortcode: str,
        session: AsyncSession
    ):
        url = await UrlRepository.get_by_shortcode(session, shortcode)

        if not url:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")


        await UrlRepository.increment_access_count(session, url)
        return url

    @staticmethod
    async def update_url(
        shortcode: str,
        session: AsyncSession,
        data: UrlUpdate
    ):
        url = await UrlRepository.get_by_shortcode(session, shortcode)

        if not url:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
        
        url.url = data.url
        url.updatedAt = datetime.utcnow()

        await UrlRepository.create(session, url)
        return url

    @staticmethod
    async def delete_url(
        shortcode: str,
        session: AsyncSession,
    ):
        url = await UrlRepository.get_by_shortcode(session, shortcode)

        if not url:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")

        await UrlRepository.delete(session, url)


