# import ssl

# 導入 Python 本身需要一個 HTTP 工具幫你發出「我要資料」的請求。
import httpx

import json

API_URL = "https://etfapi.yuantaetfs.com/ectranslation/api/trans"

PARAMS = {
    "APIType": "ETFBackstage",
    "CompanyName": "YUANTAFUNDS",
    "PageName": "/product/detail/0050/Basic_information",
    "DeviceId": "6640008f-f7f4-4217-ba91-6fafc27ccacf",
    "FuncId": "ETFTag/GetProductInformation",
    "AppName": "ETF",
    "Device": "4",
    "Platform": "ETF",
}

# 我宣告一個「取得 ETF 資料」的功能
def get_etf_data():
    response = httpx.get(
        API_URL,
        params=PARAMS,
        # SSL 暫時 verify=False ; 待處理
        verify=False
    )
    # 印出狀態碼: 
    print("Status:", response.status_code)
    # 如果 API 回傳錯誤，就直接讓 Python 報錯。
    response.raise_for_status()
    # 把 API 回傳的 JSON 轉成 Python 可以操作的資料
    return response.json()

# 我宣告一個「整理 ETF 資料」的功能
# data 來源是：
# data = get_etf_data()
def parse_etf_data(data):
    etfs = []
    # for 自取變數名稱 in 資料 ; 把 API 回傳的分類一個一個拿出來
    for category in data["Data"]:
        category_name = category["TagName"]
        # for 自取變數名稱 in 資料 ; 再把每個分類裡面的 ETF 一支一支拿出來
        for item in category["ProductInformationList"]:
            etf = {
                # "code": item["STK_CD"],
                # "name": item["FUND_NAME"],
                # "category": category_name,
                # "price": item["CLOSE_PRICE"],
                # "change": item["FLUCT"],
                # "change_percent": item["FLUCT_PERCENT"],
                # "volume": item["VOLUME"],

                "symbol": item["STK_CD"],
                "name": item["FUND_NAME"],
                "issuer": "元大投信",
            }
            # 把整理好的 ETF 放進清單
            etfs.append(etf)
    # 整理完了，把全部 ETF 清單交出去。
    return etfs


if __name__ == "__main__":
    data = get_etf_data()

    # 暫時把 API 原始 JSON 印出來
    print(json.dumps(data["Data"][0], indent=2, ensure_ascii=False))
    # print(data.keys())

    etfs = parse_etf_data(data)

    for etf in etfs:
        print(etf)

