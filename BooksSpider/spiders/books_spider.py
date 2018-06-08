# -- coding: UTF-8 --

import scrapy

class BooksSpider(scrapy.Spider):

	name = "BooksSpider"
	
	allowed_domains = ["biquge.com.tw"]
	
	url_head = "http://www.biquge.com.tw/"
	
	def start_requests(self):
		for c in range(0, 2):
			for i in range(1, 10):
				url = self.url_head + str(c) + '_'
				if c == 0:
					url += str(i)
				else:
					url += str(c*1000 + i)
				yield scrapy.Request(url, self.parse)


	def parse(self, response):
		print response.url, response.xpath('//*[@id="info"]/h1/text()').extract_first()
		