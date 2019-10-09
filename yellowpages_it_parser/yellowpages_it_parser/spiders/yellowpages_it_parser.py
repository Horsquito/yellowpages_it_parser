import scrapy
from scrapy_splash import SplashRequest
from ..items import YellowpagesItParserItem
import requests
from datetime import datetime
from lxml import html

class Spider(scrapy.Spider):
    name = 'yellowpages_it_parser'

    def start_requests(self):
        url = 'https://www.indotrading.com/searchkeyword.aspx?keyword=' + self.product
        yield SplashRequest(url, self.parse)

    def parse(self, response):
            links = response.xpath('//h3/a[@class="product_title"]/@href').getall()
            for link in links:
                yield SplashRequest(link, self.get_company_page)

    def get_company_page(self, response):
        item = YellowpagesItParserItem()
        token = 'EAAAAFouYgi1XqoWY4YWj+q2K5rkjEtMsdtr0oNBYP0pDQZS1mZbfw38tSvuKJWM4Uum7w=='
        url = 'https://www.indotrading.com/AjaxMethod.asmx/UpdateCompanyPhoneLeads'
        website = response.xpath('//h4[@class="company-name mt-30"]/a/@href').get()
        name = response.xpath('//h4[@class="company-name mt-30"]/a/text()').get()
        id = response.xpath('//form[@id="form1"]/script[1]/text()').get()
        id = id.split('\'')
        product_id = id[1]
        company_id = id[3]
        data = {'Token': token, 'EncCompanyID': company_id, 'ProductID': product_id}
        phone = requests.post(url=url, data=data)
        phone = html.fromstring(phone.content)
        phone = phone.xpath('//string/text()')
        date_and_time = datetime.now().strftime('%d-%m %H:%M')
        item['date_and_time'] = date_and_time
        item['name'] = name
        item['source'] = 'https://www.indotrading.com'
        item['website'] = website
        item['hs_code'] = self.hs_code
        item['phone'] = phone
        item['product'] = self.product
        yield item
