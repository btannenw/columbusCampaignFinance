### Author: Ben Tannenwald
### Date: Oct 12, 2017
### Purpose: file to store useful functions for plotting contribution information

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
#import numpy as np

def makeTotalAndAllReportHistograms(candidateFile):
    """function for producing histograms showing donation amount"""

    #fig, axes = plt.hist()
    #fig, axes = plt.subplots(rows, 3, figsize=(14,1+3.5*rows))
    #fig.suptitle(candidateFile.candidate, fontsize=20, fontweight='bold')
    #fig.subplots_adjust(wspace = 0.5, hspace = 0.3 )
    
    donation_data = candidateFile.returnAmountValues()
    #makeDonationHistogram(axes[0][0], location_data, 'nContributions')  # ** first column
    #y, x, _ = plt.hist(donation_data, bins=int(max(donation_data)/20))
    n, bins, patches = plt.hist(donation_data, bins=int(max(donation_data)/20))
    plt.title(candidateFile.candidate+': '+'All Contributions', fontsize=18, fontweight='bold')
    plt.ylabel("Number of Contributions", fontsize=18)
    plt.xlabel("Contribution Value [$]", fontsize=15)
    plt.text(150, 20, 'Avg. Contribution: $'+str(candidateFile.totalRaised/candidateFile.totalContributions), fontsize=14)
    print n
    print max(n)
    print dir(n)
    #print 'max', max(x), max(y)
    #print 'bin', y.index(max(y))
    plt.text(150, 20, 'Mean Contribution: $'+str(candidateFile.totalRaised/candidateFile.totalContributions), fontsize=14)


    
def makeDonationHistogram(ax, data):
    """ function to condense plot drawing"""
    labels = ['Columbus, OH', 'Greater Ohio', 'Outside OH']
    colors = ['blue', 'green', 'red']
    
    size = data[ plotType ]
    #remove categories with 0
    for item in size:
        if item == 0:
            del labels[size.index(item)]
            del colors[size.index(item)]
            del size[size.index(item)]

    # keep on rolling
    total = sum(size)
    ax.pie(size, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90, colors=colors) # shows relative values
    if plotType == 'nContributions':
        ax.text(-0.65, 1.4, '# Of Contributions', fontsize=14)
    elif plotType == 'nRaised':
        ax.text(-0.28, 1.4, '$ Raised', fontsize=14)

        

def makeTotalAndAllReportPlotsByLocation(candidateFile):
    """function for producing pie charts splitting donations by location"""

    rows = candidateFile.nReports + 1 # plus one for summary
    fig, axes = plt.subplots(rows, 3, figsize=(14,1+3.5*rows))
    fig.suptitle(candidateFile.candidate, fontsize=20, fontweight='bold')
    fig.subplots_adjust(wspace = 0.5, hspace = 0.3 )
    
    # *** A. First row shows over summary
    location_data = candidateFile.returnContributionLocations()
    makeLocationPieChart(axes[0][0], location_data, 'nContributions')  # ** first column
    makeLocationPieChart(axes[0][1], location_data, 'nRaised')         # ** second column
    makeLocationTextSummary(axes[0][2], location_data)                 # ** third column
    
    # *** B. Loop over time-ordered reports
    row = 1
    for report in candidateFile.orderedReports:
        location_data = candidateFile.returnContributionLocations(report)
        makeLocationPieChart(axes[row][0], location_data, 'nContributions')  # ** first column
        makeLocationPieChart(axes[row][1], location_data, 'nRaised')         # ** second column
        makeLocationTextSummary(axes[row][2], location_data, report, date=candidateFile.filings[report]['filingDate'] )                 # ** third column
            
        # move to next row
        row = row + 1

    fig.savefig( '../figures/byLocation/'+candidateFile.candidate.replace(' ','')+'_Total-PrePrimary-PostPrimary_byLocation.png')
    fig.savefig( '../figures/byLocation/'+candidateFile.candidate.replace(' ','')+'_Total-PrePrimary-PostPrimary_byLocation.pdf')

    
def makeLocationPieChart(ax, data, plotType):
    """ function to condense plot drawing"""
    labels = ['Columbus, OH', 'Greater Ohio', 'Outside OH']
    colors = ['blue', 'green', 'red']
    
    size = data[ plotType ]
    #remove categories with 0
    for item in size:
        if item == 0:
            del labels[size.index(item)]
            del colors[size.index(item)]
            del size[size.index(item)]

    # keep on rolling
    total = sum(size)
    ax.pie(size, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90, colors=colors) # shows relative values
    if plotType == 'nContributions':
        ax.text(-0.65, 1.4, '# Of Contributions', fontsize=14)
    elif plotType == 'nRaised':
        ax.text(-0.28, 1.4, '$ Raised', fontsize=14)


def makeLocationTextSummary(ax, data, report='', date=''):
    """ function to condense report summary"""
    ax.axis('off')
    if report =='':
        ax.text(0.3, 0.9, 'All Contributions', fontsize=14, fontweight = 'bold')
    else:
        ax.text(0.3, 0.9, report, fontsize=14, fontweight = 'bold')
    ax.text(0.3, 0.7, '# of Contributions: ' + str(sum(data['nContributions'])), fontsize=14)
    ax.text(0.3, 0.5, 'Total Raised: $'+ str(sum(data['nRaised'])), fontsize=14)
    if date =='':
        ax.text(0.3, 0.3, 'Filing Date:    N/A', fontsize=14)
    else:
        ax.text(0.3, 0.3, 'Filing Date: ' + date, fontsize=14)
