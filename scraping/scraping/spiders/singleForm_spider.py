import scrapy


class singleFormSpider(scrapy.Spider):
    name = "singleForm"

    def start_requests(self):
        urls = [
            'https://campaignfinance.columbus.gov/ps_contr.aspx?param=303',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("=")[1]
        filename = 'CampaignFinance-%s.html' % page
        for row in response.css('tr'):
            donorInfo = row.css('span::text').extract()
            if len(donorInfo) > 0:
                #{'donorInfo': [u'allen, jerry ', u'Bricker ', u'1201 plaza drive', u'Columbus, OH  43213', u'Credit', u'03/22/2017', u'$50.00', u'31A']}
                donor = donorInfo[0]
                employer = donorInfo[1]
                address = donorInfo[2]
                town = donorInfo[3]
                paymentType = donorInfo[4]
                date = donorInfo[5]
                amount = donorInfo[6]
                form = donorInfo[7]
                #print(dict(donor=donor))

                yield {
                    'donor': donorInfo[0],
                    'employer' : donorInfo[1],
                    'address' : donorInfo[2],
                    'town' : donorInfo[3],
                    'paymentType' : donorInfo[4],
                    'date' : donorInfo[5],
                    'amount' : donorInfo[6],
                    'form' : donorInfo[7],
                }

                with open(filename, 'wb') as f:
                    f.write(response.body)
                self.log('Saved file %s' % filename)
