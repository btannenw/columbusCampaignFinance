### Author: Ben Tannenwald
### Date: Oct 12, 2017
### Purpose: file to store useful functions for plotting contribution information

import operator, matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec


def makeTotalPrePrimaryPostPrimaryPlot(candidateFile):
    """function for producing complicated pie chart"""

    rows = candidateFile.nReports + 1 # plus one for summary
    fig, axes = plt.subplots(rows, 3, figsize=(14,1+4*rows))
    fig.suptitle(candidateFile.candidate, fontsize=20, fontweight='bold')

    # *** A. First row shows over summary
    location_data = candidateFile.returnContributionLocations()
    makeLocationPieChart(axes[0][0], location_data, 'nContributions')  # ** first column
    makeLocationPieChart(axes[0][1], location_data, 'nRaised')         # ** second column
    makeLocationTextSummary(axes[0][2], location_data)                 # ** third column
    
    # *** B. Blunt force approach to ordering reports by date
    date_list = {}
    for report in candidateFile.reports:
        date_raw = candidateFile.filings[report]['filingDate']
        date_list[report] = date_raw.split('/')[2] + '/' + date_raw.split('/')[0] + '/' + date_raw.split('/')[1]
    sorted_dates = sorted(date_list.items(), key=operator.itemgetter(1))
    
    # *** C. Loop over time-ordered reports
    row = 1
    for tup in sorted_dates:
        report = tup[0]
        location_data = candidateFile.returnContributionLocations(report)
        makeLocationPieChart(axes[row][0], location_data, 'nContributions')  # ** first column
        makeLocationPieChart(axes[row][1], location_data, 'nRaised')         # ** second column
        makeLocationTextSummary(axes[row][2], location_data, report, date=candidateFile.filings[report]['filingDate'] )                 # ** third column
            
        # move to next row
        row = row + 1

    fig.savefig( '../figures/'+candidateFile.candidate.replace(' ','')+'_Total-PrePrimary-PostPrimary_byLocation.png')
    fig.savefig( '../figures/'+candidateFile.candidate.replace(' ','')+'_Total-PrePrimary-PostPrimary_byLocation.pdf')

    
def makeLocationPieChart(ax, data, plotType):
    """ function to condense plot drawing"""
    labels = ['Columbus, OH', 'Greater Ohio', 'Outside OH']
    
    size = data[ plotType ]
    #remove categories with 0
    for item in size:
        if item == 0:
            del labels[size.index(item)]
            del size[size.index(item)]

    # keep on rolling
    total = sum(size)
    ax.pie(size, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90) # shows relative values
    ax.text(-0.65, 1.2, '# Of Contributions', fontsize=14)
    
    if plotType == 'nContributions':
        ax.text(-0.65, 1.2, '# Of Contributions', fontsize=14)
    elif plotType == 'nDonations':
        ax.text(-0.28, 1.2, '$ Raised', fontsize=14)


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
