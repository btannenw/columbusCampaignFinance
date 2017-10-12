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

J_Ayres     = donorFile( 'Jasmine Ayres', data['Jasmine Ayres'] )
W_Petrik    = donorFile( 'Will Petrik', data['Will Petrik'] )
P_Tyson     = donorFile( 'Priscilla Tyson', data['Priscilla Tyson'] )
E_Brown     = donorFile( 'Elizabeth Brown', data['Elizabeth Brown'] )
M_Brown     = donorFile( 'Mitchell Brown', data['Mitchell Brown'] )
S_Hardin    = donorFile( 'Shannon Hardin', data['Shannon Hardin'] )
J_Page      = donorFile( 'Jaiza Page', data['Jaiza Page'] )
M_Stinziano = donorFile( 'Michael Stinziano', data['Michael Stinziano'] )
K_Cartharn  = donorFile( 'Kieran Cartharn', data['Kieran Cartharn'] )
W_Smith     = donorFile( 'Whitney Smith', data['Whitney Smith'] )

# ***  1. Make plots showing contributions split by location for each candidate  ***   
#makeTotalandAllReportPlotsByLocation(J_Ayres)
#makeTotalandAllReportPlotsByLocation(W_Petrik)
#makeTotalandAllReportPlotsByLocation(P_Tyson)
#makeTotalandAllReportPlotsByLocation(E_Brown)
makeTotalandAllReportPlotsByLocation(M_Brown)
#makeTotalandAllReportPlotsByLocation(S_Hardin)
makeTotalandAllReportPlotsByLocation(J_Page)
#makeTotalandAllReportPlotsByLocation(M_Stinziano)


# ***  2. Make plots showing contributions split by location for each candidate  ***   

# ***  Last. Show plots  ***
plt.show()
