### Author: Ben Tannenwald
### Date: Oct 11, 2017
### Purpose: make simple plots

import json
from donorFile import donorFile
from plottingFunctions import *

#import matplotlib.pyplot as plt
#from matplotlib.gridspec import GridSpec

# 0. ***  Open restructured JSON file  *** 
with open('../structuring/multiForm_restructured_10-14-2017.json') as data_file:
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
#makeTotalAndAllReportHistograms(J_Ayres)
#makeTotalAndAllReportHistograms(W_Petrik)
#makeTotalAndAllReportHistograms(P_Tyson)
#makeTotalAndAllReportHistograms(E_Brown)
#makeTotalAndAllReportHistograms(M_Brown)
#makeTotalAndAllReportHistograms(S_Hardin)
#makeTotalAndAllReportHistograms(J_Page)
#makeTotalAndAllReportHistograms(M_Stinziano)

# ***  4. Make histograms showing time evolution of total donations for each candidate  ***   
#makeTotalAndAllReportByTime(J_Ayres)
#makeTotalAndAllReportByTime(W_Petrik)
#makeTotalAndAllReportByTime(P_Tyson)
#makeTotalAndAllReportByTime(E_Brown)
#makeTotalAndAllReportByTime(M_Brown)
#makeTotalAndAllReportByTime(S_Hardin)
#makeTotalAndAllReportByTime(J_Page)
#makeTotalAndAllReportByTime(M_Stinziano)

# ***  5. Make txt files showing multiple donors and total amount donated per candidate  ***   
makeUniqueDonorList(J_Ayres)
makeUniqueDonorList(W_Petrik)
makeUniqueDonorList(P_Tyson)
makeUniqueDonorList(E_Brown)
makeUniqueDonorList(M_Brown)
makeUniqueDonorList(S_Hardin)
makeUniqueDonorList(J_Page)
makeUniqueDonorList(M_Stinziano)

# ***  Last. Show plots  ***
plt.show()
