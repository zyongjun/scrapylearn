import scrapy

class CourseSpider(scrapy.Spider):
    name = "course"
    #allowed_domains = "pan.baidu.com"
    allowed_domains = "pan.baidu.com"
    start_urls = [
        "http://user.qzone.qq.com/1502680353/blog/1471421041?ptlang=2052"
        ]

    def parse(self,response):
        #sel = scrapy.selector.Selector(response)
        filename = response.url.split('/')[-2]
        print("filename:",filename)
        with open("hello","wb") as f:
            f.write(response.body)
