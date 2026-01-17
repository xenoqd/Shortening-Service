from fastapi.responses import RedirectResponse
from fastapi import APIRouter, Depends

from backend.schemas.url import UrlCreate, UrlUpdate, UrlRead, UrlStatistics
from backend.db.session import get_session
from backend.services.url import UrlService

from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter(tags=["URL"])


@router.post("/shorten", response_model=UrlRead, status_code=201)
async def create(
    data: UrlCreate,
    session: AsyncSession = Depends(get_session)
    ):
    url = await UrlService.create_url(data, session)
    return url


@router.get("/shorten/{shortcode}", response_model=UrlRead)
async def retrieve(
    shortcode: str,
    session: AsyncSession = Depends(get_session)
    ):
    url = await UrlService.get_url(shortcode, session)
    return url


@router.put("/shorten/{shortcode}", response_model=UrlRead)
async def update_url(
    shortcode: str,
    data: UrlUpdate,
    session: AsyncSession = Depends(get_session),
    ):
    url = await UrlService.update_url(shortcode, session, data)
    return url


@router.delete("/shorten/{shortcode}")
async def delete_url(
    shortcode: str,
    session: AsyncSession = Depends(get_session),
    ):
    url = await UrlService.delete_url(shortcode, session)
    return url


@router.get("/{shortcode}")
async def redirect(
    shortcode: str,
    session: AsyncSession = Depends(get_session)
):
    url = await UrlService.redirect_url(shortcode, session)
    return RedirectResponse(url=url.url)


@router.get("/shorten/{shortcode}/stats", response_model=UrlStatistics)
async def statistics_url(
    shortcode: str,
    session: AsyncSession = Depends(get_session),
    ):
    url = await UrlService.get_url(shortcode, session)
    return url


