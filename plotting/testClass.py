### Author: Ben Tannenwald
### Date: Oct 11, 2017
### Purpose: test donorFile class

import json
from donorFile import donorFile

# 0. *** Open restructured JSON file
with open('../structuring/multiForm_restructured_10-10-2017.json') as data_file:
    data = json.load(data_file)

#['Whitney Smith', 'Priscilla Tyson', 'Kieran Cartharn', 'Jasmine Ayres', 'Elizabeth Brown', 'Jaiza Page', 'Shannon Hardin', 'Michael Stinziano', 'Will Petrik', 'Mitchell Brown']

W_Smith     = donorFile( 'Whitney Smith', data['Whitney Smith'] )
P_Tyson     = donorFile( 'Priscilla Tyson', data['Priscilla Tyson'] )
K_Cartharn  = donorFile( 'Kieran Cartharn', data['Kieran Cartharn'] )
J_Ayres     = donorFile( 'Jasmine Ayres', data['Jasmine Ayres'] )
E_Brown     = donorFile( 'Elizabeth Brown', data['Elizabeth Brown'] )
J_Page      = donorFile( 'Jaiza Page', data['Jaiza Page'] )
S_Hardin    = donorFile( 'Shannon Hardin', data['Shannon Hardin'] )
M_Stinziano = donorFile( 'Michael Stinziano', data['Michael Stinziano'] )
W_Petrik    = donorFile( 'Will Petrik', data['Will Petrik'] )
M_Brown     = donorFile( 'Mitchell Brown', data['Mitchell Brown'] )


J_Ayres.printSimpleSummary()
W_Petrik.printSimpleSummary()
W_Smith.printSimpleSummary()
P_Tyson.printSimpleSummary()
K_Cartharn.printSimpleSummary()
E_Brown.printSimpleSummary()
J_Page.printSimpleSummary()
S_Hardin.printSimpleSummary()
M_Stinziano.printSimpleSummary()
M_Brown.printSimpleSummary()

