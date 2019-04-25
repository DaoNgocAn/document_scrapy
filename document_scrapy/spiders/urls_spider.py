import scrapy
from selenium import webdriver

class URLsSpider(scrapy.Spider):
    name = "urls"
    allowed_domains = [
        'vanban.chinhphu.vn',
    ]
    start_urls = [
        'http://vanban.chinhphu.vn/portal/page/portal/chinhphu/hethongvanban',
    ]
    table_names = "doc_list_title_row"

    def __init__(self):
        self.driver = webdriver.Chrome()

    def __del__(self):
        self.driver.close()

    def parse(self, response):
        self.driver.get(response.url)
        found = True
        while found:
            self.driver.find_element_by_id("highlight")
            rows = self.driver.find_elements_by_xpath("//table[@id='highlight']//tr")
            for row in rows[1:]:
                yield {
                    'url': row.find_element_by_tag_name("a").get_attribute("href"),
                }

            navigator = self.driver.find_elements_by_xpath("//span[@class='navigator']/a")

            found = False
            for a in navigator:
                if "S" in a.text:
                    a.click()
                    found=True
                    break

        self.driver.close()
