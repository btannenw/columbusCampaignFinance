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
            #donorInfo = row.css('span::text').extract()
            donorInfo = row.css('span').extract()
            if len(donorInfo) > 0:
                #{'donorInfo': [u'allen, jerry ', u'Bricker ', u'1201 plaza drive', u'Columbus, OH  43213', u'Credit', u'03/22/2017', u'$50.00', u'31A']}
                #print(dict(donor=donor))

                yield {
                    'donor':          donorInfo[0].split('<span>')[1].split(' </span>')[0],
                    'registrationNo': donorInfo[1].strip('</span>'),
                    'employer' :      donorInfo[2].strip('</span>'),
                    'address' :       donorInfo[3].strip('</span>'),
                    'town' :          donorInfo[4].strip('</span>'),
                    'paymentType' :   donorInfo[5].strip('</span>'),
                    'date' :          donorInfo[6].strip('</span>'),
                    'amount' :        donorInfo[7].strip('</span>'),
                    'form' :          donorInfo[8].strip('</span>'),
                    'eventDate' :     donorInfo[9].strip('</span>'),
                }

                with open(filename, 'wb') as f:
                    f.write(response.body)
                self.log('Saved file %s' % filename)
