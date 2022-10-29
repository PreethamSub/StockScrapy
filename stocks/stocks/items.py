# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class StocksItem(Item):
    CompanyName = Field()
    BUYTriggerPrice = Field()
    BUYStopLoss = Field()
    BUYStockTarget1 = Field()
    BUYStockTarget2 = Field()
    SELLTriggerPrice = Field()
    SELLStopLoss = Field()
    SELLStockTarget1 = Field()
    SELLStockTarget2 = Field()