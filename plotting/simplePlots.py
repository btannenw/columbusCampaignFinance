### Author: Ben Tannenwald
### Date: Oct 11, 2017
### Purpose: make simple plots

import json, matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

from donorFile import donorFile
from plottingFunctions import *

#import matplotlib.pyplot as plt
#from matplotlib.gridspec import GridSpec

# 0. ***  Open restructured JSON file  *** 
with open('../structuring/multiForm_restructured_10-10-2017.json') as data_file:
    data = json.load(data_file)


# 1. ***  Create donor file for each candidate
J_Ayres     = donorFile( 'Jasmine Ayres', data['Jasmine Ayres'] )
W_Petrik    = donorFile( 'Will Petrik', data['Will Petrik'] )
P_Tyson     = donorFile( 'Priscilla Tyson', data['Priscilla Tyson'] )
E_Brown     = donorFile( 'Elizabeth Brown', data['Elizabeth Brown'] )
M_Brown     = donorFile( 'Mitchell Brown', data['Mitchell Brown'] )
S_Hardin    = donorFile( 'Shannon Hardin', data['Shannon Hardin'] )
J_Page      = donorFile( 'Jaiza Page', data['Jaiza Page'] )
M_Stinziano = donorFile( 'Michael Stinziano', data['Michael Stinziano'] )
#K_Cartharn  = donorFile( 'Kieran Cartharn', data['Kieran Cartharn'] )
#W_Smith     = donorFile( 'Whitney Smith', data['Whitney Smith'] )

# ***  2. Make plots showing contributions split by location for each candidate  ***   
#makeTotalAndAllReportPlotsByLocation(J_Ayres)
#makeTotalAndAllReportPlotsByLocation(W_Petrik)
#makeTotalAndAllReportPlotsByLocation(P_Tyson)
#makeTotalAndAllReportPlotsByLocation(E_Brown)
#makeTotalAndAllReportPlotsByLocation(M_Brown)
#makeTotalAndAllReportPlotsByLocation(S_Hardin)
#makeTotalAndAllReportPlotsByLocation(J_Page)
#makeTotalAndAllReportPlotsByLocation(M_Stinziano)


# ***  3. Make histograms showing size of donations for each candidate  ***
makeTotalAndAllReportHistograms(J_Ayres)
makeTotalAndAllReportHistograms(W_Petrik)
makeTotalAndAllReportHistograms(P_Tyson)
makeTotalAndAllReportHistograms(E_Brown)
makeTotalAndAllReportHistograms(M_Brown)
makeTotalAndAllReportHistograms(S_Hardin)
makeTotalAndAllReportHistograms(J_Page)
makeTotalAndAllReportHistograms(M_Stinziano)

# ***  3. Make histograms showing time evolution of total donations for each candidate  ***   

# ***  Last. Show plots  ***
plt.show()
