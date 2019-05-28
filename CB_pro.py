import scrapy


class MySpider(scrapy.Spider):
    name = "flip_spider"
    page_no = 1
    url = "https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.processor_brand%255B%255D%3DSnapdragon&p%5B%5D=facets.serviceability%5B%5D%3Dfalse&p%5B%5D=facets.offer_type%255B%255D%3DExchange%2BOffer&otracker=clp_banner_1_10.bannerX3.BANNER_mobile-phones-store_HPUGCU9BYBF6&fm=neo%2Fmerchandising&iid=M_934db066-154e-4074-a4b1-96f56a0af28e_6.HPUGCU9BYBF6&ppt=HomePage&ppn=Home&ssid=85m4yqvgzk0000001558978084715&page="

    def start_requests(self):

        goto = "{}{}".format(self.url, self.page_no)
        yield scrapy.Request(url=goto, callback=self.parse)

    def parse(self, response):

        phone_details = response.css("div._1-2Iqu.row")

        for ph in phone_details:
            phone = ph.css("div._3wU53n::text").get()
            rating = ph.css("div.hGSR34::text").get()
            price = ph.css("div._1vC4OE._2rQ-NK::text").get()

            yield {
                "name": phone,
                "rating": rating,
                "price": price,
            }

        if self.a is not 6:
            self.page_no = self.page_no+1
            next_page = "{}{}".format(self.url, self.page_no)
            yield scrapy.Request(url=next_page, callback=self.parse)
