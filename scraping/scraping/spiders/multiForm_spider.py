import scrapy, json


class multiFormSpider(scrapy.Spider):
    name = "multiForm"

    
    # *** Create list of URLs to scrape for financial data
    def start_requests(self):
        urls = []
        
        # ** Open JSON file with URL and form information
        with open('numberToReportMaster.json') as data_file:
            data = json.load(data_file)
            
        for key in data.keys():
            urls.append('https://campaignfinance.columbus.gov/ps_contr.aspx?param='+key)

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # *** Run through URL and parse information
    def parse(self, response):
        page = response.url.split("=")[1]
        filename = 'CampaignFinance-%s.html' % page
        # ** Open JSON file with URL and form information
        with open('numberToReportMaster.json') as data_file:
            data = json.load(data_file)

        for row in response.css('tr'):
            #donorInfo = row.css('span::text').extract()
            donorInfo = row.css('span').extract()
            if len(donorInfo) > 0:
                #print(dict(donor=donor))

                yield {
                    'key':            data[page],
                    'donor':          donorInfo[0].split('<span>')[1].split(' </span>')[0].split('</span>')[0],
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
