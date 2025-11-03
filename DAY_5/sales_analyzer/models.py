from typing import List, Dict
from functions import total_revenue,filter_expensive,average_price

class SalesReport:
    def __init__(self, sales_data: List[Dict]):
        self.sales_data = sales_data
        
    def print_summary(self):
        total = sum(map(total_revenue, self.sales_data))
        avg_price = average_price(self.sales_data)
        print(f"Total Revenue: ${total:.2f}")
        print(f"Average Item Price: ${avg_price}")
        
    def show_expensive_items(self, threshold: float):
        print(f"Expensive Items -> price above: ${threshold}")
        for item in filter_expensive(self.sales_data, threshold):
            print(f" - {item['product']}: ${item['price']:.2f}")
