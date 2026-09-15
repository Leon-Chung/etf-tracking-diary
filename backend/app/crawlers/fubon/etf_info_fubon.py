# # 導入 Python 本身需要一個 HTTP 工具，
# # 幫你發出「我要資料」的請求。
# import httpx

# # BeautifulSoup 用來解析 HTML 網頁。
# from bs4 import BeautifulSoup

# # re 用來從網頁文字中找出 ETF 代碼與名稱。
# import re


# BASE_URL = "https://websys.fsit.com.tw/FubonETF/Fund/Profile.aspx"


# # 我宣告一個「取得 ETF 資料」的功能
# # stk_id 就是 ETF 股票代碼，例如：
# # 0052、006208、00692
# def get_etf_data(stk_id):
#     params = {
#         "stkId": stk_id,
#     }

#     response = httpx.get(
#         BASE_URL,
#         params=params,
#         timeout=10.0,
#         follow_redirects=True,
#     )

#     # 印出狀態碼
#     print("Status:", response.status_code)

#     # 如果 HTTP 回傳錯誤，就直接讓 Python 報錯。
#     response.raise_for_status()

#     # 回傳 HTML 原始資料
#     return response.text


# # 我宣告一個「整理 ETF 資料」的功能
# #
# # html 來源是：
# # html = get_etf_data("0052")
# def parse_etf_data(html):
#     # 把 HTML 交給 BeautifulSoup 解析
#     soup = BeautifulSoup(html, "html.parser")

#     # 把整個網頁的文字拿出來
#     text = soup.get_text(" ", strip=True)

#     # 富邦頁面目前會出現：
#     #
#     # 0052 / 富邦科技
#     #
#     # 所以我們從網頁文字裡找這個格式。
#     match = re.search(
#         r"\b([0-9]{4,6}[A-Z]?)\s*/\s*([^\s]+)",
#         text
#     )

#     # 如果找不到 ETF 資料，就報錯。
#     if not match:
#         raise ValueError("找不到 ETF 代碼與名稱")

#     symbol = match.group(1)
#     name = match.group(2)

#     etf = {
#         "symbol": symbol,
#         "name": name,
#         "issuer": "富邦投信",
#     }

#     return etf


# if __name__ == "__main__":

#     # 先測試 0052
#     data = get_etf_data("0052")

#     # 暫時把 HTML 前 1000 個字印出來
#     print(data[:1000])

#     # 整理 ETF 資料
#     etf = parse_etf_data(data)

#     print(etf)


# -----------------------------------------------------------------------

import httpx
from bs4 import BeautifulSoup
import re


BASE_URL = "https://websys.fsit.com.tw/FubonETF/Fund/Profile.aspx"


def get_etf_data(stk_id):
    params = {
        "stkId": stk_id,
    }

    response = httpx.get(
        BASE_URL,
        params=params,
        timeout=10.0,
        follow_redirects=True,
    )

    print("Status:", response.status_code)

    response.raise_for_status()

    return response.text


def parse_etf_data(html):

    soup = BeautifulSoup(html, "html.parser")

    text = soup.get_text(" ", strip=True)

    match = re.search(
        r"\b([0-9]{4,6}[A-Z]?)\s*/\s*([^\s]+)",
        text
    )

    if not match:
        raise ValueError("找不到 ETF 代碼與名稱")

    symbol = match.group(1)
    name = match.group(2)

    etf = {
        "symbol": symbol,
        "name": name,
        "issuer": "富邦投信",
    }

    return etf


# ==========================================
# 給其他程式呼叫
# ==========================================

def get_etf_info(stk_id):

    print("開始取得富邦 ETF:", stk_id)

    html = get_etf_data(stk_id)

    etf = parse_etf_data(html)

    return etf


# ==========================================
# 單獨測試 etf_info_fubon
# ==========================================

if __name__ == "__main__":

    stk_id = "0052"

    etf = get_etf_info(stk_id)

    print(etf)