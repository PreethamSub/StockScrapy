import scrapy
import pandas as pd
from stocks.items import StocksItem

class QuotesSpider(scrapy.Spider):
    name = "stocks_1"
    
    def start_requests(self):
      urls = []
      data = pd.read_csv('EQUITY_L.csv')
      #df = data.head(1826)
      #for testing purposes using 3 values of 1826
      df = data.head(3)
      codes = df['SYMBOL'].tolist()
      for code in codes:
        lis = 'https://www.stocklinedirect.com/stock-tips-%s.html' % code
        urls.append(lis)
      for url in urls:
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        data = StocksItem()
        values=[]
        values.append(response.css('h1.font-weight-normal.text-secondary span::text').get())
        for item in response.css('div.col-6.col-md-6.col-lg-3.p-1.font-weight-bold'):
            values.append(item.css('ul.list-group li.list-group-item.p-1.h4::text').get())

        data['CompanyName'] = values[0]
        data['BUYTriggerPrice'] = values[1]
        data['BUYStopLoss'] = values[2]
        data['BUYStockTarget1'] = values[3]
        data['BUYStockTarget2'] = values[4]
        data['SELLTriggerPrice'] = values[5]
        data['SELLStopLoss'] = values[6]
        data['SELLStockTarget1'] = values[7]
        data['SELLStockTarget2'] = values[8]

        yield data
