### Author: Ben Tannenwald
### Date: Oct 10, 2017
### Purpose: really simple (and manual for the moment) assignment between online form # and campaign filing

import json

data = {
    '303' : 'ayres_prePrimary',
    '347' : 'ayres_postPrimary',

    '282' : 'cartharn_prePrimary',
    '314' : 'cartharn_5dayPrimary',
    '331' : 'cartharn_postPrimary',
    '377' : 'cartharn_midCycle60day',

    '245' : 'tyson_annual2016_Jan2017',
    '263' : 'tyson_midCycle60day_March2017',
    '304' : 'tyson_prePrimary',
    '311' : 'tyson_5dayPrimary',
    '340' : 'tyson_postPrimary',
    '385' : 'tyson_midCycle60day_Sept2017',

    '232' : 'stinziano_quarterly_Oct2016',
    '252' : 'stinziano_annual2016_Jan2017',
    '322' : 'stinziano_quarterly_April2017',
    '366' : 'stinziano_semiannual_July2017',

    '231' : 'elizabethBrown_quarterly_Oct2016',
    '255' : 'elizabethBrown_annual2016',
    '323' : 'elizabethBrown_quarterly_April2017',

    '238' : 'hardin_quarterly_Nov2016',
    '253' : 'hardin_annual2016_Jan2017',
    '266' : 'hardin_midCycle60day_March2017',
    '280' : 'hardin_midCycle60day_April2017',
    '292' : 'hardin_prePrimary',
    '316' : 'hardin_5dayPrimary',
    '352' : 'hardin_postPrimary',
    '388' : 'hardin_midCycle60day_Sept2017',

    '291' : 'mitchellBrown_prePrimary',
    '317' : 'mitchellBrown_5dayPrimary',
    '343' : 'mitchellBrown_postPrimary',
    '387' : 'mitchellBrown_midCycle60day_Sept2017',

    '224' : 'page_quarterly_Oct2016',
    '247' : 'page_annual2017_Jan2017',
    '362' : 'page_semiannual_July2017',

    '287' : 'smith_prePrimary',
    '341' : 'smith_postPrimary',

    '279' : 'petrik_prePrimary',
    '350' : 'petrik_postPrimary',

    }

# dump
with open('numberToReportMaster.json', 'w') as fp:
    json.dump(data, fp)


