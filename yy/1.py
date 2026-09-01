# code/fetch_tencent.py
"""腾讯财经数据源 - 替代 Yahoo，国内免翻墙稳定抓取日K线
用法: python fetch_tencent.py
抓取茅台(A股) 和 苹果(美股) 历史数据，分别保存为 CSV
"""

import os
import time
import requests

def fetch_kline(symbol: str, days: int = 320, save_dir: str = "data"):
    """从腾讯接口拉取最近 N 个交易日 K 线并保存 CSV

    参数:
        symbol: 股票标识，A股 sh600519 / sz000001，美股 usAAPL
        days:   拉取多少天数据，腾讯最大支持约 320
        save_dir: 保存目录
    """
    url = "https://web.ifzq.gtimg.cn/appstock/app/fqkline/get"
    params = {"param": f"{symbol},day,,,{days},qfq"}

    try:
        resp = requests.get(url, params=params, timeout=10)
        resp.raise_for_status()          # 状态码非 2xx 就抛异常
        data = resp.json()["data"][symbol]

        # 腾讯可能返回 'qfqday'(前复权) 或 'day'，两者取其一
        rows = data.get("qfqday") or data.get("day")
        if not rows:
            raise ValueError(f"{symbol} 没有返回数据")

        # 组装成简单的列表结构
        records = []
        for r in rows:
            # 每行: 日期, 开盘, 收盘, 最高, 最低, 成交量
            records.append({
                "date": r[0],
                "open": float(r[1]),
                "close": float(r[2]),
                "high": float(r[3]),
                "low": float(r[4]),
                "volume": float(r[5]),
            })

        os.makedirs(save_dir, exist_ok=True)
        filepath = os.path.join(save_dir, f"{symbol}.csv")

        # 用 csv 模块写出
        import csv
        with open(filepath, "w", newline="", encoding="utf-8-sig") as f:
            writer = csv.DictWriter(f, fieldnames=records[0].keys())
            writer.writeheader()          # 写列名
            writer.writerows(records)     # 写数据

        print(f"✔ 已保存: {filepath}，共 {len(records)} 行\n")
        # 简单展示前 5 行
        print("前 3 行示例:")
        for rec in records[:3]:
            print(rec)
        return records

    except Exception as e:
        print(f"✘ 抓取 {symbol} 失败: {e}")
        return None

if __name__ == "__main__":
    # A 股：上海·茅台；美股：苹果
    fetch_kline("sh600519")
    time.sleep(3)
    fetch_kline("usAAPL")