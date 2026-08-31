squares = []
for i in range(1,6):
    squares.append(i*i)
squares_c = [i*i for i in range(1,6)]
print("平方列表为：",squares_c)
evens = [x for x in range(1,21) if x % 2 == 0]
print("偶数列表为：",evens)
prices = {"01":100,"02":200,"03":300}
high_prices = {k:v for k,v in prices.items() if v > 100}
print("高价股票为：",high_prices)
ticker = ["AAPL","MSFT","AAPL"]
unique = {t for t in ticker}
print("去重:",unique)
week_close = [10.2,10.5,11.3,10.7,None,11.2,10.0]
valid = [p for p in week_close if p is not None]
print("有效价格为：",valid)
changes = [round(valid[i]-valid[i-1],2) for i in range(1,len(valid))]
print("股价变化为：",changes)
flages = ["涨" if c>0 else "跌" for c in changes]
print ("跌涨标记",flages)
day_flag = {i+2 : flages[i] for i in range(len(flages))}
print("每日对照" , day_flag)