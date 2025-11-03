from typing import List,Dict

def total_revenue(item: Dict[str, float]) -> float:
    return item["price"] * item["quantity"]

def filter_expensive(data: List[Dict[str, float]],threshold: float) -> List[Dict]:
    return list(filter(lambda x: x["price"] > threshold, data))

def average_price(data: List[Dict]) -> float:
    prices = list(map(lambda x: x["price"], data))  
    return sum(prices)/len(prices)
