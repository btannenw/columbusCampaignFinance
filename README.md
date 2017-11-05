# Columbus Campaign Finance
### Scrape data
To run single form crawler and dump information to screen:

$ > scrapy crawl singleForm 

To run single form crawler and store information in JSON:

$ > scrapy crawl singleForm -o singleForm_ayers_prePrimary.json

Replace 'singleForm' with 'multiForm' to run all campaign contribution forms as of 10/10/2017. Master list of URLs and tag information given in scraping/masterForContributionReports.json. To make changes in master JSON, edit scraping/makeMasterSiteJSON.py and re-run to produce new master.

### Re-structuring
To restructure the data scraped from city databases, go to structuring/ and run

$ > python restructureContributionJSON.py

### Analyze
To analyze restructured JSON, go to plotting/ and run

$ > python simplePlots.py

Figures showing campaign contributions as a function of time, by geographical origin, and size of contribution will be produced in figures/. Tables showing number of total contributions and total donated by unique donor are created in tables/. The tables can be produced for individual candidates and for user-specified groupings.

