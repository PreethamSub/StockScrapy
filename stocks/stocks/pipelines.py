# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class StocksPipeline:
    def open_spider(self, spider):
        self.conn = sqlite3.connect('stocksdata.db')
        self.c = self.conn.cursor()
        self.c.execute('''
        CREATE TABLE IF NOT EXISTS data(
          CompanyName TEXT,
          BUYTriggerPrice REAL,
          BUYStopLoss REAL,
          BUYStockTarget1 REAL,
          BUYStockTarget2 REAL,
          SELLTriggerPrice REAL,
          SELLStopLoss REAL,
          SELLStockTarget1 REAL,
          SELLStockTarget2 REAL
        )'''
      )


    def process_item(self, item, spider):
      self.c.execute('''INSERT INTO data VALUES(?,?,?,?,?,?,?,?,?)''', 
      (
        item['CompanyName'],
        item['BUYTriggerPrice'],
        item['BUYStopLoss'],
        item['BUYStockTarget1'],
        item['BUYStockTarget2'],
        item['SELLTriggerPrice'],
        item['SELLStopLoss'],
        item['SELLStockTarget1'],
        item['SELLStockTarget2']))
      self.conn.commit()
      return item

    def close_spider(self, spider):
      self.conn.close()
