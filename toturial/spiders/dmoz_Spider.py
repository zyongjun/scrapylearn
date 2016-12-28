import scrapy
from toturial.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = "dmoz.org"
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"]

    def parse(self,response):

        sel = scrapy.selector.Selector(response)
        sites = sel.xpath('//div[@class="site-item "]/div[@class="title-and-desc"]')
        items = []
        for site in sites:
            item = DmozItem()
            item['link'] = site.xpath('a/@href').extract()
            item['title'] = site.xpath('a/div[@class="site-title"]/text()').extract()
            item['desc'] = site.xpath('div[@class="site-descr "]/text()').extract()
            items.append(item)
        return items
        
