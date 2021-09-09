import scrapy
from tutorial.items import ItcastItem

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.com']
    start_urls = ["http://www.itcast.cn/channel/teacher.shtml"]

    def parse(self, response):
        # 存放老师信息的集合
        items = []
        for each in response.xpath("//div[@class='li_txt']"):
            #  信息封装到对象中
            item = ItcastItem()
            #  extract()返回的都是unicode字符串
            name = each.xpath("h3/text()").extract()
            title = each.xpath("h4/text()").extract()
            info = each.xpath("p/text()").extract()

            #  xpath返回的是包含一个元素的列表
            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]

            items.append(item)
        return items
