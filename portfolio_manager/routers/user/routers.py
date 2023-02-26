from datetime import datetime

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from routers.user.models import User, Position
from routers.user.base_models import RequestPosition

from services.fetchers.finnhub import FinhubFetcher
from services.algorithms.year_to_date import YearToDate

from utils.jwt import get_current_user

router = APIRouter(
    prefix="/user",
    responses={404: {"description": "Not found"}},
)


@router.get("/portfolio")
async def get_user_portfolio(user: User = Depends(get_current_user)):
    positions = await user.positions
    return JSONResponse(positions)


@router.post("/portfolio")
async def updet_user_portfolio(
    request_position: RequestPosition, user: User = Depends(get_current_user)
) -> RequestPosition:
    position, _ = await Position.update_or_create(
        amount=request_position.amount,
        defaults={
            "user": user,
            "created": datetime.now().date(),
            "currency": request_position.currency,
            "updated": datetime.now().date(),
        },
    )
    return position


@router.get("/ytd")
async def get_ytd(symbol: str, user: User = Depends(get_current_user)):
    position = await Position.filter(currency=symbol, user=user).first()
    if not position:
        return JSONResponse({"ytd": 0})

    candles = FinhubFetcher(symbol).get_crypto_candles()
    if not candles:
        return JSONResponse({"ytd": 0})

    return JSONResponse({"ytd": YearToDate(candles)(position.amount)})


@router.get("/ytd_aggregation")
async def get_ytd(symbol: str, aggregation_fun: str, user: User = Depends(get_current_user)):
    print(symbol, aggregation_fun)
    amounts = await Position.filter(currency=symbol, created_dt__year=datetime.now().year, user=user).values_list(
        "amount", flat=True
    )
    if not amounts:
        return JSONResponse({aggregation_fun: 0})

    candles = FinhubFetcher(symbol).get_crypto_candles()
    if not candles:
        return JSONResponse({aggregation_fun: 0})

    year_to_date = YearToDate(candles)

    aggregation_method = getattr(year_to_date, aggregation_fun)
    if not aggregation_method:
        return JSONResponse({aggregation_fun: 0})

    value = aggregation_method(amounts)

    return JSONResponse({aggregation_fun: value})
