import scrapy
import string
from avvos.items import avvosItem
class avvosSpider(scrapy.Spider):
	name = "lawyer"
	base_url = 'https://www.avvo.com'
	start_urls = ['https://www.avvo.com/all-lawyers/ny/new_york.html']
	def parse(self,response):
		place_urls = response.xpath('//li[@class="u-margin-bottom-half"]/a/@href').extract()
		for url in place_urls:
			yield scrapy.Request(self.base_url+url, callback=self.lawyer_total)
	def lawyer_total(self,response):
		person_url = response.xpath('//div[@class="col-xs-8"]/a[@class="v-serp-block-link"]/@href').extract()
		for url in person_url:
			 yield scrapy.Request(self.base_url+url, callback=self.person_details)

	def person_details(self,response):
		name = response.xpath('//div[@class="col-xs-8 col-sm-10 col-md-8"]/h1/span/text()').extract()
		licence = response.xpath('//').extract()
		image=response.xpath('//div[@class="col-xs-4 col-sm-2 col-md-4 remove-right-gutter"]//img/@src').extract()
		avvo_rating=response.xpath('//div[@class="u-vertical-padding-half"]/span/text()').extract()
		client_rating=response.xpath('//div[@class="u-vertical-padding-half"]/span/text()').extract()
		reviews=response.xpath('//span[@class="small"]/text()').extract()
		about_me=response.xpath('//div[@class="is-truncated"]/p/text()').extract()
		practice_areas=response.xpath('//li[@class="js-specialty"]/a/text()').extract()
		

			
		name = ''.join(name).strip()
		licence = ''.join(licence).strip()
		image = ''.join(image).strip()
		avvo_rating = ''.join(avvo_rating).strip()
		client_rating = ''.join(client_rating).strip()
		reviews = ''.join(reviews).strip()
		about_me=''.join(about_me).strip()
		practice_areas = ''.join(practice_areas).strip()
		yield avvosItem (
			name = name,
			licence = licence,
			image= image,
			avvo_rating= avvo_rating,
			client_rating=client_rating,
			reviews= reviews,
			about_me=about_me,
			practice_areas=practice_areas

			)
    



