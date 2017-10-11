### Author: Ben Tannenwald
### Date: Oct 10, 2017
### Purpose: really simple assignment between online form # and campaign filing

import json

data = {
    '303' : ['Jasmine Ayres', 'Pre Primary', '07/27/2017'],
    '347' : ['Jasmine Ayres', 'Post Primary', '06/09/2017'],

    '282' : ['Kieran Cartharn', 'Pre Primary', '04/19/2017'],
    '314' : ['Kieran Cartharn', '5 Day Primary', '04/27/2017'],
    '331' : ['Kieran Cartharn', 'Post Primary', '06/06/2017'],
    '377' : ['Kieran Cartharn', 'Mid-Cycle/60 Day', '09/08/2017'],

    '245' : ['Priscilla Tyson', 'Annual 2016', '01/31/2017'],
    '263' : ['Priscilla Tyson', 'Mid-Cycle/60 Day', '03/02/2017'],
    '304' : ['Priscilla Tyson', 'Pre Primary', '04/25/2017'],
    '311' : ['Priscilla Tyson', '5 Day Primary', '04/27/2017'],
    '340' : ['Priscilla Tyson', 'Post Primary', '06/08/2017'],
    '385' : ['Priscilla Tyson', 'Mid-Cycle/60 Day', '09/08/2017'],

    '232' : ['Michael Stinziano', 'Quarterly', '10/31/2016'],
    '252' : ['Michael Stinziano', 'Annual 2016', '01/31/2017'],
    '322' : ['Michael Stinziano', 'Quarterly', '04/28/2017'],
    '366' : ['Michael Stinziano', 'Semiannual 2017', '07/31/2017'],

    '231' : ['Elizabeth Brown', 'Quarterly', '10/31/2016'],
    '255' : ['Elizabeth Brown', 'Annual 2016', '01/31/2017'],
    '323' : ['Elizabeth Brown', 'Quarterly', '04/28/2017'],

    '238' : ['Shannon Hardin', 'Quarterly', '11/01/2016'],
    '253' : ['Shannon Hardin', 'Annual 2016', '01/31/2017'],
    '280' : ['Shannon Hardin', 'Mid-Cycle/60 Day', '04/19/2017'],
    '292' : ['Shannon Hardin', 'Pre Primary', '04/20/2017'],
    '316' : ['Shannon Hardin', '5 Day Primary', '04/27/2017'],
    '352' : ['Shannon Hardin', 'Post Primary', '06/09/2017'],
    '388' : ['Shannon Hardin', 'Mid-Cycle/60 Day', '09/08/2017'],

    '291' : ['Mitchell Brown', 'Pre Primary', '04/20/2017'],
    '317' : ['Mitchell Brown', '5 Day Primary', '04/27/2017'],
    '343' : ['Mitchell Brown', 'Post Primary', '06/09/2017'],
    '387' : ['Mitchell Brown', 'Mid-Cycle/60 Day', '09/08/2017'],

    '224' : ['Jaiza Page', 'Quarterly', '10/31/2016'],
    '247' : ['Jaiza Page', 'Annual 2017', '01/31/2017'],
    '362' : ['Jaiza Page', 'Semiannual 2017', '07/30/2017'],

    '287' : ['Whitney Smith', 'Pre Primary', '04/19/2017'],
    '341' : ['Whitney Smith', 'Post Primary', '06/09/2017'],

    '279' : ['Will Petrik', 'Pre Primary', '04/17/2017'],
    '350' : ['Will Petrik', 'Post Primary', '06/12/2017'],

    }

# dump
with open('masterForContributionReports.json', 'w') as fp:
    json.dump(data, fp)


