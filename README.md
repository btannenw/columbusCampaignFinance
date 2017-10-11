To run single form crawler and dump information to screen:

$ > scrapy crawl singleForm 

To run single form crawler and store information in JSON:

$ > scrapy crawl singleForm -o singleForm_ayers_prePrimary.json

Replace 'singleForm' with 'multiForm' to run all campaign contribution forms as of 10/10/2017. Master list of URLs and tag information given in scraping/masterForContributionReports.json. To make changes in master JSON, edit scraping/makeMasterSiteJSON.py and re-run to produce new master.