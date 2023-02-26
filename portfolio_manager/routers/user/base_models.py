from pydantic import BaseModel


class RequestPosition(BaseModel):
    currency: str
    amount: float
