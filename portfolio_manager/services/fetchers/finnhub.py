from datetime import datetime

from finnhub import Client

from settings.constants import FINHUB_API_KEY


class FinhubFetcher:
    def __init__(self, symbol: str) -> None:
        self.symbol = symbol

    def _init_client(self) -> None:
        return Client(FINHUB_API_KEY)

    def _get_params(self, resolution: str) -> dict:
        now = datetime.now()
        _from = int(datetime(now.year, 1, 1, 0, 0, 0, 0).timestamp())  # 1 January of current year
        to = int(now.timestamp())

        return {
            "symbol": f"BINANCE:{self.symbol}USDT",
            "resolution": resolution,
            "_from": _from,
            "to": to,
        }

    def get_crypto_candles(self, resolution: str = "D") -> dict:
        client = self._init_client()
        params = self._get_params(resolution)
        response = client.crypto_candles(**params)
        if response.get("s") == "no_data":
            return {}
        return response
