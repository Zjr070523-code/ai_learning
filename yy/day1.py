import os
import time
import yfinance as yf


def fetch_stock(ticker: str, save_dir: str = "data"):
    try:
        # 新版 yfinance 基于 curl_cffi，自带浏览器指纹，无需手动传 session
        t = yf.Ticker(ticker)
        df = t.history(period="1y")
        print(f"\n===={ticker}====")
        print("---head():前五行---")
        print(df.head())
        print("\n---info():数据结构---")
        print(df.info())
        print("\n---describe():统计信息---")
        print(df.describe())
        os.makedirs(save_dir, exist_ok=True)
        filepath = os.path.join(save_dir, f"{ticker}.csv")
        df.to_csv(filepath, index=False, encoding="utf-8-sig")
        print(f"\n已保存:{filepath},共{len(df)}行\n")
        return df
    except Exception as e:
        print(f"获取{ticker}数据失败：{e}")
        return None


if __name__ == "__main__":
    fetch_stock("AAPL")
    time.sleep(10)
    fetch_stock("MSFT")
