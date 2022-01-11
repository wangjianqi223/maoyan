# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class MaoyanItem(scrapy.Item):
    gameId = Field()  # 发表时间
    gameName = Field()  # 内容类型
    gameNameEn = Field()  # 缩略图,单张,s3 path
    gameTypes = Field()  # 发表时间
    gameSourceName = Field()  # 内容类型
    gameDesc = Field()  # 缩略图,单张,s3 path
