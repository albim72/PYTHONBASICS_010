from data import SALES_DATA
from models import SalesReport

if __name__ == '__main__':
    report = SalesReport(SALES_DATA)
    report.print_summary()
    report.show_expensive_items(100)
