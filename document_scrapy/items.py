# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DocumentScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    So_Hieu = scrapy.Field(serializer=str)
    Ngay_Ban_Hanh = scrapy.Field(serializer=str)
    Ngay_Co_Hieu_Luc = scrapy.Field(serializer=str)
    Nguoi_Ky = scrapy.Field(serializer=str)
    Trich_Yeu = scrapy.Field(serializer=str)
    Co_Quan_Ban_Hanh = scrapy.Field(serializer=str)
    Phan_Loai = scrapy.Field(serializer=str)
    URLs = scrapy.Field()
