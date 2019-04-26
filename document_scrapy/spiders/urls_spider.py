import scrapy
from selenium import webdriver
from document_scrapy.spiders.utils import get_with_retry
from selenium.webdriver.firefox.options import Options

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
        # options = Options()
        # options.headless = True
        # self.driver = webdriver.Firefox(options=options)
        self.driver = webdriver.Chrome()

    def __del__(self):
        self.driver.close()

    def parse(self, response):
        url = response.url
        try:
            get_with_retry(self.driver, url)
        except:
            import sys
            sys.exit(0)

        found = True
        while found:
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
                    self.driver.find_element_by_xpath("//select[@name='pagesize']").find_elements_by_tag_name("option")[
                        -1].click()
                    found=True
                    break

        self.driver.close()
