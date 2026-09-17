# from app.crawlers.yuanta.etf_info_yuanta import (
#     get_etf_data as yuanta_get_etf_data,
#     parse_etf_data as yuanta_parse_etf_data,
# )

# from app.crawlers.fubon.etf_info_fubon import (
#     get_etf_info as fubon_get_etf_info,
# )


# def search_etfs(keyword: str):

#     keyword = keyword.strip()

#     if not keyword:
#         return []

#     results = []

#     # =========================
#     # 1. 搜尋元大
#     # =========================

#     yuanta_data = yuanta_get_etf_data()

#     yuanta_etfs = yuanta_parse_etf_data(yuanta_data)

#     yuanta_matches = [
#         etf
#         for etf in yuanta_etfs
#         if keyword.lower() in etf["symbol"].lower()
#         or keyword.lower() in etf["name"].lower()
#     ]

#     results.extend(
#         {
#             "source": "yuanta",
#             **etf,
#         }
#         for etf in yuanta_matches
#     )

#     # =========================
#     # 2. 找出可能的 ETF 代碼
#     # =========================

#     symbols = {
#         etf["symbol"]
#         for etf in yuanta_matches
#     }

#     # =========================
#     # 3. 用代碼查富邦
#     # =========================

#     for symbol in symbols:

#         try:
#             fubon_etf = fubon_get_etf_info(symbol)

#             results.append(
#                 {
#                     "source": "fubon",
#                     **fubon_etf,
#                 }
#             )

#         except Exception as e:
#             print(f"富邦查詢失敗 {symbol}: {e}")

#     return results

# ----------------------------------------------------------------------------------

import asyncio
from typing import List
from app.crawlers.etf_base import BaseETFCrawler
from app.crawlers.yuanta.etf_info_yuanta import YuantaETFCrawler
from app.crawlers.fubon.etf_info_fubon import FubonETFCrawler
from app.schemas.etf_schemas import ETFInfoResponse

class ETFService:
    def __init__(self):
        # 註冊目前支援的所有券商爬蟲，未來要加國泰、群益，直接在這裡加入 class 即可
        self.crawlers: List[BaseETFCrawler] = [
            YuantaETFCrawler(),
            FubonETFCrawler(),
        ]

    async def search_etf(self, symbol: str) -> ETFInfoResponse:
        # 同時打給元大與富邦
        tasks = [crawler.fetch_etf_info(symbol) for crawler in self.crawlers]
        results = await asyncio.gather(*tasks)

        # 過濾出非 None 的合法結果
        for result in results:
            if result is not None:
                return result

        raise ValueError(f"在目前支援的券商中，查無代碼為 {symbol} 的 ETF")