# -*- coding: utf-8 -*-
import json
import scrapy
from maoyan.items import MaoyanItem


class DemoSpider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ['lewan.baidu.com']
    start_urls = ["https://lewan.baidu.com/lewanapi?action=aladdin_rank_games&gameSource=standalone"]

    def parse(self, response):
        result = json.loads(response.body.decode('utf8'))

        for info in result['result']['data']['upcoming']:
            item = {
                "gameId": info['gameId'],
                "gameName": info['gameName'],
                "gameNameEn": info['gameNameEn'],
                "gameTypes": '/'.join(info['gameTypes']),
                "gameSourceName": info["gameSourceName"],
                "gameDesc": info['gameDesc']
            }
            print(item)
            yield MaoyanItem(item)
