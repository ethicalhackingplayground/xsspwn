#!/usr/bin/python

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class Spider():

	def crawl(self, url, query):

	    name = query
	    allowed_domains = ["www.google.com"]
	    start_urls = url

	    rules = (
		Rule(LinkExtractor(allow=(), restrict_css=('.pageNextPrev',)),
		     callback="parse_item",
		     follow=True),)

	def parse_item(self, response):
		print('Processing..' + response.url)
		return response.url
		
