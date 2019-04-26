import scrapy
import json
from selenium import webdriver
from document_scrapy.items import DocumentScrapyItem
from document_scrapy.spiders.utils import get_with_retry
from selenium.webdriver.firefox.options import Options
import logging


class InfoSpider(scrapy.Spider):
    name = 'info'

    def __init__(self):
        options = Options()
        options.headless = True
        self.driver = webdriver.Firefox(options=options)
        # self.driver = webdriver.Chrome()
        logging.basicConfig(filename="info.log", level=logging.WARNING,
                            format='%(asctime)s - %(message)s',
                            datefmt='%d-%b-%y %H:%M:%S')


    def __del__(self):
        self.driver.close()

    def start_requests(self):
        with open('urls.json') as json_file:
            urls = json.load(json_file)
            for url in urls:
                yield scrapy.Request(url=url["url"], callback=self.parse)

    @staticmethod
    def process_input(_i):
        _i = _i.lower()
        if _i == 'Số/Ký hiệu'.lower():
            return 'So_Hieu'
        elif _i == 'Ngày ban hành'.lower():
            return 'Ngay_Ban_Hanh'
        elif _i == 'ngày có hiệu lực':
            return 'Ngay_Co_Hieu_Luc'
        elif _i == 'người ký':
            return 'Nguoi_Ky'
        elif _i == 'trích yếu':
            return 'Trich_Yeu'
        elif _i == 'cơ quan ban hành':
            return 'Co_Quan_Ban_Hanh'
        elif _i == 'phân loại':
            return 'Phan_Loai'
        else:
            return 'unknown'

    def parse(self, response):

        try:
            get_with_retry(self.driver, response.url)
        except Exception as e:
            logging.CRITICAL("Exception occurred", exc_info=True)

        item = DocumentScrapyItem()
        item['URLs'] = []
        item['URL_ROOT'] = response.url

        if "none" in self.driver.find_element_by_id("documentAttr").get_attribute("style"):
            self.driver.find_element_by_xpath('//div[@onclick="viewDocumentAttr()"]').click()
        rows = self.driver.find_elements_by_xpath("//table[@class='doc_detail_attr_table']//tr")
        for row in rows:
            key = self.process_input(row.find_elements_by_tag_name("td")[0].text)
            value = row.find_elements_by_tag_name("td")[1].text
            if key == 'unknown':
                item['unknown'] = f'{row.find_elements_by_tag_name("td")[0].text}: {value}'
            else:
                item[key] = value


        for url in self.driver.find_elements_by_xpath("//a[@class='doc_detail_file_link']"):
            item['URLs'].append(url.get_attribute("href"))

        yield item
