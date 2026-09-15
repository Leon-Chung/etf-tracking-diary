import httpx
from bs4 import BeautifulSoup


BASE_URL = "https://websys.fsit.com.tw/FubonETF/Fund/Assets.aspx"


def get_etf_holdings_data(symbol: str):

    params = {
        "stkId": symbol,
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


def parse_etf_holdings(html: str):

    holdings = []

    soup = BeautifulSoup(html, "html.parser")

    tables = soup.find_all("table")

    for table in tables:

        rows = table.find_all("tr")

        for row in rows:

            cells = row.find_all(["td", "th"])

            if not cells:
                continue

            values = [
                cell.get_text(" ", strip=True)
                for cell in cells
            ]

            if len(values) >= 5 and values[0].isdigit():

                holding = {
                    "rank": len(holdings) + 1,
                    "stock_symbol": values[0],
                    "stock_name": values[1],
                    "weight": values[4],
                }

                holdings.append(holding)

    return holdings


# ==========================================
# 給 etf_info_fubon 呼叫的主要函式
# ==========================================

def get_etf_holdings(etf: dict):

    symbol = etf["symbol"]

    print("開始抓取富邦 ETF 持股:", symbol)

    html = get_etf_holdings_data(symbol)

    holdings = parse_etf_holdings(html)

    print("持股數量:", len(holdings))

    return holdings

# ==========================================
# 測試
# ==========================================

if __name__ == "__main__":

    # 模擬 etf_info_fubon 搜尋後得到的 ETF
    etf = {
        "symbol": "006208",
    }

    holdings = get_etf_holdings(etf)

    print("\n========== ETF 持股 ==========")

    for holding in holdings:
        print(holding)

    print("==============================")