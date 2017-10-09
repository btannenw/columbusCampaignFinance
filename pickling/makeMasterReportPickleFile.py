### Author: Ben Tannenwald
### Date: Oct 9, 2017
### Purpose: really simple (and manual for the moment) assignment between online form # and campaign filing

import pickle

data = {
    '303' : 'ayres_prePrimary',
    '347' : 'ayres_postPrimary',
    '282' : 'cartharn_prePrimary',
    '314' : 'cartharn_5dayPrimary',
    '331' : 'cartharn_postPrimary',
    '377' : 'cartharn_midCycle60day',
    '245' : 'tyson_annual2016',
    '263' : 'tyson_midCycle60day_March2017',
    '304' : 'tyson_prePrimary',
    '311' : 'tyson_5dayPrimary',
    '340' : 'tyson_postPrimary',
    '385' : 'tyson_midCycle60day_Sept2017',
    '232' : 'stinziano_quarterly_Oct2016',
    '252' : 'stinziano_annual2016',
    '' : 'stinziano_',
    '' : 'stinziano_',
    '' : 'stinziano_',
    '' : '',
    '' : '',
    '' : '',
    '' : '',
    '' : '',
    '' : '',
    '' : '',
    '' : '',

    }


output = open('numberToReportMaster.pkl', 'wb')

# Pickle dictionary using protocol 0.
pickle.dump(data, output)
