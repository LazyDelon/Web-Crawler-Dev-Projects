import twstock

# 取得股票名稱和即時股價
def get_price(stockid):
    rt = twstock.realtime.get(stockid) 
    
    if rt["success"]:
        return (rt["info"]["name"], float(rt["realtime"]["latest_trade_price"]))
    else:
        return (False, False)

# 檢查是否符合四大買賣點
def get_best(stockid):
    stock = twstock.Stock(stockid)
    
    bp = twstock.BestFourPoint(stock).best_four_point()
    
    if(bp):
        return("買進" if bp[0] else "賣出", bp[1])
    else:
        return(False, False)
        
Name, Price = get_price("2330")
act, why = get_best("2330")

print(Name, Price, act, why, sep="|")