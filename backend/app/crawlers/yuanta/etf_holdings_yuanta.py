# 測試區
# import httpx


# API_URL = "https://etfapi.yuantaetfs.com/ectranslation/api/bridge"


# def get_etf_holdings_data(symbol: str):
#     params = {
#         "APIType": "ETFAPI",
#         "CompanyName": "YUANTAFUNDS",
#         "PageName": f"/product/detail/{symbol}/ratio",
#         "DeviceId": "6640008f-f7f4-4217-ba91-6fafc27ccacf",
#         "FuncId": "PCF/Daily",
#         "AppName": "ETF",
#         "Device": "3",
#         "Platform": "ETF",
#         "ticker": symbol,
#     }

#     response = httpx.get(
#         API_URL,
#         params=params,
#         verify=False
#     )

#     print("Status:", response.status_code)

#     response.raise_for_status()

#     return response.json()


# def parse_etf_holdings(data):
#     holdings = []

#     stock_weights = data["FundWeights"]["StockWeights"]

#     for rank, item in enumerate(stock_weights, start=1):
#         holding = {
#             "rank": rank,
#             "stock_symbol": item["code"],
#             "stock_name": item["name"],
#             "weight": item["weights"],
#         }

#         holdings.append(holding)

#     return holdings


# if __name__ == "__main__":
#     symbol = "00850"

#     data = get_etf_holdings_data(symbol)

#     holdings = parse_etf_holdings(data)

#     for holding in holdings:
#         print(holding)

# ---------------------------------------------------------------------------------
import httpx

from sqlalchemy import select

from app.database import SessionLocal
from app.models.etf_info import ETFInfo


API_URL = "https://etfapi.yuantaetfs.com/ectranslation/api/bridge"


def get_etf_holdings_data(symbol: str):
    params = {
        "APIType": "ETFAPI",
        "CompanyName": "YUANTAFUNDS",
        "PageName": f"/product/detail/{symbol}/ratio",
        "DeviceId": "6640008f-f7f4-4217-ba91-6fafc27ccacf",
        "FuncId": "PCF/Daily",
        "AppName": "ETF",
        "Device": "3",
        "Platform": "ETF",
        "ticker": symbol,
    }

    response = httpx.get(
        API_URL,
        params=params,
        verify=False
    )

    print("Status:", response.status_code)

    response.raise_for_status()

    return response.json()


def parse_etf_holdings(data):
    holdings = []

    stock_weights = data["FundWeights"]["StockWeights"]

    for rank, item in enumerate(stock_weights, start=1):
        holding = {
            "rank": rank,
            "stock_symbol": item["code"],
            "stock_name": item["name"],
            "weight": item["weights"],
        }

        holdings.append(holding)

    return holdings


def get_all_etfs():
    db = SessionLocal()

    try:
        statement = select(ETFInfo)

        result = db.execute(statement)

        etfs = result.scalars().all()

        return etfs

    finally:
        db.close()


if __name__ == "__main__":

    etfs = get_all_etfs()

    print("ETF 數量:", len(etfs))

    for etf in etfs:
        print({
            "symbol": etf.symbol,
            "name": etf.name,
            "issuer": etf.issuer
        })
