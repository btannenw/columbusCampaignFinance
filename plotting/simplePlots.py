### Author: Ben Tannenwald
### Date: Oct 11, 2017
### Purpose: make simple plots

import json, matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

from donorFile import donorFile
from plottingFunctions import *

#import matplotlib.pyplot as plt
#from matplotlib.gridspec import GridSpec

# 0. *** Open restructured JSON file
with open('../structuring/multiForm_restructured_10-10-2017.json') as data_file:
    data = json.load(data_file)

#['Whitney Smith', 'Priscilla Tyson', 'Kieran Cartharn', 'Jasmine Ayres', 'Elizabeth Brown', 'Jaiza Page', 'Shannon Hardin', 'Michael Stinziano', 'Will Petrik', 'Mitchell Brown']

#W_Smith     = donorFile( 'Whitney Smith', data['Whitney Smith'] )
#P_Tyson     = donorFile( 'Priscilla Tyson', data['Priscilla Tyson'] )
#K_Cartharn  = donorFile( 'Kieran Cartharn', data['Kieran Cartharn'] )
#E_Brown     = donorFile( 'Elizabeth Brown', data['Elizabeth Brown'] )
#J_Page      = donorFile( 'Jaiza Page', data['Jaiza Page'] )
#M_Stinziano = donorFile( 'Michael Stinziano', data['Michael Stinziano'] )
J_Ayres     = donorFile( 'Jasmine Ayres', data['Jasmine Ayres'] )
W_Petrik    = donorFile( 'Will Petrik', data['Will Petrik'] )
M_Brown     = donorFile( 'Mitchell Brown', data['Mitchell Brown'] )
S_Hardin    = donorFile( 'Shannon Hardin', data['Shannon Hardin'] )

# ***  1. Make pre/post primary plots for each candidate  ***   
makeTotalPrePrimaryPostPrimaryPlot(J_Ayres)
#makeTotalPrePrimaryPostPrimaryPlot(W_Petrik)
makeTotalPrePrimaryPostPrimaryPlot(S_Hardin)
#makeTotalPrePrimaryPostPrimaryPlot(M_Brown)



#plt.subplot(the_grid[1, 0], aspect=1)
#ax_ayres_loc_nContrib_all = makeLocationPieChart(ayres_location_all, 'nContributions', 'Jasmine Ayres: All Contributions (By # Of Contributions)')
#ax_ayres_loc_nRaised_all =makeLocationPieChart(ayres_location_all, 'nRaised', 'Jasmine Ayres: All Contributions (By $ Raised)')

plt.show()
