import scrapy
import pandas as pd
from stocks.items import StocksItem



class QuotesSpider(scrapy.Spider):
    name = "stocks_1"
    

    def start_requests(self):
      urls = []
      data = pd.read_csv('/content/drive/MyDrive/Scrapy proj/stocks/stocks/spiders/EQUITY_L.csv')
      #df = data.head(1826)
      df = data.head(3)
      codes = df['SYMBOL'].tolist()
      for code in codes:
        lis = 'https://www.stocklinedirect.com/stock-tips-%s.html' % code
        urls.append(lis)
      for url in urls:
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        items = StocksItem()
        keys = [
            'CompanyName',
            'BUYTriggerPrice',
            'BUYStopLoss',
            'BUYStockTarget1',
            'BUYStockTarget2',
            'SELLTriggerPrice',
            'SELLStopLoss',
            'SELLStockTarget1',
            'SELLStockTarget2'
            ]
        values=[]
        values.append(response.css('h1.font-weight-normal.text-secondary span::text').get())
        for item in response.css('div.col-6.col-md-6.col-lg-3.p-1.font-weight-bold'):
            values.append(item.css('ul.list-group li.list-group-item.p-1.h4::text').get())

        items['CompanyName'] = values[0]
        items['BUYTriggerPrice'] = values[1]
        items['BUYStopLoss'] = values[2]
        items['BUYStockTarget1'] = values[3]
        items['BUYStockTarget2'] = values[4]
        items['SELLTriggerPrice'] = values[5]
        items['SELLStopLoss'] = values[6]
        items['SELLStockTarget1'] = values[7]
        items['SELLStockTarget2'] = values[8]

        yield items

